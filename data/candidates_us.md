# data/candidates_us.md

> รายชื่อหุ้นสหรัฐที่ยังไม่ได้ทำ จาก S&P 500 รวมกับ Nasdaq-100 ตัดตัวที่อยู่ใน `output/data.json` แล้วออก
>
> - **ใช้เลือกตัวที่จะทำเท่านั้น ไม่ใช่หลักฐาน** แหล่งนี้ไม่อยู่ใน Trust sources ของ `spec.md` (ซึ่งกำหนดไว้สำหรับหลักฐานรายตัว) ตัวเลขและข้อเท็จจริงของหุ้นทุกตัวยังต้องมาจาก SEC EDGAR ตามเดิม
> - ที่มา: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies (503 แถว) และ https://en.wikipedia.org/wiki/List_of_NASDAQ-100_companies (101 แถว) ดึงเมื่อ 2026-11-05 สมาชิกดัชนีเปลี่ยนได้ ควรตรวจกับเว็บไซต์ดัชนีก่อนอ้างว่า "เป็นสมาชิก"
> - หุ้นที่ทำแล้วใน `data.json` ฝั่งสหรัฐ 65 ตัว: 59 ตัวอยู่ในรายชื่อรวมนี้ (ตัดออกแล้ว) อีก 6 ตัวไม่อยู่ในทั้งสองดัชนี: CCJ, CLS, H, LEU, OKLO, TLN
> - เหลือ **456 บริษัท**: S&P 500 441 (นับ FOXA และ NWSA ที่มีสองคลาสหุ้นเป็นบริษัทละ 1) และ Nasdaq-100 ที่ไม่อยู่ใน S&P อีก 15
> - คลาสหุ้นที่สองของบริษัทเดียวกันถูกตัดออกเพื่อไม่ให้ซ้ำ: GOOG (GOOGL ทำแล้ว), FOX และ NWS (เก็บ FOXA กับ NWSA ไว้แทน)

## สรุปตามกลุ่ม GICS

| กลุ่ม | จำนวน |
|---|---|
| Industrials | 77 |
| Financials | 76 |
| Information Technology | 62 |
| Health Care | 47 |
| Consumer Discretionary | 36 |
| Consumer Staples | 33 |
| Real Estate | 28 |
| Materials | 24 |
| Energy | 21 |
| Utilities | 19 |
| Communication Services | 18 |
| นอก S&P 500 (Nasdaq-100 เท่านั้น จัดตาม ICB) | 15 |

## Communication Services (18)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| APP | AppLovin | Advertising | S&P+NDX |
| CHTR | Charter Communications | Cable & Satellite | S&P |
| CMCSA | Comcast | Cable & Satellite | S&P+NDX |
| DIS | Walt Disney Company (The) | Movies & Entertainment | S&P |
| ECHO | EchoStar | Wireless Telecommunication Services | S&P |
| FOXA | Fox Corporation (Class A) | Broadcasting | S&P |
| LYV | Live Nation Entertainment | Movies & Entertainment | S&P |
| META | Meta Platforms | Interactive Media & Services | S&P+NDX |
| NFLX | Netflix | Movies & Entertainment | S&P+NDX |
| NWSA | News Corp (Class A) | Publishing | S&P |
| OMC | Omnicom Group | Advertising | S&P |
| RDDT | Reddit | Interactive Media & Services | S&P |
| SKYD | Skydance | Movies & Entertainment | S&P |
| T | AT&T | Integrated Telecommunication Services | S&P |
| TKO | TKO Group Holdings | Movies & Entertainment | S&P |
| TMUS | T-Mobile US | Wireless Telecommunication Services | S&P+NDX |
| TTWO | Take-Two Interactive | Interactive Home Entertainment | S&P+NDX |
| VZ | Verizon | Integrated Telecommunication Services | S&P |

