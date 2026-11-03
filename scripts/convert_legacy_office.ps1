# แปลงไฟล์ .doc/.xls ใน data/raw/ เป็น .docx/.xlsx เพราะ extract.py อ่านได้แค่ไฟล์ Office รุ่นใหม่
#
# บางไฟล์จาก iDisc เป็น .docx/.xlsx อยู่แล้วแต่ตั้งนามสกุลผิด (ขึ้นต้นด้วย "PK")
# ไฟล์แบบนี้คัดลอกแล้วเปลี่ยนนามสกุลก็พอ ไม่ต้องเปิด Word/Excel
# ไฟล์รุ่นเก่าจริง (ขึ้นต้นด้วย D0 CF 11 E0) ต้องเปิดด้วย Word/Excel ในเครื่อง แบบอ่านอย่างเดียวและปิดมาโคร
# ถ้าไฟล์ไหนแปลงนานเกิน $timeoutSec วินาที (Word/Excel มักค้างที่หน้าต่างที่มองไม่เห็น) จะข้ามและแจ้ง
#
# ไฟล์ที่ได้ชื่อ <ชื่อเดิม>.converted.docx / .converted.xlsx วางข้างไฟล์ต้นฉบับ
# ไฟล์ต้นฉบับไม่ถูกแก้ และ build_sources.py ข้ามไฟล์ .converted. เพราะไม่ใช่เอกสารต้นทาง
#
# ใช้: powershell -ExecutionPolicy Bypass -File scripts/convert_legacy_office.ps1
# แล้วรัน extract.py กับโฟลเดอร์ของหุ้นนั้นอีกครั้ง

param([int]$timeoutSec = 90)

$root = Resolve-Path (Join-Path $PSScriptRoot '..\data\raw')
$files = Get-ChildItem -Recurse -File $root | Where-Object { $_.Extension -in '.doc', '.xls' }

$convert = {
    param($app, $src, $out)
    $forceDisableMacros = 3
    if ($app -eq 'word') {
        $o = New-Object -ComObject Word.Application
        $o.Visible = $false; $o.DisplayAlerts = 0; $o.AutomationSecurity = $forceDisableMacros
        try {
            $d = $o.Documents.Open($src, $false, $true)
            $d.SaveAs2($out, 16)   # 16 = wdFormatXMLDocument (.docx)
            $d.Close($false)
        } finally { $o.Quit() }
    } else {
        $o = New-Object -ComObject Excel.Application
        $o.Visible = $false; $o.DisplayAlerts = $false; $o.AutomationSecurity = $forceDisableMacros
        try {
            $w = $o.Workbooks.Open($src, 0, $true)
            $w.SaveAs($out, 51)    # 51 = xlOpenXMLWorkbook (.xlsx)
            $w.Close($false)
        } finally { $o.Quit() }
    }
}

foreach ($f in $files) {
    $ext = if ($f.Extension -eq '.doc') { '.docx' } else { '.xlsx' }
    $out = Join-Path $f.DirectoryName ($f.BaseName + '.converted' + $ext)
    $rel = $f.FullName.Substring($root.Path.Length + 1)
    if (Test-Path $out) { "ข้าม (แปลงไว้แล้ว)  $rel"; continue }

    $head = [System.IO.File]::ReadAllBytes($f.FullName)[0..1]
    if ($head[0] -eq 0x50 -and $head[1] -eq 0x4B) {
        Copy-Item $f.FullName $out
        "เปลี่ยนนามสกุล   $rel"
        continue
    }

    $app = if ($f.Extension -eq '.doc') { 'word' } else { 'excel' }
    $before = @(Get-Process WINWORD, EXCEL -ErrorAction SilentlyContinue | ForEach-Object Id)
    $job = Start-Job -ScriptBlock $convert -ArgumentList $app, $f.FullName, $out
    if (Wait-Job $job -Timeout $timeoutSec) {
        Receive-Job $job -ErrorAction SilentlyContinue | Out-Null
        if (Test-Path $out) { "แปลงด้วย $app   $rel" } else { "แปลงไม่สำเร็จ    $rel" }
    } else {
        "ค้างเกิน $timeoutSec วินาที ข้าม  $rel"
        # ปิดเฉพาะ Word/Excel ที่สคริปต์นี้เปิดขึ้นมา ไม่แตะตัวที่ผู้ใช้เปิดอยู่ก่อน
        Get-Process WINWORD, EXCEL -ErrorAction SilentlyContinue |
            Where-Object { $_.Id -notin $before } | Stop-Process -Force
    }
    Remove-Job $job -Force
}
