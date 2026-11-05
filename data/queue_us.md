# data/queue_us.md

> คิวหุ้นสหรัฐ (S&P 500 รวม Nasdaq-100) ที่ยังไม่ได้ทำ ชุดละ 15 ตัว ยังไม่รัน รอผู้เรียนตรวจ
>
> - **เป็นลำดับคิวเท่านั้น ไม่ใช่หลักฐาน** รายชื่อมาจาก `data/candidates_us.md` (ตัดตัวที่ทำแล้วในรอบ 65 ออก เหลือ '+str(len(cand))+' บริษัท ที่มาและวันที่ดึงอยู่ในไฟล์นั้น)
> - **ตัวที่ 1–46 (ชุด 2–4 และ LMT)** เรียงตามลำดับมูลค่าตลาดจากไฟล์ `sp500_nasdaq100_top_stocks.csv` ของผู้เรียน ไม่เขียนตัวเลขมูลค่าลง repo เพราะ CSV ไม่มีแหล่งที่มาและไม่อยู่ใน Trust sources
> - **ตัวที่ 47 เป็นต้นไป** ยังไม่มีข้อมูลลำดับมูลค่า เรียงตามกลุ่ม GICS แล้วตามตัวอักษรเหมือน `candidates_us.md` ถ้าต้องการเรียงใหม่ ต้องมีข้อมูลมูลค่าจากผู้เรียน
> - ชุดที่ 1 ทำแล้ว (รอบ 65): SPCX AAPL META TSLA BRK.B WMT JPM V XOM JNJ
> - **ชื่อคีย์ที่ใช้ในระบบ** ต้องไม่ซ้ำทั้ง repo (ใช้เป็นชื่อโฟลเดอร์ `data/raw/us/<คีย์>` และ doc_id) BA ไทยใช้ไปแล้ว Boeing จึงใช้คีย์ `BA.US` (แสดงเป็น US:BA ได้ แต่ `:` ใช้ในชื่อโฟลเดอร์ Windows ไม่ได้) ถ้าเจอซ้ำกับหุ้นไทยตัวอื่น ให้ใช้ `<ตัว>.US` เหมือนกัน
> - สถานะ: `รอ` ยังไม่ทำ · `ทำแล้ว` เสร็จและอยู่ใน `output/data.json` อัปเดตตอนจบแต่ละชุด