## Consumer Discretionary (36)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| APTV | Aptiv | Automotive Parts & Equipment | S&P |
| AZO | AutoZone | Automotive Retail | S&P |
| BBY | Best Buy | Computer & Electronics Retail | S&P |
| CMG | Chipotle Mexican Grill | Restaurants | S&P |
| CVNA | Carvana | Automotive Retail | S&P |
| DASH | DoorDash | Specialized Consumer Services | S&P+NDX |
| DECK | Deckers Brands | Footwear | S&P |
| DHI | D. R. Horton | Homebuilding | S&P |
| DPZ | Domino's | Restaurants | S&P |
| DRI | Darden Restaurants | Restaurants | S&P |
| EBAY | eBay Inc. | Broadline Retail | S&P |
| F | Ford Motor Company | Automobile Manufacturers | S&P |
| GM | General Motors | Automobile Manufacturers | S&P |
| GPC | Genuine Parts Company | Distributors | S&P |
| GRMN | Garmin | Consumer Electronics | S&P |
| HAS | Hasbro | Leisure Products | S&P |
| HD | Home Depot (The) | Home Improvement Retail | S&P |
| LEN | Lennar | Homebuilding | S&P |
| LOW | Lowe's | Home Improvement Retail | S&P |
| LULU | Lululemon Athletica | Apparel, Accessories & Luxury Goods | S&P |
| MCD | McDonald's | Restaurants | S&P |
| MGM | MGM Resorts | Casinos & Gaming | S&P |
| NKE | Nike, Inc. | Apparel, Accessories & Luxury Goods | S&P |
| NVR | NVR, Inc. | Homebuilding | S&P |
| ORLY | O'Reilly Automotive | Automotive Retail | S&P+NDX |
| PHM | PulteGroup | Homebuilding | S&P |
| RL | Ralph Lauren Corporation | Apparel, Accessories & Luxury Goods | S&P |
| ROST | Ross Stores | Apparel Retail | S&P+NDX |
| SBUX | Starbucks | Restaurants | S&P+NDX |
| TJX | TJX Companies | Apparel Retail | S&P |
| TPR | Tapestry, Inc. | Apparel, Accessories & Luxury Goods | S&P |
| TSCO | Tractor Supply | Other Specialty Retail | S&P |
| TSLA | Tesla, Inc. | Automobile Manufacturers | S&P+NDX |
| ULTA | Ulta Beauty | Other Specialty Retail | S&P |
| WSM | Williams-Sonoma, Inc. | Homefurnishing Retail | S&P |
| YUM | Yum! Brands | Restaurants | S&P |

## Consumer Staples (33)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| ADM | Archer Daniels Midland | Agricultural Products & Services | S&P |
| BF.B | Brown–Forman | Distillers & Vintners | S&P |
| BG | Bunge Global | Agricultural Products & Services | S&P |
| CASY | Casey's | Food Retail | S&P |
| CHD | Church & Dwight | Household Products | S&P |
| CL | Colgate-Palmolive | Household Products | S&P |
| CLX | Clorox | Household Products | S&P |
| COST | Costco | Consumer Staples Merchandise Retail | S&P+NDX |
| DG | Dollar General | Consumer Staples Merchandise Retail | S&P |
| DLTR | Dollar Tree | Consumer Staples Merchandise Retail | S&P |
| EL | Estée Lauder Companies (The) | Personal Care Products | S&P |
| GIS | General Mills | Packaged Foods & Meats | S&P |
| HRL | Hormel Foods | Packaged Foods & Meats | S&P |
| HSY | Hershey Company (The) | Packaged Foods & Meats | S&P |
| KDP | Keurig Dr Pepper | Soft Drinks & Non-alcoholic Beverages | S&P+NDX |
| KHC | Kraft Heinz | Packaged Foods & Meats | S&P |
| KMB | Kimberly-Clark | Household Products | S&P |
| KO | Coca-Cola Company (The) | Soft Drinks & Non-alcoholic Beverages | S&P |
| KR | Kroger | Food Retail | S&P |
| MDLZ | Mondelez International | Packaged Foods & Meats | S&P+NDX |
| MKC | McCormick & Company | Packaged Foods & Meats | S&P |
| MNST | Monster Beverage | Soft Drinks & Non-alcoholic Beverages | S&P+NDX |
| MO | Altria | Tobacco | S&P |
| PEP | PepsiCo | Soft Drinks & Non-alcoholic Beverages | S&P+NDX |
| PG | Procter & Gamble | Personal Care Products | S&P |
| PM | Philip Morris International | Tobacco | S&P |
| SJM | J.M. Smucker Company (The) | Packaged Foods & Meats | S&P |
| STZ | Constellation Brands | Distillers & Vintners | S&P |
| SYY | Sysco | Food Distributors | S&P |
| TGT | Target Corporation | Consumer Staples Merchandise Retail | S&P |
| TSN | Tyson Foods | Packaged Foods & Meats | S&P |
| VYLR | Vylor | Agricultural Products & Services | S&P |
| WMT | Walmart | Consumer Staples Merchandise Retail | S&P+NDX |

## Energy (21)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| APA | APA Corporation | Oil & Gas Exploration & Production | S&P |
| BKR | Baker Hughes | Oil & Gas Equipment & Services | S&P+NDX |
| COP | ConocoPhillips | Oil & Gas Exploration & Production | S&P |
| CVX | Chevron Corporation | Integrated Oil & Gas | S&P |
| DVN | Devon Energy | Oil & Gas Exploration & Production | S&P |
| EOG | EOG Resources | Oil & Gas Exploration & Production | S&P |
| EQT | EQT Corporation | Oil & Gas Exploration & Production | S&P |
| EXE | Expand Energy | Oil & Gas Exploration & Production | S&P |
| FANG | Diamondback Energy | Oil & Gas Exploration & Production | S&P+NDX |
| HAL | Halliburton | Oil & Gas Equipment & Services | S&P |
| KMI | Kinder Morgan | Oil & Gas Storage & Transportation | S&P |
| MPC | Marathon Petroleum | Oil & Gas Refining & Marketing | S&P |
| OKE | Oneok | Oil & Gas Storage & Transportation | S&P |
| OXY | Occidental Petroleum | Oil & Gas Exploration & Production | S&P |
| PSX | Phillips 66 | Oil & Gas Refining & Marketing | S&P |
| SLB | Schlumberger | Oil & Gas Equipment & Services | S&P |
| TPL | Texas Pacific Land Corporation | Oil & Gas Exploration & Production | S&P |
| TRGP | Targa Resources | Oil & Gas Storage & Transportation | S&P |
| VLO | Valero Energy | Oil & Gas Refining & Marketing | S&P |
| WMB | Williams Companies | Oil & Gas Storage & Transportation | S&P |
| XOM | ExxonMobil | Integrated Oil & Gas | S&P |

## Financials (76)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| ACGL | Arch Capital Group | Property & Casualty Insurance | S&P |
| AFL | Aflac | Life & Health Insurance | S&P |
| AIG | American International Group | Multi-line Insurance | S&P |
| AIZ | Assurant | Multi-line Insurance | S&P |
| AJG | Arthur J. Gallagher & Co. | Insurance Brokers | S&P |
| ALL | Allstate | Property & Casualty Insurance | S&P |
| AMP | Ameriprise Financial | Asset Management & Custody Banks | S&P |
| AON | Aon plc | Insurance Brokers | S&P |
| APO | Apollo Global Management | Asset Management & Custody Banks | S&P |
| ARES | Ares Management | Asset Management & Custody Banks | S&P |
| AXP | American Express | Consumer Finance | S&P |
| BAC | Bank of America | Diversified Banks | S&P |
| BEN | Franklin Resources | Asset Management & Custody Banks | S&P |
| BLK | BlackRock | Asset Management & Custody Banks | S&P |
| BNY | BNY Mellon | Asset Management & Custody Banks | S&P |
| BRK.B | Berkshire Hathaway | Multi-Sector Holdings | S&P |
| BRO | Brown & Brown | Insurance Brokers | S&P |
| BX | Blackstone Inc. | Asset Management & Custody Banks | S&P |
| C | Citigroup | Diversified Banks | S&P |
| CB | Chubb Limited | Property & Casualty Insurance | S&P |
| CBOE | Cboe Global Markets | Financial Exchanges & Data | S&P |
| CFG | Citizens Financial Group | Regional Banks | S&P |
| CINF | Cincinnati Financial | Property & Casualty Insurance | S&P |
| CME | CME Group | Financial Exchanges & Data | S&P |
| COF | Capital One | Consumer Finance | S&P |
| COIN | Coinbase | Financial Exchanges & Data | S&P |
| CPAY | Corpay | Transaction & Payment Processing Services | S&P |
| EG | Everest Group | Reinsurance | S&P |
| ERIE | Erie Indemnity | Insurance Brokers | S&P |
| FDS | FactSet | Financial Exchanges & Data | S&P |
| FIS | Fidelity National Information Services | Transaction & Payment Processing Services | S&P |
| FISV | Fiserv | Transaction & Payment Processing Services | S&P |
| FITB | Fifth Third Bancorp | Regional Banks | S&P |
| GL | Globe Life | Life & Health Insurance | S&P |
| GPN | Global Payments | Transaction & Payment Processing Services | S&P |
| GS | Goldman Sachs | Investment Banking & Brokerage | S&P |
| HBAN | Huntington Bancshares | Regional Banks | S&P |
| HIG | Hartford (The) | Property & Casualty Insurance | S&P |
| HOOD | Robinhood Markets | Investment Banking & Brokerage | S&P |
| IBKR | Interactive Brokers | Investment Banking & Brokerage | S&P |
| ICE | Intercontinental Exchange | Financial Exchanges & Data | S&P |
| IVZ | Invesco | Asset Management & Custody Banks | S&P |
| JKHY | Jack Henry & Associates | Transaction & Payment Processing Services | S&P |
| JPM | JPMorgan Chase | Diversified Banks | S&P |
| KEY | KeyCorp | Regional Banks | S&P |
| KKR | KKR & Co. | Asset Management & Custody Banks | S&P |
| L | Loews Corporation | Multi-line Insurance | S&P |
| MA | Mastercard | Transaction & Payment Processing Services | S&P |
| MCO | Moody's Corporation | Financial Exchanges & Data | S&P |
| MET | MetLife | Life & Health Insurance | S&P |
| MRSH | Marsh McLennan | Insurance Brokers | S&P |
| MS | Morgan Stanley | Investment Banking & Brokerage | S&P |
| MSCI | MSCI | Financial Exchanges & Data | S&P |
| MTB | M&T Bank | Regional Banks | S&P |
| NDAQ | Nasdaq, Inc. | Financial Exchanges & Data | S&P |
| NTRS | Northern Trust | Asset Management & Custody Banks | S&P |
| PFG | Principal Financial Group | Life & Health Insurance | S&P |
| PGR | Progressive Corporation | Property & Casualty Insurance | S&P |
| PNC | PNC Financial Services | Diversified Banks | S&P |
| PRU | Prudential Financial | Life & Health Insurance | S&P |
| PYPL | PayPal | Transaction & Payment Processing Services | S&P+NDX |
| RF | Regions Financial Corporation | Regional Banks | S&P |
| RJF | Raymond James Financial | Investment Banking & Brokerage | S&P |
| SCHW | Charles Schwab Corporation | Investment Banking & Brokerage | S&P |
| SPGI | S&P Global | Financial Exchanges & Data | S&P |
| STT | State Street Corporation | Asset Management & Custody Banks | S&P |
| SYF | Synchrony Financial | Consumer Finance | S&P |
| TFC | Truist Financial | Diversified Banks | S&P |
| TROW | T. Rowe Price | Asset Management & Custody Banks | S&P |
| TRV | Travelers Companies (The) | Property & Casualty Insurance | S&P |
| USB | U.S. Bancorp | Diversified Banks | S&P |
| V | Visa Inc. | Transaction & Payment Processing Services | S&P |
| WFC | Wells Fargo | Diversified Banks | S&P |
| WRB | W. R. Berkley Corporation | Property & Casualty Insurance | S&P |
| WTW | Willis Towers Watson | Insurance Brokers | S&P |
| XYZ | Block, Inc. | Transaction & Payment Processing Services | S&P |