| ชุด | ลำดับ | คีย์ | ชื่อบริษัท | กลุ่ม | ลำดับมูลค่า | สถานะ |
|---|---|---|---|---|---|---|
| 2 | 1 | MA | Mastercard | Financials | จาก CSV | ทำแล้ว |
| 2 | 2 | ABBV | AbbVie | Health Care | จาก CSV | ทำแล้ว |
| 2 | 3 | COST | Costco | Consumer Staples | จาก CSV | ทำแล้ว |
| 2 | 4 | CVX | Chevron Corporation | Energy | จาก CSV | ทำแล้ว |
| 2 | 5 | KO | Coca-Cola Company (The) | Consumer Staples | จาก CSV | ทำแล้ว |
| 2 | 6 | CSCO | Cisco | Information Technology | จาก CSV | ทำแล้ว |
| 2 | 7 | PG | Procter & Gamble | Consumer Staples | จาก CSV | ทำแล้ว |
| 2 | 8 | MRK | Merck & Co. | Health Care | จาก CSV | ทำแล้ว |
| 2 | 9 | UNH | UnitedHealth Group | Health Care | จาก CSV | ทำแล้ว |
| 2 | 10 | BAC | Bank of America | Financials | จาก CSV | ทำแล้ว |
| 2 | 11 | HD | Home Depot (The) | Consumer Discretionary | จาก CSV | ทำแล้ว |
| 2 | 12 | GE | GE Aerospace | Industrials | จาก CSV | ทำแล้ว |
| 2 | 13 | PM | Philip Morris International | Consumer Staples | จาก CSV | ทำแล้ว |
| 2 | 14 | INTC | Intel | Information Technology | จาก CSV | ทำแล้ว |
| 2 | 15 | MS | Morgan Stanley | Financials | จาก CSV | ทำแล้ว |
| 3 | 16 | AMAT | Applied Materials | Information Technology | จาก CSV | ทำแล้ว |
| 3 | 17 | PANW | Palo Alto Networks | Information Technology | จาก CSV | ทำแล้ว |
| 3 | 18 | TXN | Texas Instruments | Information Technology | จาก CSV | ทำแล้ว |
| 3 | 19 | LRCX | Lam Research | Information Technology | จาก CSV | ทำแล้ว |
| 3 | 20 | NFLX | Netflix | Communication Services | จาก CSV | ทำแล้ว |
| 3 | 21 | CAT | Caterpillar Inc. | Industrials | จาก CSV | ทำแล้ว |
| 3 | 22 | GS | Goldman Sachs | Financials | จาก CSV | ทำแล้ว |
| 3 | 23 | RTX | RTX Corporation | Industrials | จาก CSV | ทำแล้ว |
| 3 | 24 | WFC | Wells Fargo | Financials | จาก CSV | ทำแล้ว |
| 3 | 25 | TMO | Thermo Fisher Scientific | Health Care | จาก CSV | ทำแล้ว |
| 3 | 26 | AMGN | Amgen | Health Care | จาก CSV | ทำแล้ว |
| 3 | 27 | CRWD | CrowdStrike | Information Technology | จาก CSV | ทำแล้ว |
| 3 | 28 | LIN | Linde plc | Materials | จาก CSV | ทำแล้ว |
| 3 | 29 | AXP | American Express | Financials | จาก CSV | ทำแล้ว |
| 3 | 30 | GILD | Gilead Sciences | Health Care | จาก CSV | ทำแล้ว |
| 4 | 31 | C | Citigroup | Financials | จาก CSV | ทำแล้ว |
| 4 | 32 | DIS | Walt Disney Company (The) | Communication Services | จาก CSV | ทำแล้ว |
| 4 | 33 | MCD | McDonald's | Consumer Discretionary | จาก CSV | ทำแล้ว |
| 4 | 34 | PEP | PepsiCo | Consumer Staples | จาก CSV | ทำแล้ว |
| 4 | 35 | VZ | Verizon | Communication Services | จาก CSV | ทำแล้ว |
| 4 | 36 | CRM | Salesforce | Information Technology | จาก CSV | ทำแล้ว |
| 4 | 37 | UNP | Union Pacific Corporation | Industrials | จาก CSV | ทำแล้ว |
| 4 | 38 | DE | Deere & Company | Industrials | จาก CSV | ทำแล้ว |
| 4 | 39 | WELL | Welltower | Real Estate | จาก CSV | ทำแล้ว |
| 4 | 40 | TMUS | T-Mobile US | Communication Services | จาก CSV | ทำแล้ว |
| 4 | 41 | COP | ConocoPhillips | Energy | จาก CSV | ทำแล้ว |
| 4 | 42 | TJX | TJX Companies | Consumer Discretionary | จาก CSV | ทำแล้ว |
| 4 | 43 | T | AT&T | Communication Services | จาก CSV | ทำแล้ว |
| 4 | 44 | UBER | Uber | Industrials | จาก CSV | ทำแล้ว |
| 4 | 45 | BA.US | Boeing (US:BA) | Industrials | จาก CSV | ทำแล้ว |
| 5 | 46 | LMT | Lockheed Martin | Industrials | จาก CSV | ทำแล้ว |
| 5 | 47 | APP | AppLovin | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 48 | CHTR | Charter Communications | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 49 | CMCSA | Comcast | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 50 | ECHO | EchoStar | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 51 | FOXA | Fox Corporation (Class A) | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 52 | LYV | Live Nation Entertainment | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 53 | NWSA | News Corp (Class A) | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 54 | OMC | Omnicom Group | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 55 | RDDT | Reddit | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 56 | SKYD | Skydance | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 57 | TKO | TKO Group Holdings | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 58 | TTWO | Take-Two Interactive | Communication Services | ยังไม่มี | ทำแล้ว |
| 5 | 59 | APTV | Aptiv | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 5 | 60 | AZO | AutoZone | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 61 | BBY | Best Buy | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 62 | CMG | Chipotle Mexican Grill | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 63 | CVNA | Carvana | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 64 | DASH | DoorDash | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 65 | DECK | Deckers Brands | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 66 | DHI | D. R. Horton | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 67 | DPZ | Domino's | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 68 | DRI | Darden Restaurants | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 69 | EBAY | eBay Inc. | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 70 | F | Ford Motor Company | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 71 | GM | General Motors | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 72 | GPC | Genuine Parts Company | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 73 | GRMN | Garmin | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 74 | HAS | Hasbro | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 6 | 75 | LEN | Lennar | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 76 | LOW | Lowe's | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 77 | LULU | Lululemon Athletica | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 78 | MGM | MGM Resorts | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 79 | NKE | Nike, Inc. | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 80 | NVR | NVR, Inc. | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 81 | ORLY | O'Reilly Automotive | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 82 | PHM | PulteGroup | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 83 | RL | Ralph Lauren Corporation | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 84 | ROST | Ross Stores | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 85 | SBUX | Starbucks | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 86 | TPR | Tapestry, Inc. | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 87 | TSCO | Tractor Supply | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 88 | ULTA | Ulta Beauty | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 89 | WSM | Williams-Sonoma, Inc. | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 7 | 90 | YUM | Yum! Brands | Consumer Discretionary | ยังไม่มี | ทำแล้ว |
| 8 | 91 | ADM | Archer Daniels Midland | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 92 | BF.B | Brown–Forman | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 93 | BG | Bunge Global | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 94 | CASY | Casey's | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 95 | CHD | Church & Dwight | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 96 | CL | Colgate-Palmolive | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 97 | CLX | Clorox | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 98 | DG | Dollar General | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 99 | DLTR | Dollar Tree | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 100 | EL | Estée Lauder Companies (The) | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 101 | GIS | General Mills | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 102 | HRL | Hormel Foods | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 103 | HSY | Hershey Company (The) | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 104 | KDP | Keurig Dr Pepper | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 8 | 105 | KHC | Kraft Heinz | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 106 | KMB | Kimberly-Clark | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 107 | KR | Kroger | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 108 | MDLZ | Mondelez International | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 109 | MKC | McCormick & Company | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 110 | MNST | Monster Beverage | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 111 | MO | Altria | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 112 | SJM | J.M. Smucker Company (The) | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 113 | STZ | Constellation Brands | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 114 | SYY | Sysco | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 115 | TGT | Target Corporation | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 116 | TSN | Tyson Foods | Consumer Staples | ยังไม่มี | ทำแล้ว |
| 9 | 117 | VYLR | Vylor | Consumer Staples | ยังไม่มี | ข้าม (ไม่มีเอกสารใน SEC) |
| 9 | 118 | APA | APA Corporation | Energy | ยังไม่มี | ทำแล้ว |
| 9 | 119 | BKR | Baker Hughes | Energy | ยังไม่มี | ทำแล้ว |
| 9 | 120 | DVN | Devon Energy | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 121 | EOG | EOG Resources | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 122 | EQT | EQT Corporation | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 123 | EXE | Expand Energy | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 124 | FANG | Diamondback Energy | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 125 | HAL | Halliburton | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 126 | KMI | Kinder Morgan | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 127 | MPC | Marathon Petroleum | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 128 | OKE | Oneok | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 129 | OXY | Occidental Petroleum | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 130 | PSX | Phillips 66 | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 131 | SLB | Schlumberger | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 132 | TPL | Texas Pacific Land Corporation | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 133 | TRGP | Targa Resources | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 134 | VLO | Valero Energy | Energy | ยังไม่มี | ทำแล้ว |
| 10 | 135 | WMB | Williams Companies | Energy | ยังไม่มี | ทำแล้ว |
| 11 | 136 | ACGL | Arch Capital Group | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 137 | AFL | Aflac | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 138 | AIG | American International Group | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 139 | AIZ | Assurant | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 140 | AJG | Arthur J. Gallagher & Co. | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 141 | ALL | Allstate | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 142 | AMP | Ameriprise Financial | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 143 | AON | Aon plc | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 144 | APO | Apollo Global Management | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 145 | ARES | Ares Management | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 146 | BEN | Franklin Resources | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 147 | BLK | BlackRock | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 148 | BNY | BNY Mellon | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 149 | BRO | Brown & Brown | Financials | ยังไม่มี | ทำแล้ว |
| 11 | 150 | BX | Blackstone Inc. | Financials | ยังไม่มี | ทำแล้ว |
| 12 | 151 | CB | Chubb Limited | Financials | ยังไม่มี | รอ |
| 12 | 152 | CBOE | Cboe Global Markets | Financials | ยังไม่มี | รอ |
| 12 | 153 | CFG | Citizens Financial Group | Financials | ยังไม่มี | รอ |
| 12 | 154 | CINF | Cincinnati Financial | Financials | ยังไม่มี | รอ |
| 12 | 155 | CME | CME Group | Financials | ยังไม่มี | รอ |
| 12 | 156 | COF | Capital One | Financials | ยังไม่มี | รอ |
| 12 | 157 | COIN | Coinbase | Financials | ยังไม่มี | รอ |
| 12 | 158 | CPAY | Corpay | Financials | ยังไม่มี | รอ |
| 12 | 159 | EG | Everest Group | Financials | ยังไม่มี | รอ |
| 12 | 160 | ERIE | Erie Indemnity | Financials | ยังไม่มี | รอ |
| 12 | 161 | FDS | FactSet | Financials | ยังไม่มี | รอ |
| 12 | 162 | FIS | Fidelity National Information Services | Financials | ยังไม่มี | รอ |
| 12 | 163 | FISV | Fiserv | Financials | ยังไม่มี | รอ |
| 12 | 164 | FITB | Fifth Third Bancorp | Financials | ยังไม่มี | รอ |
| 12 | 165 | GL | Globe Life | Financials | ยังไม่มี | รอ |
| 13 | 166 | GPN | Global Payments | Financials | ยังไม่มี | รอ |
| 13 | 167 | HBAN | Huntington Bancshares | Financials | ยังไม่มี | รอ |
| 13 | 168 | HIG | Hartford (The) | Financials | ยังไม่มี | รอ |
| 13 | 169 | HOOD | Robinhood Markets | Financials | ยังไม่มี | รอ |
| 13 | 170 | IBKR | Interactive Brokers | Financials | ยังไม่มี | รอ |
| 13 | 171 | ICE | Intercontinental Exchange | Financials | ยังไม่มี | รอ |
| 13 | 172 | IVZ | Invesco | Financials | ยังไม่มี | รอ |
| 13 | 173 | JKHY | Jack Henry & Associates | Financials | ยังไม่มี | รอ |
| 13 | 174 | KEY | KeyCorp | Financials | ยังไม่มี | รอ |
| 13 | 175 | KKR | KKR & Co. | Financials | ยังไม่มี | รอ |
| 13 | 176 | L | Loews Corporation | Financials | ยังไม่มี | รอ |
| 13 | 177 | MCO | Moody's Corporation | Financials | ยังไม่มี | รอ |
| 13 | 178 | MET | MetLife | Financials | ยังไม่มี | รอ |
| 13 | 179 | MRSH | Marsh McLennan | Financials | ยังไม่มี | รอ |
| 13 | 180 | MSCI | MSCI | Financials | ยังไม่มี | รอ |
| 14 | 181 | MTB | M&T Bank | Financials | ยังไม่มี | รอ |
| 14 | 182 | NDAQ | Nasdaq, Inc. | Financials | ยังไม่มี | รอ |
| 14 | 183 | NTRS | Northern Trust | Financials | ยังไม่มี | รอ |
| 14 | 184 | PFG | Principal Financial Group | Financials | ยังไม่มี | รอ |
| 14 | 185 | PGR | Progressive Corporation | Financials | ยังไม่มี | รอ |
| 14 | 186 | PNC | PNC Financial Services | Financials | ยังไม่มี | รอ |
| 14 | 187 | PRU | Prudential Financial | Financials | ยังไม่มี | รอ |
| 14 | 188 | PYPL | PayPal | Financials | ยังไม่มี | รอ |
| 14 | 189 | RF | Regions Financial Corporation | Financials | ยังไม่มี | รอ |
| 14 | 190 | RJF | Raymond James Financial | Financials | ยังไม่มี | รอ |
| 14 | 191 | SCHW | Charles Schwab Corporation | Financials | ยังไม่มี | รอ |
| 14 | 192 | SPGI | S&P Global | Financials | ยังไม่มี | รอ |
| 14 | 193 | STT | State Street Corporation | Financials | ยังไม่มี | รอ |
| 14 | 194 | SYF | Synchrony Financial | Financials | ยังไม่มี | รอ |
| 14 | 195 | TFC | Truist Financial | Financials | ยังไม่มี | รอ |
| 15 | 196 | TROW | T. Rowe Price | Financials | ยังไม่มี | รอ |
| 15 | 197 | TRV | Travelers Companies (The) | Financials | ยังไม่มี | รอ |
| 15 | 198 | USB | U.S. Bancorp | Financials | ยังไม่มี | รอ |
| 15 | 199 | WRB | W. R. Berkley Corporation | Financials | ยังไม่มี | รอ |
| 15 | 200 | WTW | Willis Towers Watson | Financials | ยังไม่มี | รอ |
| 15 | 201 | XYZ | Block, Inc. | Financials | ยังไม่มี | รอ |
| 15 | 202 | A | Agilent Technologies | Health Care | ยังไม่มี | รอ |
| 15 | 203 | ALGN | Align Technology | Health Care | ยังไม่มี | รอ |
| 15 | 204 | BAX | Baxter International | Health Care | ยังไม่มี | รอ |
| 15 | 205 | BIIB | Biogen | Health Care | ยังไม่มี | รอ |
| 15 | 206 | BMY | Bristol Myers Squibb | Health Care | ยังไม่มี | รอ |
| 15 | 207 | CAH | Cardinal Health | Health Care | ยังไม่มี | รอ |
| 15 | 208 | CI | Cigna | Health Care | ยังไม่มี | รอ |
| 15 | 209 | CNC | Centene Corporation | Health Care | ยังไม่มี | รอ |
| 15 | 210 | COO | Cooper Companies (The) | Health Care | ยังไม่มี | รอ |
| 16 | 211 | COR | Cencora | Health Care | ยังไม่มี | รอ |
| 16 | 212 | CRL | Charles River Laboratories | Health Care | ยังไม่มี | รอ |
| 16 | 213 | CVS | CVS Health | Health Care | ยังไม่มี | รอ |
| 16 | 214 | DGX | Quest Diagnostics | Health Care | ยังไม่มี | รอ |
| 16 | 215 | DHR | Danaher Corporation | Health Care | ยังไม่มี | รอ |
| 16 | 216 | DVA | DaVita | Health Care | ยังไม่มี | รอ |
| 16 | 217 | ELV | Elevance Health | Health Care | ยังไม่มี | รอ |
| 16 | 218 | GEHC | GE HealthCare | Health Care | ยังไม่มี | รอ |
| 16 | 219 | HSIC | Henry Schein | Health Care | ยังไม่มี | รอ |
| 16 | 220 | HUM | Humana | Health Care | ยังไม่มี | รอ |
| 16 | 221 | IDXX | Idexx Laboratories | Health Care | ยังไม่มี | รอ |
| 16 | 222 | ILMN | Illumina, Inc. | Health Care | ยังไม่มี | รอ |
| 16 | 223 | INCY | Incyte | Health Care | ยังไม่มี | รอ |
| 16 | 224 | IQV | IQVIA | Health Care | ยังไม่มี | รอ |
| 16 | 225 | LH | Labcorp | Health Care | ยังไม่มี | รอ |
| 17 | 226 | MCK | McKesson | Health Care | ยังไม่มี | รอ |
| 17 | 227 | MRNA | Moderna | Health Care | ยังไม่มี | รอ |
| 17 | 228 | MTD | Mettler Toledo | Health Care | ยังไม่มี | รอ |
| 17 | 229 | PFE | Pfizer | Health Care | ยังไม่มี | รอ |
| 17 | 230 | REGN | Regeneron Pharmaceuticals | Health Care | ยังไม่มี | รอ |
| 17 | 231 | RMD | ResMed | Health Care | ยังไม่มี | รอ |
| 17 | 232 | RVTY | Revvity | Health Care | ยังไม่มี | รอ |
| 17 | 233 | SOLV | Solventum | Health Care | ยังไม่มี | รอ |
| 17 | 234 | STE | Steris | Health Care | ยังไม่มี | รอ |
| 17 | 235 | TECH | Bio-Techne | Health Care | ยังไม่มี | รอ |
| 17 | 236 | VEEV | Veeva Systems | Health Care | ยังไม่มี | รอ |
| 17 | 237 | VRTX | Vertex Pharmaceuticals | Health Care | ยังไม่มี | รอ |
| 17 | 238 | VTRS | Viatris | Health Care | ยังไม่มี | รอ |
| 17 | 239 | WAT | Waters Corporation | Health Care | ยังไม่มี | รอ |
| 17 | 240 | WST | West Pharmaceutical Services | Health Care | ยังไม่มี | รอ |
| 18 | 241 | ZTS | Zoetis | Health Care | ยังไม่มี | รอ |
| 18 | 242 | ADP | Automatic Data Processing | Industrials | ยังไม่มี | รอ |
| 18 | 243 | ALLE | Allegion | Industrials | ยังไม่มี | รอ |
| 18 | 244 | AME | Ametek | Industrials | ยังไม่มี | รอ |
| 18 | 245 | AOS | A. O. Smith | Industrials | ยังไม่มี | รอ |
| 18 | 246 | AXON | Axon Enterprise | Industrials | ยังไม่มี | รอ |
| 18 | 247 | BR | Broadridge Financial Solutions | Industrials | ยังไม่มี | รอ |
| 18 | 248 | CARR | Carrier Global | Industrials | ยังไม่มี | รอ |
| 18 | 249 | CHRW | C.H. Robinson | Industrials | ยังไม่มี | รอ |
| 18 | 250 | CMI | Cummins | Industrials | ยังไม่มี | รอ |
| 18 | 251 | CPRT | Copart | Industrials | ยังไม่มี | รอ |
| 18 | 252 | CSX | CSX Corporation | Industrials | ยังไม่มี | รอ |
| 18 | 253 | CTAS | Cintas | Industrials | ยังไม่มี | รอ |
| 18 | 254 | DD | DuPont | Industrials | ยังไม่มี | รอ |
| 18 | 255 | DOV | Dover Corporation | Industrials | ยังไม่มี | รอ |
| 19 | 256 | EFX | Equifax | Industrials | ยังไม่มี | รอ |
| 19 | 257 | EME | Emcor | Industrials | ยังไม่มี | รอ |
| 19 | 258 | EMR | Emerson Electric | Industrials | ยังไม่มี | รอ |
| 19 | 259 | EXPD | Expeditors International | Industrials | ยังไม่มี | รอ |
| 19 | 260 | FAST | Fastenal | Industrials | ยังไม่มี | รอ |
| 19 | 261 | FDX | FedEx | Industrials | ยังไม่มี | รอ |
| 19 | 262 | FDXF | FedEx Freight | Industrials | ยังไม่มี | รอ |
| 19 | 263 | FERG | Ferguson Enterprises | Industrials | ยังไม่มี | รอ |
| 19 | 264 | FIX | Comfort Systems USA | Industrials | ยังไม่มี | รอ |
| 19 | 265 | FTV | Fortive | Industrials | ยังไม่มี | รอ |
| 19 | 266 | GD | General Dynamics | Industrials | ยังไม่มี | รอ |
| 19 | 267 | GNRC | Generac | Industrials | ยังไม่มี | รอ |
| 19 | 268 | GWW | W. W. Grainger | Industrials | ยังไม่มี | รอ |
| 19 | 269 | HII | Huntington Ingalls Industries | Industrials | ยังไม่มี | รอ |
| 19 | 270 | HON | Honeywell Technologies | Industrials | ยังไม่มี | รอ |
| 20 | 271 | HONA | Honeywell Aerospace | Industrials | ยังไม่มี | รอ |
| 20 | 272 | HUBB | Hubbell Incorporated | Industrials | ยังไม่มี | รอ |
| 20 | 273 | HWM | Howmet Aerospace | Industrials | ยังไม่มี | รอ |
| 20 | 274 | IEX | IDEX Corporation | Industrials | ยังไม่มี | รอ |
| 20 | 275 | IR | Ingersoll Rand | Industrials | ยังไม่มี | รอ |
| 20 | 276 | ITW | Illinois Tool Works | Industrials | ยังไม่มี | รอ |
| 20 | 277 | J | Jacobs Solutions | Industrials | ยังไม่มี | รอ |
| 20 | 278 | JBHT | J.B. Hunt | Industrials | ยังไม่มี | รอ |
| 20 | 279 | JCI | Johnson Controls | Industrials | ยังไม่มี | รอ |
| 20 | 280 | LDOS | Leidos | Industrials | ยังไม่มี | รอ |
| 20 | 281 | LHX | L3Harris | Industrials | ยังไม่มี | รอ |
| 20 | 282 | LII | Lennox International | Industrials | ยังไม่มี | รอ |
| 20 | 283 | LUV | Southwest Airlines | Industrials | ยังไม่มี | รอ |
| 20 | 284 | MAS | Masco | Industrials | ยังไม่มี | รอ |
| 20 | 285 | MMM | 3M | Industrials | ยังไม่มี | รอ |
| 21 | 286 | NDSN | Nordson Corporation | Industrials | ยังไม่มี | รอ |
| 21 | 287 | NOC | Northrop Grumman | Industrials | ยังไม่มี | รอ |
| 21 | 288 | NSC | Norfolk Southern | Industrials | ยังไม่มี | รอ |
| 21 | 289 | ODFL | Old Dominion | Industrials | ยังไม่มี | รอ |
| 21 | 290 | OTIS | Otis Worldwide | Industrials | ยังไม่มี | รอ |
| 21 | 291 | PAYX | Paychex | Industrials | ยังไม่มี | รอ |
| 21 | 292 | PCAR | Paccar | Industrials | ยังไม่มี | รอ |
| 21 | 293 | PH | Parker Hannifin | Industrials | ยังไม่มี | รอ |
| 21 | 294 | PNR | Pentair | Industrials | ยังไม่มี | รอ |
| 21 | 295 | PWR | Quanta Services | Industrials | ยังไม่มี | รอ |
| 21 | 296 | ROK | Rockwell Automation | Industrials | ยังไม่มี | รอ |
| 21 | 297 | ROL | Rollins, Inc. | Industrials | ยังไม่มี | รอ |
| 21 | 298 | RSG | Republic Services | Industrials | ยังไม่มี | รอ |
| 21 | 299 | SNA | Snap-on | Industrials | ยังไม่มี | รอ |
| 21 | 300 | SWK | Stanley Black & Decker | Industrials | ยังไม่มี | รอ |
| 22 | 301 | TDG | TransDigm Group | Industrials | ยังไม่มี | รอ |
| 22 | 302 | TT | Trane Technologies | Industrials | ยังไม่มี | รอ |
| 22 | 303 | TXT | Textron | Industrials | ยังไม่มี | รอ |
| 22 | 304 | UPS | United Parcel Service | Industrials | ยังไม่มี | รอ |
| 22 | 305 | URI | United Rentals | Industrials | ยังไม่มี | รอ |
| 22 | 306 | VLTO | Veralto | Industrials | ยังไม่มี | รอ |
| 22 | 307 | VRSK | Verisk Analytics | Industrials | ยังไม่มี | รอ |
| 22 | 308 | WAB | Wabtec | Industrials | ยังไม่มี | รอ |
| 22 | 309 | WM | Waste Management | Industrials | ยังไม่มี | รอ |
| 22 | 310 | XYL | Xylem Inc. | Industrials | ยังไม่มี | รอ |
| 22 | 311 | ACN | Accenture | Information Technology | ยังไม่มี | รอ |
| 22 | 312 | ADBE | Adobe Inc. | Information Technology | ยังไม่มี | รอ |
| 22 | 313 | ADI | Analog Devices | Information Technology | ยังไม่มี | รอ |
| 22 | 314 | ADSK | Autodesk | Information Technology | ยังไม่มี | รอ |
| 22 | 315 | AKAM | Akamai Technologies | Information Technology | ยังไม่มี | รอ |
| 23 | 316 | CDNS | Cadence Design Systems | Information Technology | ยังไม่มี | รอ |
| 23 | 317 | CDW | CDW Corporation | Information Technology | ยังไม่มี | รอ |
| 23 | 318 | CTSH | Cognizant | Information Technology | ยังไม่มี | รอ |
| 23 | 319 | DDOG | Datadog | Information Technology | ยังไม่มี | รอ |
| 23 | 320 | FFIV | F5, Inc. | Information Technology | ยังไม่มี | รอ |
| 23 | 321 | FICO | Fair Isaac | Information Technology | ยังไม่มี | รอ |
| 23 | 322 | FLEX | Flex Ltd. | Information Technology | ยังไม่มี | รอ |
| 23 | 323 | FTNT | Fortinet | Information Technology | ยังไม่มี | รอ |
| 23 | 324 | GDDY | GoDaddy | Information Technology | ยังไม่มี | รอ |
| 23 | 325 | GEN | Gen Digital | Information Technology | ยังไม่มี | รอ |
| 23 | 326 | GLW | Corning Inc. | Information Technology | ยังไม่มี | รอ |
| 23 | 327 | HPE | Hewlett Packard Enterprise | Information Technology | ยังไม่มี | รอ |
| 23 | 328 | HPQ | HP Inc. | Information Technology | ยังไม่มี | รอ |
| 23 | 329 | IBM | IBM | Information Technology | ยังไม่มี | รอ |
| 23 | 330 | INTU | Intuit | Information Technology | ยังไม่มี | รอ |
| 24 | 331 | IT | Gartner | Information Technology | ยังไม่มี | รอ |
| 24 | 332 | JBL | Jabil | Information Technology | ยังไม่มี | รอ |
| 24 | 333 | KEYS | Keysight Technologies | Information Technology | ยังไม่มี | รอ |
| 24 | 334 | KLAC | KLA Corporation | Information Technology | ยังไม่มี | รอ |
| 24 | 335 | LITE | Lumentum | Information Technology | ยังไม่มี | รอ |
| 24 | 336 | MCHP | Microchip Technology | Information Technology | ยังไม่มี | รอ |
| 24 | 337 | MPWR | Monolithic Power Systems | Information Technology | ยังไม่มี | รอ |
| 24 | 338 | MSI | Motorola Solutions | Information Technology | ยังไม่มี | รอ |
| 24 | 339 | NOW | ServiceNow | Information Technology | ยังไม่มี | รอ |
| 24 | 340 | NTAP | NetApp | Information Technology | ยังไม่มี | รอ |
| 24 | 341 | NXPI | NXP Semiconductors | Information Technology | ยังไม่มี | รอ |
| 24 | 342 | OKTA | Okta, Inc. | Information Technology | ยังไม่มี | รอ |
| 24 | 343 | ON | ON Semiconductor | Information Technology | ยังไม่มี | รอ |
| 24 | 344 | P | Everpure | Information Technology | ยังไม่มี | รอ |
| 24 | 345 | PLTR | Palantir Technologies | Information Technology | ยังไม่มี | รอ |
| 25 | 346 | PTC | PTC Inc. | Information Technology | ยังไม่มี | รอ |
| 25 | 347 | Q | Qnity Electronics | Information Technology | ยังไม่มี | รอ |
| 25 | 348 | QCOM | Qualcomm | Information Technology | ยังไม่มี | รอ |
| 25 | 349 | ROP | Roper Technologies | Information Technology | ยังไม่มี | รอ |
| 25 | 350 | SNDK | Sandisk | Information Technology | ยังไม่มี | รอ |
| 25 | 351 | SNPS | Synopsys | Information Technology | ยังไม่มี | รอ |
| 25 | 352 | STX | Seagate Technology | Information Technology | ยังไม่มี | รอ |
| 25 | 353 | SWKS | Skyworks Solutions | Information Technology | ยังไม่มี | รอ |
| 25 | 354 | TDY | Teledyne Technologies | Information Technology | ยังไม่มี | รอ |
| 25 | 355 | TEL | TE Connectivity | Information Technology | ยังไม่มี | รอ |
| 25 | 356 | TER | Teradyne | Information Technology | ยังไม่มี | รอ |
| 25 | 357 | TRMB | Trimble Inc. | Information Technology | ยังไม่มี | รอ |
| 25 | 358 | TWLO | Twilio | Information Technology | ยังไม่มี | รอ |
| 25 | 359 | TYL | Tyler Technologies | Information Technology | ยังไม่มี | รอ |
| 25 | 360 | VRSN | Verisign | Information Technology | ยังไม่มี | รอ |
| 26 | 361 | WDAY | Workday, Inc. | Information Technology | ยังไม่มี | รอ |
| 26 | 362 | WDC | Western Digital | Information Technology | ยังไม่มี | รอ |
| 26 | 363 | ZBRA | Zebra Technologies | Information Technology | ยังไม่มี | รอ |
| 26 | 364 | ALB | Albemarle Corporation | Materials | ยังไม่มี | รอ |
| 26 | 365 | AMCR | Amcor | Materials | ยังไม่มี | รอ |
| 26 | 366 | APD | Air Products | Materials | ยังไม่มี | รอ |
| 26 | 367 | AVY | Avery Dennison | Materials | ยังไม่มี | รอ |
| 26 | 368 | BALL | Ball Corporation | Materials | ยังไม่มี | รอ |
| 26 | 369 | CF | CF Industries | Materials | ยังไม่มี | รอ |
| 26 | 370 | CRH | CRH plc | Materials | ยังไม่มี | รอ |
| 26 | 371 | DOW | Dow Inc. | Materials | ยังไม่มี | รอ |
| 26 | 372 | ECL | Ecolab | Materials | ยังไม่มี | รอ |
| 26 | 373 | FCX | Freeport-McMoRan | Materials | ยังไม่มี | รอ |
| 26 | 374 | IFF | International Flavors & Fragrances | Materials | ยังไม่มี | รอ |
| 26 | 375 | IP | International Paper | Materials | ยังไม่มี | รอ |
| 27 | 376 | LYB | LyondellBasell | Materials | ยังไม่มี | รอ |
| 27 | 377 | MLM | Martin Marietta Materials | Materials | ยังไม่มี | รอ |
| 27 | 378 | MOS | Mosaic Company (The) | Materials | ยังไม่มี | รอ |
| 27 | 379 | NEM | Newmont | Materials | ยังไม่มี | รอ |
| 27 | 380 | NUE | Nucor | Materials | ยังไม่มี | รอ |
| 27 | 381 | PKG | Packaging Corporation of America | Materials | ยังไม่มี | รอ |
| 27 | 382 | PPG | PPG Industries | Materials | ยังไม่มี | รอ |
| 27 | 383 | SHW | Sherwin-Williams | Materials | ยังไม่มี | รอ |
| 27 | 384 | STLD | Steel Dynamics | Materials | ยังไม่มี | รอ |
| 27 | 385 | SW | Smurfit Westrock | Materials | ยังไม่มี | รอ |
| 27 | 386 | VMC | Vulcan Materials Company | Materials | ยังไม่มี | รอ |
| 27 | 387 | AMT | American Tower | Real Estate | ยังไม่มี | รอ |
| 27 | 388 | ARE | Alexandria Real Estate Equities | Real Estate | ยังไม่มี | รอ |
| 27 | 389 | BXP | BXP, Inc. | Real Estate | ยังไม่มี | รอ |
| 27 | 390 | CBRE | CBRE Group | Real Estate | ยังไม่มี | รอ |
| 28 | 391 | CCI | Crown Castle | Real Estate | ยังไม่มี | รอ |
| 28 | 392 | CPT | Camden Property Trust | Real Estate | ยังไม่มี | รอ |
| 28 | 393 | CSGP | CoStar Group | Real Estate | ยังไม่มี | รอ |
| 28 | 394 | DOC | Healthpeak Properties | Real Estate | ยังไม่มี | รอ |
| 28 | 395 | ESS | Essex Property Trust | Real Estate | ยังไม่มี | รอ |
| 28 | 396 | EXR | Extra Space Storage | Real Estate | ยังไม่มี | รอ |
| 28 | 397 | FRT | Federal Realty Investment Trust | Real Estate | ยังไม่มี | รอ |
| 28 | 398 | HST | Host Hotels & Resorts | Real Estate | ยังไม่มี | รอ |
| 28 | 399 | INVH | Invitation Homes | Real Estate | ยังไม่มี | รอ |
| 28 | 400 | IRM | Iron Mountain | Real Estate | ยังไม่มี | รอ |
| 28 | 401 | KIM | Kimco Realty | Real Estate | ยังไม่มี | รอ |
| 28 | 402 | MAA | Mid-America Apartment Communities | Real Estate | ยังไม่มี | รอ |
| 28 | 403 | O | Realty Income | Real Estate | ยังไม่มี | รอ |
| 28 | 404 | PLD | Prologis | Real Estate | ยังไม่มี | รอ |
| 28 | 405 | PSA | Public Storage | Real Estate | ยังไม่มี | รอ |
| 29 | 406 | REG | Regency Centers | Real Estate | ยังไม่มี | รอ |
| 29 | 407 | SBAC | SBA Communications | Real Estate | ยังไม่มี | รอ |
| 29 | 408 | SPG | Simon Property Group | Real Estate | ยังไม่มี | รอ |
| 29 | 409 | UDR | UDR, Inc. | Real Estate | ยังไม่มี | รอ |
| 29 | 410 | VICI | Vici Properties | Real Estate | ยังไม่มี | รอ |
| 29 | 411 | VMRK | Vivmark Residential | Real Estate | ยังไม่มี | รอ |
| 29 | 412 | VTR | Ventas | Real Estate | ยังไม่มี | รอ |
| 29 | 413 | WY | Weyerhaeuser | Real Estate | ยังไม่มี | รอ |
| 29 | 414 | AEE | Ameren | Utilities | ยังไม่มี | รอ |
| 29 | 415 | AES | AES Corporation | Utilities | ยังไม่มี | รอ |
| 29 | 416 | ATO | Atmos Energy | Utilities | ยังไม่มี | รอ |
| 29 | 417 | AWK | American Water Works | Utilities | ยังไม่มี | รอ |
| 29 | 418 | CMS | CMS Energy | Utilities | ยังไม่มี | รอ |
| 29 | 419 | CNP | CenterPoint Energy | Utilities | ยังไม่มี | รอ |
| 29 | 420 | DTE | DTE Energy | Utilities | ยังไม่มี | รอ |
| 30 | 421 | ED | Consolidated Edison | Utilities | ยังไม่มี | รอ |
| 30 | 422 | EIX | Edison International | Utilities | ยังไม่มี | รอ |
| 30 | 423 | ES | Eversource Energy | Utilities | ยังไม่มี | รอ |
| 30 | 424 | EVRG | Evergy | Utilities | ยังไม่มี | รอ |
| 30 | 425 | EXC | Exelon | Utilities | ยังไม่มี | รอ |
| 30 | 426 | FE | FirstEnergy | Utilities | ยังไม่มี | รอ |
| 30 | 427 | LNT | Alliant Energy | Utilities | ยังไม่มี | รอ |
| 30 | 428 | NI | NiSource | Utilities | ยังไม่มี | รอ |
| 30 | 429 | PEG | Public Service Enterprise Group | Utilities | ยังไม่มี | รอ |
| 30 | 430 | PNW | Pinnacle West Capital | Utilities | ยังไม่มี | รอ |
| 30 | 431 | PPL | PPL Corporation | Utilities | ยังไม่มี | รอ |
| 30 | 432 | WEC | WEC Energy Group | Utilities | ยังไม่มี | รอ |
| 30 | 433 | ALAB | Astera Labs | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 30 | 434 | ALNY | Alnylam Pharmaceuticals | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 30 | 435 | ARM | Arm Holdings | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 436 | ASML | ASML Holding | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 437 | CCEP | Coca-Cola Europacific Partners | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 438 | CRWV | CoreWeave | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 439 | FER | Ferrovial | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 440 | MELI | Mercado Libre | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 441 | MSTR | MicroStrategy | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 442 | NBIS | Nebius Group | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 443 | PDD | PDD Holdings | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 444 | RKLB | Rocket Lab | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 445 | SHOP | Shopify | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
| 31 | 446 | TRI | Thomson Reuters | Nasdaq-100 ที่ไม่อยู่ใน S&P 500 | ยังไม่มี | รอ |