## Health Care (47)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| A | Agilent Technologies | Life Sciences Tools & Services | S&P |
| ABBV | AbbVie | Biotechnology | S&P |
| ALGN | Align Technology | Health Care Supplies | S&P |
| AMGN | Amgen | Biotechnology | S&P+NDX |
| BAX | Baxter International | Health Care Equipment | S&P |
| BIIB | Biogen | Biotechnology | S&P |
| BMY | Bristol Myers Squibb | Pharmaceuticals | S&P |
| CAH | Cardinal Health | Health Care Distributors | S&P |
| CI | Cigna | Health Care Services | S&P |
| CNC | Centene Corporation | Managed Health Care | S&P |
| COO | Cooper Companies (The) | Health Care Supplies | S&P |
| COR | Cencora | Health Care Distributors | S&P |
| CRL | Charles River Laboratories | Life Sciences Tools & Services | S&P |
| CVS | CVS Health | Health Care Services | S&P |
| DGX | Quest Diagnostics | Health Care Services | S&P |
| DHR | Danaher Corporation | Life Sciences Tools & Services | S&P |
| DVA | DaVita | Health Care Services | S&P |
| ELV | Elevance Health | Managed Health Care | S&P |
| GEHC | GE HealthCare | Health Care Equipment | S&P+NDX |
| GILD | Gilead Sciences | Biotechnology | S&P+NDX |
| HSIC | Henry Schein | Health Care Distributors | S&P |
| HUM | Humana | Managed Health Care | S&P |
| IDXX | Idexx Laboratories | Health Care Equipment | S&P+NDX |
| ILMN | Illumina, Inc. | Life Sciences Tools & Services | S&P |
| INCY | Incyte | Biotechnology | S&P |
| IQV | IQVIA | Life Sciences Tools & Services | S&P |
| JNJ | Johnson & Johnson | Pharmaceuticals | S&P |
| LH | Labcorp | Health Care Services | S&P |
| MCK | McKesson | Health Care Distributors | S&P |
| MRK | Merck & Co. | Pharmaceuticals | S&P |
| MRNA | Moderna | Biotechnology | S&P+NDX |
| MTD | Mettler Toledo | Life Sciences Tools & Services | S&P |
| PFE | Pfizer | Pharmaceuticals | S&P |
| REGN | Regeneron Pharmaceuticals | Biotechnology | S&P+NDX |
| RMD | ResMed | Health Care Equipment | S&P |
| RVTY | Revvity | Health Care Equipment | S&P |
| SOLV | Solventum | Health Care Technology | S&P |
| STE | Steris | Health Care Equipment | S&P |
| TECH | Bio-Techne | Life Sciences Tools & Services | S&P |
| TMO | Thermo Fisher Scientific | Life Sciences Tools & Services | S&P |
| UNH | UnitedHealth Group | Managed Health Care | S&P |
| VEEV | Veeva Systems | Health Care Technology | S&P |
| VRTX | Vertex Pharmaceuticals | Biotechnology | S&P+NDX |
| VTRS | Viatris | Pharmaceuticals | S&P |
| WAT | Waters Corporation | Life Sciences Tools & Services | S&P |
| WST | West Pharmaceutical Services | Health Care Supplies | S&P |
| ZTS | Zoetis | Pharmaceuticals | S&P |

## Industrials (77)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| ADP | Automatic Data Processing | Human Resource & Employment Services | S&P+NDX |
| ALLE | Allegion | Building Products | S&P |
| AME | Ametek | Electrical Components & Equipment | S&P |
| AOS | A. O. Smith | Building Products | S&P |
| AXON | Axon Enterprise | Aerospace & Defense | S&P+NDX |
| BA | Boeing | Aerospace & Defense | S&P |
| BR | Broadridge Financial Solutions | Data Processing & Outsourced Services | S&P |
| CARR | Carrier Global | Building Products | S&P |
| CAT | Caterpillar Inc. | Construction Machinery & Heavy Transportation Equipment | S&P |
| CHRW | C.H. Robinson | Air Freight & Logistics | S&P |
| CMI | Cummins | Construction Machinery & Heavy Transportation Equipment | S&P |
| CPRT | Copart | Diversified Support Services | S&P+NDX |
| CSX | CSX Corporation | Rail Transportation | S&P+NDX |
| CTAS | Cintas | Diversified Support Services | S&P+NDX |
| DD | DuPont | Industrial Conglomerates | S&P |
| DE | Deere & Company | Agricultural & Farm Machinery | S&P |
| DOV | Dover Corporation | Industrial Machinery & Supplies & Components | S&P |
| EFX | Equifax | Research & Consulting Services | S&P |
| EME | Emcor | Construction & Engineering | S&P |
| EMR | Emerson Electric | Electrical Components & Equipment | S&P |
| EXPD | Expeditors International | Air Freight & Logistics | S&P |
| FAST | Fastenal | Trading Companies & Distributors | S&P+NDX |
| FDX | FedEx | Air Freight & Logistics | S&P |
| FDXF | FedEx Freight | Cargo Ground Transportation | S&P |
| FERG | Ferguson Enterprises | Trading Companies & Distributors | S&P |
| FIX | Comfort Systems USA | Construction & Engineering | S&P |
| FTV | Fortive | Industrial Machinery & Supplies & Components | S&P |
| GD | General Dynamics | Aerospace & Defense | S&P |
| GE | GE Aerospace | Aerospace & Defense | S&P |
| GNRC | Generac | Heavy Electrical Equipment | S&P |
| GWW | W. W. Grainger | Industrial Machinery & Supplies & Components | S&P |
| HII | Huntington Ingalls Industries | Aerospace & Defense | S&P |
| HON | Honeywell Technologies | Industrial Conglomerates | S&P+NDX |
| HONA | Honeywell Aerospace | Aerospace & Defense | S&P+NDX |
| HUBB | Hubbell Incorporated | Industrial Machinery & Supplies & Components | S&P |
| HWM | Howmet Aerospace | Aerospace & Defense | S&P |
| IEX | IDEX Corporation | Industrial Machinery & Supplies & Components | S&P |
| IR | Ingersoll Rand | Industrial Machinery & Supplies & Components | S&P |
| ITW | Illinois Tool Works | Industrial Machinery & Supplies & Components | S&P |
| J | Jacobs Solutions | Construction & Engineering | S&P |
| JBHT | J.B. Hunt | Cargo Ground Transportation | S&P |
| JCI | Johnson Controls | Building Products | S&P |
| LDOS | Leidos | Diversified Support Services | S&P |
| LHX | L3Harris | Aerospace & Defense | S&P |
| LII | Lennox International | Building Products | S&P |
| LMT | Lockheed Martin | Aerospace & Defense | S&P |
| LUV | Southwest Airlines | Passenger Airlines | S&P |
| MAS | Masco | Building Products | S&P |
| MMM | 3M | Industrial Conglomerates | S&P |
| NDSN | Nordson Corporation | Industrial Machinery & Supplies & Components | S&P |
| NOC | Northrop Grumman | Aerospace & Defense | S&P |
| NSC | Norfolk Southern | Rail Transportation | S&P |
| ODFL | Old Dominion | Cargo Ground Transportation | S&P+NDX |
| OTIS | Otis Worldwide | Industrial Machinery & Supplies & Components | S&P |
| PAYX | Paychex | Human Resource & Employment Services | S&P+NDX |
| PCAR | Paccar | Construction Machinery & Heavy Transportation Equipment | S&P+NDX |
| PH | Parker Hannifin | Industrial Machinery & Supplies & Components | S&P |
| PNR | Pentair | Industrial Machinery & Supplies & Components | S&P |
| PWR | Quanta Services | Construction & Engineering | S&P |
| ROK | Rockwell Automation | Electrical Components & Equipment | S&P |
| ROL | Rollins, Inc. | Environmental & Facilities Services | S&P |
| RSG | Republic Services | Environmental & Facilities Services | S&P |
| RTX | RTX Corporation | Aerospace & Defense | S&P |
| SNA | Snap-on | Industrial Machinery & Supplies & Components | S&P |
| SWK | Stanley Black & Decker | Industrial Machinery & Supplies & Components | S&P |
| TDG | TransDigm Group | Aerospace & Defense | S&P |
| TT | Trane Technologies | Building Products | S&P |
| TXT | Textron | Aerospace & Defense | S&P |
| UBER | Uber | Passenger Ground Transportation | S&P |
| UNP | Union Pacific Corporation | Rail Transportation | S&P |
| UPS | United Parcel Service | Air Freight & Logistics | S&P |
| URI | United Rentals | Trading Companies & Distributors | S&P |
| VLTO | Veralto | Environmental & Facilities Services | S&P |
| VRSK | Verisk Analytics | Research & Consulting Services | S&P |
| WAB | Wabtec | Construction Machinery & Heavy Transportation Equipment | S&P |
| WM | Waste Management | Environmental & Facilities Services | S&P |
| XYL | Xylem Inc. | Industrial Machinery & Supplies & Components | S&P |

## Information Technology (62)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| AAPL | Apple Inc. | Technology Hardware, Storage & Peripherals | S&P+NDX |
| ACN | Accenture | IT Consulting & Other Services | S&P |
| ADBE | Adobe Inc. | Application Software | S&P+NDX |
| ADI | Analog Devices | Semiconductors | S&P+NDX |
| ADSK | Autodesk | Application Software | S&P+NDX |
| AKAM | Akamai Technologies | Internet Services & Infrastructure | S&P |
| AMAT | Applied Materials | Semiconductor Materials & Equipment | S&P+NDX |
| CDNS | Cadence Design Systems | Application Software | S&P+NDX |
| CDW | CDW Corporation | Technology Distributors | S&P |
| CRM | Salesforce | Application Software | S&P |
| CRWD | CrowdStrike | Systems Software | S&P+NDX |
| CSCO | Cisco | Communications Equipment | S&P+NDX |
| CTSH | Cognizant | IT Consulting & Other Services | S&P |
| DDOG | Datadog | Application Software | S&P+NDX |
| FFIV | F5, Inc. | Communications Equipment | S&P |
| FICO | Fair Isaac | Application Software | S&P |
| FLEX | Flex Ltd. | Electronic Manufacturing Services | S&P |
| FTNT | Fortinet | Systems Software | S&P+NDX |
| GDDY | GoDaddy | Internet Services & Infrastructure | S&P |
| GEN | Gen Digital | Systems Software | S&P |
| GLW | Corning Inc. | Electronic Components | S&P |
| HPE | Hewlett Packard Enterprise | Technology Hardware, Storage & Peripherals | S&P |
| HPQ | HP Inc. | Technology Hardware, Storage & Peripherals | S&P |
| IBM | IBM | IT Consulting & Other Services | S&P |
| INTC | Intel | Semiconductors | S&P+NDX |
| INTU | Intuit | Application Software | S&P+NDX |
| IT | Gartner | IT Consulting & Other Services | S&P |
| JBL | Jabil | Electronic Manufacturing Services | S&P |
| KEYS | Keysight Technologies | Electronic Equipment & Instruments | S&P |
| KLAC | KLA Corporation | Semiconductor Materials & Equipment | S&P+NDX |
| LITE | Lumentum | Communications Equipment | S&P+NDX |
| LRCX | Lam Research | Semiconductor Materials & Equipment | S&P+NDX |
| MCHP | Microchip Technology | Semiconductors | S&P+NDX |
| MPWR | Monolithic Power Systems | Semiconductors | S&P+NDX |
| MSI | Motorola Solutions | Communications Equipment | S&P |
| NOW | ServiceNow | Systems Software | S&P |
| NTAP | NetApp | Technology Hardware, Storage & Peripherals | S&P |
| NXPI | NXP Semiconductors | Semiconductors | S&P+NDX |
| OKTA | Okta, Inc. | Application Software | S&P |
| ON | ON Semiconductor | Semiconductors | S&P |
| P | Everpure | Technology Hardware, Storage & Peripherals | S&P |
| PANW | Palo Alto Networks | Systems Software | S&P+NDX |
| PLTR | Palantir Technologies | Application Software | S&P+NDX |
| PTC | PTC Inc. | Application Software | S&P |
| Q | Qnity Electronics | Semiconductor Materials & Equipment | S&P |
| QCOM | Qualcomm | Semiconductors | S&P+NDX |
| ROP | Roper Technologies | Electronic Equipment & Instruments | S&P+NDX |
| SNDK | Sandisk | Technology Hardware, Storage & Peripherals | S&P+NDX |
| SNPS | Synopsys | Application Software | S&P+NDX |
| STX | Seagate Technology | Technology Hardware, Storage & Peripherals | S&P+NDX |
| SWKS | Skyworks Solutions | Semiconductors | S&P |
| TDY | Teledyne Technologies | Electronic Equipment & Instruments | S&P |
| TEL | TE Connectivity | Electronic Manufacturing Services | S&P |
| TER | Teradyne | Semiconductor Materials & Equipment | S&P+NDX |
| TRMB | Trimble Inc. | Application Software | S&P |
| TWLO | Twilio | Systems Software | S&P |
| TXN | Texas Instruments | Semiconductors | S&P+NDX |
| TYL | Tyler Technologies | Application Software | S&P |
| VRSN | Verisign | Internet Services & Infrastructure | S&P |
| WDAY | Workday, Inc. | Application Software | S&P+NDX |
| WDC | Western Digital | Technology Hardware, Storage & Peripherals | S&P+NDX |
| ZBRA | Zebra Technologies | Electronic Equipment & Instruments | S&P |

## Materials (24)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| ALB | Albemarle Corporation | Specialty Chemicals | S&P |
| AMCR | Amcor | Paper & Plastic Packaging Products & Materials | S&P |
| APD | Air Products | Industrial Gases | S&P |
| AVY | Avery Dennison | Paper & Plastic Packaging Products & Materials | S&P |
| BALL | Ball Corporation | Metal, Glass & Plastic Containers | S&P |
| CF | CF Industries | Fertilizers & Agricultural Chemicals | S&P |
| CRH | CRH plc | Construction Materials | S&P |
| DOW | Dow Inc. | Commodity Chemicals | S&P |
| ECL | Ecolab | Specialty Chemicals | S&P |
| FCX | Freeport-McMoRan | Copper | S&P |
| IFF | International Flavors & Fragrances | Specialty Chemicals | S&P |
| IP | International Paper | Paper & Plastic Packaging Products & Materials | S&P |
| LIN | Linde plc | Industrial Gases | S&P+NDX |
| LYB | LyondellBasell | Specialty Chemicals | S&P |
| MLM | Martin Marietta Materials | Construction Materials | S&P |
| MOS | Mosaic Company (The) | Fertilizers & Agricultural Chemicals | S&P |
| NEM | Newmont | Gold | S&P |
| NUE | Nucor | Steel | S&P |
| PKG | Packaging Corporation of America | Paper & Plastic Packaging Products & Materials | S&P |
| PPG | PPG Industries | Specialty Chemicals | S&P |
| SHW | Sherwin-Williams | Specialty Chemicals | S&P |
| STLD | Steel Dynamics | Steel | S&P |
| SW | Smurfit Westrock | Paper & Plastic Packaging Products & Materials | S&P |
| VMC | Vulcan Materials Company | Construction Materials | S&P |

## Real Estate (28)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| AMT | American Tower | Telecom Tower REITs | S&P |
| ARE | Alexandria Real Estate Equities | Office REITs | S&P |
| BXP | BXP, Inc. | Office REITs | S&P |
| CBRE | CBRE Group | Real Estate Services | S&P |
| CCI | Crown Castle | Telecom Tower REITs | S&P |
| CPT | Camden Property Trust | Multi-Family Residential REITs | S&P |
| CSGP | CoStar Group | Real Estate Services | S&P |
| DOC | Healthpeak Properties | Health Care REITs | S&P |
| ESS | Essex Property Trust | Multi-Family Residential REITs | S&P |
| EXR | Extra Space Storage | Self-Storage REITs | S&P |
| FRT | Federal Realty Investment Trust | Retail REITs | S&P |
| HST | Host Hotels & Resorts | Hotel & Resort REITs | S&P |
| INVH | Invitation Homes | Single-Family Residential REITs | S&P |
| IRM | Iron Mountain | Other Specialized REITs | S&P |
| KIM | Kimco Realty | Retail REITs | S&P |
| MAA | Mid-America Apartment Communities | Multi-Family Residential REITs | S&P |
| O | Realty Income | Retail REITs | S&P |
| PLD | Prologis | Industrial REITs | S&P |
| PSA | Public Storage | Self-Storage REITs | S&P |
| REG | Regency Centers | Retail REITs | S&P |
| SBAC | SBA Communications | Telecom Tower REITs | S&P |
| SPG | Simon Property Group | Retail REITs | S&P |
| UDR | UDR, Inc. | Multi-Family Residential REITs | S&P |
| VICI | Vici Properties | Hotel & Resort REITs | S&P |
| VMRK | Vivmark Residential | Multi-Family Residential REITs | S&P |
| VTR | Ventas | Health Care REITs | S&P |
| WELL | Welltower | Health Care REITs | S&P |
| WY | Weyerhaeuser | Timber REITs | S&P |

## Utilities (19)

| ticker | บริษัท | กลุ่มย่อย | ดัชนี |
|---|---|---|---|
| AEE | Ameren | Multi-Utilities | S&P |
| AES | AES Corporation | Independent Power Producers & Energy Traders | S&P |
| ATO | Atmos Energy | Gas Utilities | S&P |
| AWK | American Water Works | Water Utilities | S&P |
| CMS | CMS Energy | Multi-Utilities | S&P |
| CNP | CenterPoint Energy | Multi-Utilities | S&P |
| DTE | DTE Energy | Multi-Utilities | S&P |
| ED | Consolidated Edison | Multi-Utilities | S&P |
| EIX | Edison International | Electric Utilities | S&P |
| ES | Eversource Energy | Electric Utilities | S&P |
| EVRG | Evergy | Electric Utilities | S&P |
| EXC | Exelon | Electric Utilities | S&P+NDX |
| FE | FirstEnergy | Electric Utilities | S&P |
| LNT | Alliant Energy | Electric Utilities | S&P |
| NI | NiSource | Multi-Utilities | S&P |
| PEG | Public Service Enterprise Group | Electric Utilities | S&P |
| PNW | Pinnacle West Capital | Multi-Utilities | S&P |
| PPL | PPL Corporation | Electric Utilities | S&P |
| WEC | WEC Energy Group | Electric Utilities | S&P |

## Nasdaq-100 ที่ไม่อยู่ใน S&P 500 (15)

จัดกลุ่มตาม ICB ของ Nasdaq ไม่ตรงกับ GICS บางตัวเป็นบริษัทต่างชาติที่ยื่น 20-F / 40-F แทน 10-K ต้องตรวจก่อนว่า `fetch_us.py` ดึงได้ครบหรือไม่ (ตัวที่ผมไม่รู้จักชื่อ ticker ให้ตรวจชื่อบริษัทก่อน เช่น SPCX)

| ticker | บริษัท | ICB |
|---|---|---|
| ALAB | Astera Labs | Technology / Semiconductors |
| ALNY | Alnylam Pharmaceuticals | Health Care / Biotechnology |
| ARM | Arm Holdings | Technology / Semiconductors |
| ASML | ASML Holding | Technology / Industrial Machinery |
| CCEP | Coca-Cola Europacific Partners | Consumer Staples / Soft Drinks |
| CRWV | CoreWeave | Technology / Computer Services |
| FER | Ferrovial | Industrials / Military, Government, Technical |
| MELI | Mercado Libre | Consumer Discretionary / Catalog/Specialty Distribution |
| MSTR | MicroStrategy | Technology / Software |
| NBIS | Nebius Group | Technology / Computer Services |
| PDD | PDD Holdings | Technology / EDP Services |
| RKLB | Rocket Lab | Industrials / Aerospace |
| SHOP | Shopify | Technology / Software |
| SPCX | SpaceX | Telecommunications / Telecommunications Services |
| TRI | Thomson Reuters | Technology / Software |
