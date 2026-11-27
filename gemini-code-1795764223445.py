import os
import shutil
import zipfile

# Create project structure
base_dir = "/tmp/honey_landing_page"
os.makedirs(os.path.join(base_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "google_apps_script"), exist_ok=True)

# Copy uploaded images to images folder with clean names
img1_src = "811b84fcd8b20d9fa9629c1fcda9b280.png_720x720q80.jpg"
img2_src = "_c156c26899.webp"

if os.path.exists(img1_src):
    shutil.copy(img1_src, os.path.join(base_dir, "images", "vejpong_honey.jpg"))
if os.path.exists(img2_src):
    shutil.copy(img2_src, os.path.join(base_dir, "images", "doikham_honey.webp"))

# Shared CSS & JS for the 5-page website + Google Sheet API integration
style_css = """@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');

:root {
  --primary: #d97706;
  --primary-dark: #b45309;
  --primary-light: #fef3c7;
  --secondary: #1e293b;
  --bg: #fffbeb;
  --white: #ffffff;
  --text: #334155;
  --border: #fde68a;
  --shadow: 0 10px 25px -5px rgba(217, 119, 6, 0.12), 0 8px 10px -6px rgba(217, 119, 6, 0.08);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Prompt', sans-serif;
}

body {
  background-color: var(--bg);
  color: var(--text);
  line-height: 1.6;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Navbar */
nav {
  background: var(--white);
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-dark);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-links {
  display: flex;
  gap: 1.25rem;
  list-style: none;
  flex-wrap: wrap;
}

.nav-links a {
  text-decoration: none;
  color: var(--secondary);
  font-weight: 500;
  padding: 0.4rem 0.8rem;
  border-radius: 8px;
  transition: all 0.2s;
}

.nav-links a:hover, .nav-links a.active {
  background: var(--primary-light);
  color: var(--primary-dark);
}

/* Main Container */
main {
  flex: 1;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

/* Hero Section */
.hero {
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
  border-radius: 24px;
  padding: 3.5rem 2.5rem;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 2rem;
  align-items: center;
  box-shadow: var(--shadow);
  margin-bottom: 3rem;
}

.hero h1 {
  font-size: 2.6rem;
  color: var(--secondary);
  line-height: 1.25;
  margin-bottom: 1rem;
}

.hero h1 span {
  color: var(--primary-dark);
}

.hero p {
  font-size: 1.1rem;
  margin-bottom: 1.75rem;
  color: #475569;
}

.hero-imgs {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.hero-imgs img {
  width: 48%;
  max-height: 300px;
  object-fit: contain;
  background: var(--white);
  padding: 1rem;
  border-radius: 16px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}

/* Buttons */
.btn {
  display: inline-block;
  background: var(--primary);
  color: var(--white);
  padding: 0.75rem 1.75rem;
  border-radius: 12px;
  text-decoration: none;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: background 0.2s, transform 0.1s;
  font-size: 1rem;
}

.btn:hover {
  background: var(--primary-dark);
  transform: translateY(-2px);
}

.btn-outline {
  background: var(--white);
  color: var(--primary-dark);
  border: 2px solid var(--primary);
}

.btn-outline:hover {
  background: var(--primary-light);
}

.btn-sm {
  padding: 0.4rem 0.9rem;
  font-size: 0.875rem;
  border-radius: 8px;
}

/* Product Grid */
.section-title {
  text-align: center;
  font-size: 2rem;
  color: var(--secondary);
  margin-bottom: 0.5rem;
}

.section-sub {
  text-align: center;
  color: #64748b;
  margin-bottom: 2.5rem;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.card {
  background: var(--white);
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.2s;
}

.card:hover {
  transform: translateY(-4px);
}

.card-img {
  width: 100%;
  height: 240px;
  object-fit: contain;
  background: #fafafa;
  border-radius: 12px;
  margin-bottom: 1rem;
  padding: 0.75rem;
}

.badge {
  display: inline-block;
  background: var(--primary-light);
  color: var(--primary-dark);
  font-size: 0.8rem;
  font-weight: 600;
  padding: 0.25rem 0.75rem;
  border-radius: 999px;
  margin-bottom: 0.5rem;
  width: fit-content;
}

.card h3 {
  font-size: 1.25rem;
  color: var(--secondary);
  margin-bottom: 0.5rem;
}

.card p {
  font-size: 0.95rem;
  color: #64748b;
  margin-bottom: 1rem;
}

.price-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px solid #f1f5f9;
}

.price {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--primary-dark);
}

/* Forms & Tables */
.box {
  background: var(--white);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  max-width: 750px;
  margin: 0 auto;
}

.box-wide {
  max-width: 1100px;
}

.form-group {
  margin-bottom: 1.25rem;
}

label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.4rem;
  color: var(--secondary);
}

input, select, textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1.5px solid #cbd5e1;
  border-radius: 10px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.2s;
}

input:focus, select:focus, textarea:focus {
  border-color: var(--primary);
}

.table-wrap {
  overflow-x: auto;
  margin-top: 1.5rem;
}

table {
  width: 100%;
  border-collapse: collapse;
  background: var(--white);
}

th, td {
  padding: 0.9rem 1rem;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
  font-size: 0.95rem;
}

th {
  background: var(--primary-light);
  color: var(--primary-dark);
  font-weight: 600;
}

.status-pill {
  padding: 0.25rem 0.65rem;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 600;
}

.status-pending { background: #fef3c7; color: #b45309; }
.status-paid { background: #dcfce7; color: #15803d; }
.status-shipped { background: #dbeafe; color: #1d4ed8; }

.alert {
  padding: 1rem;
  border-radius: 12px;
  background: #fef3c7;
  border: 1px solid #f59e0b;
  color: #92400e;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
}

footer {
  background: var(--secondary);
  color: #cbd5e1;
  text-align: center;
  padding: 1.5rem;
  margin-top: 4rem;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .hero { grid-template-columns: 1fr; text-align: center; }
  .hero h1 { font-size: 2rem; }
}
"""

with open(os.path.join(base_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(style_css)

# Shared JS (app.js) with 4 SKUs using the separated images/ folder + Google Apps Script Web App connection
app_js = """// ==========================================
// ตั้งค่า URL ของ Google Apps Script Web App
// วาง Web App URL ที่ได้จากการ Deploy Google Sheet ที่นี่
// ==========================================
const GOOGLE_SCRIPT_URL = localStorage.getItem('HONEY_GAS_URL') || "";

// ข้อมูลสินค้าน้ำผึ้ง 4 SKUs (ดึงรูปภาพจากโฟลเดอร์ images/ แยกต่างหาก)
const PRODUCTS = [
  {
    sku: "HNY-VP-001",
    name: "น้ำผึ้งเวชพงศ์ น้ำผึ้งสดแท้จากธรรมชาติ (แพ็คคู่สุดคุ้ม)",
    brand: "เวชพงศ์ (Vejpong)",
    weight: "700 กรัม x 2 ขวด",
    price: 490,
    image: "images/vejpong_honey.jpg",
    desc: "น้ำผึ้งแท้ 100% คัดสรรจากธรรมชาติ รสชาติหอมหวานละมุน บรรจุขวดบีบใช้งานสะดวก แพ็คคู่สุดคุ้มค่า"
  },
  {
    sku: "HNY-DK-002",
    name: "น้ำผึ้งเกสรดอกลำไย ตราดอยคำ (ขวดใหญ่)",
    brand: "ดอยคำ (Doi Kham)",
    weight: "770 กรัม",
    price: 265,
    image: "images/doikham_honey.webp",
    desc: "น้ำผึ้งแท้ 100% จากเกสรดอกลำไยธรรมชาติ ไม่แต่งกลิ่น ไม่เจือสี กลิ่นหอมเป็นเอกลักษณ์ เหมาะสำหรับชงเครื่องดื่มและทำเบเกอรี่"
  },
  {
    sku: "HNY-DK-003",
    name: "น้ำผึ้งเกสรดอกลำไย ตราดอยคำ (แบบหลอดบีบ)",
    brand: "ดอยคำ (Doi Kham)",
    weight: "120 กรัม",
    price: 65,
    image: "images/doikham_honey.webp",
    desc: "ขนาดพกพาสะดวก ฝาเปิด-ปิดง่าย ไม่หกเลอะเทอะ เหมาะสำหรับราดแพนเค้ก ขนมปัง หรือพกพาไปทำงาน"
  },
  {
    sku: "HNY-DK-004",
    name: "น้ำผึ้งเกสรดอกลำไย ตราดอยคำ (ขวดโหลแก้วพรีเมียม)",
    brand: "ดอยคำ (Doi Kham)",
    weight: "230 กรัม",
    price: 115,
    image: "images/doikham_honey.webp",
    desc: "บรรจุในขวดโหลแก้วคุณภาพดี รักษาความหอมสดใหม่ของน้ำผึ้งเกสรดอกลำไย 100% เหมาะสำหรับเป็นของฝากหรือใช้ในครัวเรือน"
  }
];

// บันทึกคำสั่งซื้อ (ส่งเข้า Google Sheet หากตั้งค่า URL แล้ว และสำรองไว้ใน LocalStorage)
async function submitOrderToSheet(orderData) {
  // เก็บสำรองใน LocalStorage เพื่อให้หน้าขอบคุณและหน้าแอดมินแสดงผลได้ทันทีแม้ยังไม่ต่อ API
  const localOrders = JSON.parse(localStorage.getItem('HONEY_ORDERS') || "[]");
  localOrders.unshift(orderData);
  localStorage.setItem('HONEY_ORDERS', JSON.stringify(localOrders));
  localStorage.setItem('LAST_ORDER', JSON.stringify(orderData));

  const gasUrl = localStorage.getItem('HONEY_GAS_URL') || GOOGLE_SCRIPT_URL;
  if (gasUrl) {
    try {
      await fetch(gasUrl, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "createOrder", ...orderData })
      });
    } catch (err) {
      console.error("Google Sheet Sync Error:", err);
    }
  }
  return true;
}

// ดึงข้อมูลคำสั่งซื้อทั้งหมด (จาก Google Sheet ถ้ามี URL หรือจาก LocalStorage)
async function fetchAllOrders() {
  const gasUrl = localStorage.getItem('HONEY_GAS_URL') || GOOGLE_SCRIPT_URL;
  if (gasUrl) {
    try {
      const res = await fetch(`${gasUrl}?action=getOrders`);
      const json = await res.json();
      if (json && Array.isArray(json.orders)) {
        return json.orders;
      }
    } catch (err) {
      console.warn("ไม่สามารถดึงข้อมูลจาก Google Sheet ได้ ใช้ข้อมูลสำรองในเครื่องแทน:", err);
    }
  }
  return JSON.parse(localStorage.getItem('HONEY_ORDERS') || "[]");
}

// อัปเดตสถานะคำสั่งซื้อ
async function updateOrderStatus(orderId, newStatus) {
  const localOrders = JSON.parse(localStorage.getItem('HONEY_ORDERS') || "[]");
  const idx = localOrders.findIndex(o => o.orderId === orderId);
  if (idx !== -1) {
    localOrders[idx].status = newStatus;
    localStorage.setItem('HONEY_ORDERS', JSON.stringify(localOrders));
  }

  const gasUrl = localStorage.getItem('HONEY_GAS_URL') || GOOGLE_SCRIPT_URL;
  if (gasUrl) {
    try {
      await fetch(gasUrl, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "updateStatus", orderId, status: newStatus })
      });
    } catch (err) {
      console.error("Update status failed:", err);
    }
  }
}
"""

with open(os.path.join(base_dir, "app.js"), "w", encoding="utf-8") as f:
    f.write(app_js)

# Shared Navbar HTML snippet
def get_navbar(active_page):
    pages = [
        ("index.html", "หน้าแรก"),
        ("products.html", "หน้าสินค้า"),
        ("order.html", "หน้าสั่งซื้อ"),
        ("admin.html", "หน้าแอดมิน"),
        ("thankyou.html", "หน้าขอบคุณ")
    ]
    links_html = ""
    for href, label in pages:
        cls = ' class="active"' if href == active_page else ''
        links_html += f'        <li><a href="{href}"{cls}>{label}</a></li>\n'
    return f"""  <nav>
    <div class="nav-container">
      <a href="index.html" class="logo">🍯 GoldenBee Honey Store</a>
      <ul class="nav-links">
{links_html}      </ul>
    </div>
  </nav>"""

# 1. หน้าแรก (index.html)
index_html = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>หน้าแรก | GoldenBee ร้านน้ำผึ้งแท้ 100% จากธรรมชาติ</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
{get_navbar("index.html")}

  <main>
    <section class="hero">
      <div>
        <span class="badge">🐝 น้ำผึ้งแท้ 100% คัดสรรคุณภาพ</span>
        <h1>ความหวานบริสุทธิ์จากธรรมชาติ <span>เพื่อสุขภาพที่ดีทุกวัน</span></h1>
        <p>รวมน้ำผึ้งแท้เกรดพรีเมียม ทั้งน้ำผึ้งสดแท้จากธรรมชาติเวชพงศ์ และน้ำผึ้งเกสรดอกลำไยตราดอยคำ ไม่แต่งกลิ่น ไม่เจือสี พร้อมจัดส่งตรงถึงหน้าบ้านคุณ</p>
        <div style="display:flex; gap:1rem; flex-wrap:wrap;">
          <a href="order.html" class="btn">สั่งซื้อน้ำผึ้งทันที</a>
          <a href="products.html" class="btn btn-outline">ดูสินค้าทั้งหมด (4 SKUs)</a>
        </div>
      </div>
      <div class="hero-imgs">
        <img src="images/vejpong_honey.jpg" alt="น้ำผึ้งเวชพงศ์" />
        <img src="images/doikham_honey.webp" alt="น้ำผึ้งดอยคำ" />
      </div>
    </section>

    <h2 class="section-title">สินค้าแนะนำขายดี</h2>
    <p class="section-sub">เลือกขนาดและแบรนด์น้ำผึ้งแท้ที่เหมาะกับความต้องการของคุณ</p>

    <div class="product-grid" id="featured-products"></div>
  </main>

  <footer>
    <p>© 2026 GoldenBee Honey Store | ระบบจัดเก็บข้อมูลการขายด้วย Google Sheets</p>
  </footer>

  <script src="app.js"></script>
  <script>
    const container = document.getElementById('featured-products');
    PRODUCTS.slice(0, 2).forEach(p => {{
      container.innerHTML += `
        <div class="card">
          <img src="${{p.image}}" alt="${{p.name}}" class="card-img" />
          <span class="badge">${{p.brand}} | SKU: ${{p.sku}}</span>
          <h3>${{p.name}}</h3>
          <p>${{p.desc}}</p>
          <div class="price-row">
            <span class="price">฿${{p.price.toLocaleString()}}</span>
            <a href="order.html?sku=${{p.sku}}" class="btn btn-sm">สั่งซื้อสินค้านี้</a>
          </div>
        </div>
      `;
    }});
  </script>
</body>
</html>
"""

# 2. หน้าสินค้า (products.html)
products_html = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>หน้าสินค้า | GoldenBee ร้านน้ำผึ้งแท้ 100%</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
{get_navbar("products.html")}

  <main>
    <h1 class="section-title">รายการสินค้าน้ำผึ้งแท้ทั้งหมด (4 SKUs)</h1>
    <p class="section-sub">รับประกันน้ำผึ้งแท้ 100% ทุกขวด คัดสรรจากแหล่งผลิตที่ได้มาตรฐาน</p>

    <div class="product-grid" id="all-products"></div>
  </main>

  <footer>
    <p>© 2026 GoldenBee Honey Store | ระบบจัดเก็บข้อมูลการขายด้วย Google Sheets</p>
  </footer>

  <script src="app.js"></script>
  <script>
    const grid = document.getElementById('all-products');
    PRODUCTS.forEach(p => {{
      grid.innerHTML += `
        <div class="card">
          <img src="${{p.image}}" alt="${{p.name}}" class="card-img" />
          <span class="badge">รหัสสินค้า: ${{p.sku}}</span>
          <h3>${{p.name}}</h3>
          <p><strong>แบรนด์:</strong> ${{p.brand}} | <strong>ปริมาณ:</strong> ${{p.weight}}</p>
          <p>${{p.desc}}</p>
          <div class="price-row">
            <span class="price">฿${{p.price.toLocaleString()}}</span>
            <a href="order.html?sku=${{p.sku}}" class="btn btn-sm">เลือกสั่งซื้อ</a>
          </div>
        </div>
      `;
    }});
  </script>
</body>
</html>
"""

# 3. หน้าสั่งซื้อ (order.html)
order_html = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>หน้าสั่งซื้อ | GoldenBee ร้านน้ำผึ้งแท้ 100%</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
{get_navbar("order.html")}

  <main>
    <div class="box">
      <h1 class="section-title" style="font-size:1.75rem;">แบบฟอร์มสั่งซื้อน้ำผึ้งแท้</h1>
      <p class="section-sub" style="margin-bottom:1.5rem;">กรอกข้อมูลจัดส่งและเลือกรหัสสินค้า (SKU) ระบบจะบันทึกข้อมูลไปยัง Google Sheet อัตโนมัติ</p>

      <form id="orderForm">
        <div class="form-group">
          <label for="skuSelect">เลือกสินค้าน้ำผึ้ง (SKU) *</label>
          <select id="skuSelect" required></select>
        </div>

        <div id="productPreview" style="display:flex; gap:1rem; align-items:center; background:#fffbeb; padding:1rem; border-radius:12px; margin-bottom:1.25rem; border:1px solid #fde68a;">
          <img id="previewImg" src="" alt="สินค้า" style="width:70px; height:70px; object-fit:contain; background:#fff; border-radius:8px; padding:4px;" />
          <div>
            <div id="previewName" style="font-weight:600; color:#1e293b;"></div>
            <div id="previewPrice" style="color:#b45309; font-weight:700;"></div>
          </div>
        </div>

        <div class="form-group">
          <label for="qty">จำนวน (ชิ้น/แพ็ค) *</label>
          <input type="number" id="qty" min="1" max="50" value="1" required />
        </div>

        <div class="form-group">
          <label for="customerName">ชื่อ-นามสกุล ผู้รับ *</label>
          <input type="text" id="customerName" placeholder="เช่น สมชาย ใจดี" required />
        </div>

        <div class="form-group">
          <label for="phone">เบอร์โทรศัพท์ติดต่อ *</label>
          <input type="tel" id="phone" placeholder="เช่น 081-234-5678" required />
        </div>

        <div class="form-group">
          <label for="address">ที่อยู่สำหรับจัดส่ง *</label>
          <textarea id="address" rows="3" placeholder="บ้านเลขที่, ถนน, ตำบล/แขวง, อำเภอ/เขต, จังหวัด, รหัสไปรษณีย์" required></textarea>
        </div>

        <div class="form-group">
          <label for="paymentMethod">ช่องทางการชำระเงิน *</label>
          <select id="paymentMethod" required>
            <option value="โอนเงินผ่านบัญชีธนาคาร / PromptPay">โอนเงินผ่านบัญชีธนาคาร / PromptPay</option>
            <option value="เก็บเงินปลายทาง (COD)">เก็บเงินปลายทาง (COD)</option>
          </select>
        </div>

        <div style="background:#f8fafc; padding:1rem; border-radius:12px; margin-bottom:1.5rem; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-weight:600;">ยอดชำระรวมทั้งสิ้น:</span>
          <span id="totalPrice" style="font-size:1.5rem; font-weight:700; color:#b45309;">฿0</span>
        </div>

        <button type="submit" id="submitBtn" class="btn" style="width:100%; font-size:1.1rem;">ยืนยันการสั่งซื้อ</button>
      </form>
    </div>
  </main>

  <footer>
    <p>© 2026 GoldenBee Honey Store | ระบบจัดเก็บข้อมูลการขายด้วย Google Sheets</p>
  </footer>

  <script src="app.js"></script>
  <script>
    const skuSelect = document.getElementById('skuSelect');
    const qtyInput = document.getElementById('qty');
    const urlParams = new URLSearchParams(window.location.search);
    const preselectedSku = urlParams.get('sku');

    PRODUCTS.forEach(p => {{
      const opt = document.createElement('option');
      opt.value = p.sku;
      opt.textContent = `[${{p.sku}}] ${{p.name}} - ฿${{p.price}}`;
      if (preselectedSku === p.sku) opt.selected = true;
      skuSelect.appendChild(opt);
    }});

    function updateSummary() {{
      const selected = PRODUCTS.find(p => p.sku === skuSelect.value) || PRODUCTS[0];
      const qty = parseInt(qtyInput.value) || 1;
      const total = selected.price * qty;
      document.getElementById('previewImg').src = selected.image;
      document.getElementById('previewName').textContent = selected.name;
      document.getElementById('previewPrice').textContent = `ราคาต่อหน่วย: ฿${{selected.price.toLocaleString()}} (${{selected.weight}})`;
      document.getElementById('totalPrice').textContent = `฿${{total.toLocaleString()}}`;
    }}

    skuSelect.addEventListener('change', updateSummary);
    qtyInput.addEventListener('input', updateSummary);
    updateSummary();

    document.getElementById('orderForm').addEventListener('submit', async (e) => {{
      e.preventDefault();
      const btn = document.getElementById('submitBtn');
      btn.disabled = true;
      btn.textContent = "กำลังบันทึกคำสั่งซื้อลง Google Sheet...";

      const selected = PRODUCTS.find(p => p.sku === skuSelect.value);
      const qty = parseInt(qtyInput.value) || 1;
      const orderData = {{
        orderId: "ORD-" + Date.now().toString().slice(-6),
        timestamp: new Date().toLocaleString('th-TH'),
        sku: selected.sku,
        productName: selected.name,
        qty: qty,
        unitPrice: selected.price,
        totalPrice: selected.price * qty,
        customerName: document.getElementById('customerName').value.trim(),
        phone: document.getElementById('phone').value.trim(),
        address: document.getElementById('address').value.trim(),
        paymentMethod: document.getElementById('paymentMethod').value,
        status: "รอดำเนินการ"
      }};

      await submitOrderToSheet(orderData);
      window.location.href = "thankyou.html";
    }});
  </script>
</body>
</html>
"""

# 4. หน้าแอดมิน (admin.html)
admin_html = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>หน้าแอดมิน | จัดการคำสั่งซื้อและเชื่อมต่อ Google Sheet</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
{get_navbar("admin.html")}

  <main>
    <div class="box box-wide">
      <h1 class="section-title" style="font-size:1.75rem; text-align:left;">ระบบหลังบ้าน (Admin Dashboard)</h1>
      <p style="color:#64748b; margin-bottom:1.5rem;">จัดการรายการสั่งซื้อ ตรวจสอบยอดขาย และเชื่อมต่อฐานข้อมูล Google Sheets</p>

      <div class="alert">
        <strong>🔗 การเชื่อมต่อ Google Sheet API (Google Apps Script):</strong>
        <div style="display:flex; gap:0.5rem; margin-top:0.5rem; flex-wrap:wrap;">
          <input type="url" id="gasUrlInput" placeholder="วาง Web App URL จาก Google Apps Script ที่นี่ (https://script.google.com/macros/s/.../exec)" style="flex:1; min-width:260px;" />
          <button onclick="saveGasUrl()" class="btn btn-sm">บันทึกการเชื่อมต่อ</button>
          <button onclick="loadOrders()" class="btn btn-sm btn-outline">รีเฟรชข้อมูล</button>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
        <div style="background:#fffbeb; padding:1.25rem; border-radius:14px; border:1px solid #fde68a;">
          <div style="font-size:0.9rem; color:#64748b;">จำนวนออเดอร์ทั้งหมด</div>
          <div id="statCount" style="font-size:1.75rem; font-weight:700; color:#1e293b;">0</div>
        </div>
        <div style="background:#fffbeb; padding:1.25rem; border-radius:14px; border:1px solid #fde68a;">
          <div style="font-size:0.9rem; color:#64748b;">ยอดขายรวมทั้งหมด</div>
          <div id="statRevenue" style="font-size:1.75rem; font-weight:700; color:#b45309;">฿0</div>
        </div>
      </div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>รหัสออเดอร์</th>
              <th>วันที่-เวลา</th>
              <th>ลูกค้า / เบอร์โทร</th>
              <th>สินค้า (SKU)</th>
              <th>จำนวน</th>
              <th>ยอดรวม</th>
              <th>สถานะ</th>
              <th>จัดการ</th>
            </tr>
          </thead>
          <tbody id="ordersTableBody">
            <tr><td colspan="8" style="text-align:center;">กำลังโหลดข้อมูล...</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <footer>
    <p>© 2026 GoldenBee Honey Store | ระบบจัดเก็บข้อมูลการขายด้วย Google Sheets</p>
  </footer>

  <script src="app.js"></script>
  <script>
    document.getElementById('gasUrlInput').value = localStorage.getItem('HONEY_GAS_URL') || "";

    function saveGasUrl() {{
      const val = document.getElementById('gasUrlInput').value.trim();
      localStorage.setItem('HONEY_GAS_URL', val);
      alert("บันทึก URL ของ Google Sheet เรียบร้อยแล้ว!");
      loadOrders();
    }}

    async function loadOrders() {{
      const tbody = document.getElementById('ordersTableBody');
      tbody.innerHTML = '<tr><td colspan="8" style="text-align:center;">กำลังโหลดข้อมูล...</td></tr>';
      const orders = await fetchAllOrders();

      document.getElementById('statCount').textContent = orders.length + " รายการ";
      const totalRev = orders.reduce((sum, o) => sum + (Number(o.totalPrice) || 0), 0);
      document.getElementById('statRevenue').textContent = "฿" + totalRev.toLocaleString();

      if (orders.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="8" style="text-align:center; color:#94a3b8;">ยังไม่มีรายการสั่งซื้อในระบบ</td></tr>';
        return;
      }}

      tbody.innerHTML = "";
      orders.forEach(o => {{
        let pillClass = "status-pending";
        if (o.status === "ชำระเงินแล้ว") pillClass = "status-paid";
        if (o.status === "จัดส่งแล้ว") pillClass = "status-shipped";

        tbody.innerHTML += `
          <tr>
            <td><strong>${{o.orderId}}</strong></td>
            <td>${{o.timestamp}}</td>
            <td>${{o.customerName}}<br><small style="color:#64748b;">${{o.phone}}</small></td>
            <td><span class="badge">${{o.sku}}</span><br>${{o.productName}}</td>
            <td>${{o.qty}}</td>
            <td><strong>฿${{Number(o.totalPrice).toLocaleString()}}</strong></td>
            <td><span class="status-pill ${{pillClass}}">${{o.status}}</span></td>
            <td>
              <select onchange="changeStatus('${{o.orderId}}', this.value)" style="padding:0.35rem; font-size:0.85rem;">
                <option value="รอดำเนินการ" ${{o.status === 'รอดำเนินการ' ? 'selected' : ''}}>รอดำเนินการ</option>
                <option value="ชำระเงินแล้ว" ${{o.status === 'ชำระเงินแล้ว' ? 'selected' : ''}}>ชำระเงินแล้ว</option>
                <option value="จัดส่งแล้ว" ${{o.status === 'จัดส่งแล้ว' ? 'selected' : ''}}>จัดส่งแล้ว</option>
              </select>
            </td>
          </tr>
        `;
      }});
    }}

    async function changeStatus(orderId, status) {{
      await updateOrderStatus(orderId, status);
      loadOrders();
    }}

    loadOrders();
  </script>
</body>
</html>
"""

# 5. หน้าขอบคุณ (thankyou.html)
thankyou_html = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>หน้าขอบคุณ | GoldenBee ร้านน้ำผึ้งแท้ 100%</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
{get_navbar("thankyou.html")}

  <main>
    <div class="box" style="text-align:center;">
      <div style="font-size:4rem; margin-bottom:0.5rem;">🎉</div>
      <h1 style="color:#15803d; margin-bottom:0.5rem;">ขอบคุณสำหรับการสั่งซื้อ!</h1>
      <p style="color:#64748b; margin-bottom:2rem;">ระบบได้บันทึกข้อมูลคำสั่งซื้อของคุณเรียบร้อยแล้ว ทางร้านจะรีบดำเนินการจัดส่งให้เร็วที่สุด</p>

      <div id="orderReceipt" style="text-align:left; background:#fffbeb; border:1px solid #fde68a; border-radius:16px; padding:1.5rem; margin-bottom:2rem;">
        <p style="text-align:center; color:#64748b;">ยังไม่มีข้อมูลคำสั่งซื้อล่าสุด</p>
      </div>

      <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
        <a href="index.html" class="btn">กลับสู่หน้าแรก</a>
        <a href="admin.html" class="btn btn-outline">ตรวจสอบสถานะในหน้าแอดมิน</a>
      </div>
    </div>
  </main>

  <footer>
    <p>© 2026 GoldenBee Honey Store | ระบบจัดเก็บข้อมูลการขายด้วย Google Sheets</p>
  </footer>

  <script>
    const lastOrder = JSON.parse(localStorage.getItem('LAST_ORDER') || "null");
    if (lastOrder) {{
      document.getElementById('orderReceipt').innerHTML = `
        <h3 style="margin-bottom:1rem; color:#b45309; border-bottom:1px solid #fde68a; padding-bottom:0.5rem;">สรุปรายการคำสั่งซื้อ #${{lastOrder.orderId}}</h3>
        <p><strong>วันที่สั่งซื้อ:</strong> ${{lastOrder.timestamp}}</p>
        <p><strong>ชื่อผู้รับ:</strong> ${{lastOrder.customerName}} (${{lastOrder.phone}})</p>
        <p><strong>ที่อยู่จัดส่ง:</strong> ${{lastOrder.address}}</p>
        <p><strong>สินค้า:</strong> [${{lastOrder.sku}}] ${{lastOrder.productName}} จำนวน ${{lastOrder.qty}} ชิ้น</p>
        <p><strong>วิธีชำระเงิน:</strong> ${{lastOrder.paymentMethod}}</p>
        <p style="font-size:1.25rem; color:#b45309; margin-top:0.75rem;"><strong>ยอดชำระสุทธิ: ฿${{Number(lastOrder.totalPrice).toLocaleString()}}</strong></p>
      `;
    }}
  </script>
</body>
</html>
"""

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
with open(os.path.join(base_dir, "products.html"), "w", encoding="utf-8") as f:
    f.write(products_html)
with open(os.path.join(base_dir, "order.html"), "w", encoding="utf-8") as f:
    f.write(order_html)
with open(os.path.join(base_dir, "admin.html"), "w", encoding="utf-8") as f:
    f.write(admin_html)
with open(os.path.join(base_dir, "thankyou.html"), "w", encoding="utf-8") as f:
    f.write(thankyou_html)

# Google Apps Script code for Google Sheets backend
gas_code = """// =========================================================================
// โค้ด Google Apps Script สำหรับเชื่อมต่อเว็บไซต์ขายน้ำผึ้งกับ Google Sheets
// วิธีใช้งาน:
// 1. สร้าง Google Sheet ใหม่ ตั้งชื่อชีตแรก (Tab) ว่า "Orders"
// 2. ไปที่เมนู ส่วนขยาย (Extensions) > Apps Script
// 3. ลบโค้ดเดิมออกทั้งหมด แล้ววางโค้ดนี้ลงไป กดบันทึก
// 4. กดปุ่ม "ทำให้ใช้งานได้" (Deploy) > "การทำให้ใช้งานได้รายการใหม่" (New deployment)
// 5. เลือกประเภทเป็น "เว็บแอป" (Web app) -> ตั้งค่าผู้มีสิทธิ์เข้าถึงเป็น "ทุกคน" (Anyone)
// 6. คัดลอก Web App URL ไปวางในหน้าแอดมิน (admin.html) ของเว็บไซต์
// =========================================================================

const SHEET_NAME = "Orders";

function setupSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
  }
  if (sheet.getLastRow() === 0) {
    sheet.appendRow([
      "Order ID", "Timestamp", "SKU", "Product Name", "Quantity",
      "Unit Price", "Total Price", "Customer Name", "Phone",
      "Address", "Payment Method", "Status"
    ]);
  }
  return sheet;
}

function doGet(e) {
  const sheet = setupSheet();
  const data = sheet.getDataRange().getValues();
  const orders = [];

  for (let i = 1; i < data.length; i++) {
    orders.push({
      orderId: data[i][0],
      timestamp: data[i][1],
      sku: data[i][2],
      productName: data[i][3],
      qty: data[i][4],
      unitPrice: data[i][5],
      totalPrice: data[i][6],
      customerName: data[i][7],
      phone: data[i][8],
      address: data[i][9],
      paymentMethod: data[i][10],
      status: data[i][11]
    });
  }

  return ContentService
    .createTextOutput(JSON.stringify({ status: "success", orders: orders.reverse() }))
    .setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  const sheet = setupSheet();
  const payload = JSON.parse(e.postData.contents);

  if (payload.action === "createOrder") {
    sheet.appendRow([
      payload.orderId,
      payload.timestamp,
      payload.sku,
      payload.productName,
      payload.qty,
      payload.unitPrice,
      payload.totalPrice,
      payload.customerName,
      payload.phone,
      payload.address,
      payload.paymentMethod,
      payload.status || "รอดำเนินการ"
    ]);
    return ContentService
      .createTextOutput(JSON.stringify({ status: "created", orderId: payload.orderId }))
      .setMimeType(ContentService.MimeType.JSON);
  }

  if (payload.action === "updateStatus") {
    const data = sheet.getDataRange().getValues();
    for (let i = 1; i < data.length; i++) {
      if (data[i][0] == payload.orderId) {
        sheet.getRange(i + 1, 12).setValue(payload.status);
        break;
      }
    }
    return ContentService
      .createTextOutput(JSON.stringify({ status: "updated", orderId: payload.orderId }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
"""

with open(os.path.join(base_dir, "google_apps_script", "Code.gs"), "w", encoding="utf-8") as f:
    f.write(gas_code)

readme_txt = """โครงสร้างโปรเจกต์เว็บไซต์ขายน้ำผึ้งแท้ (GoldenBee Honey Store)
=========================================================
1. index.html          - หน้าแรก (Hero Banner + สินค้าแนะนำ)
2. products.html       - หน้าสินค้าทั้งหมด (4 SKUs: น้ำผึ้งเวชพงศ์ และ น้ำผึ้งดอยคำ 3 ขนาด)
3. order.html          - หน้าสั่งซื้อ (เลือก SKU, คำนวณราคาอัตโนมัติ, บันทึกลง Google Sheet)
4. admin.html          - หน้าแอดมิน (เชื่อมต่อ Google Sheet URL, ดูยอดขาย, อัปเดตสถานะจัดส่ง)
5. thankyou.html       - หน้าขอบคุณ (แสดงใบสรุปคำสั่งซื้อหลังสั่งซื้อสำเร็จ)
6. style.css           - ไฟล์ตกแต่งดีไซน์เว็บไซต์ (Responsive รองรับมือถือและคอมพิวเตอร์)
7. app.js              - ไฟล์ข้อมูลสินค้า 4 SKUs และระบบเชื่อมต่อ API ของ Google Sheet
8. images/             - โฟลเดอร์เก็บรูปภาพสินค้าแยกต่างหาก (vejpong_honey.jpg, doikham_honey.webp)
9. google_apps_script/Code.gs - โค้ดสำหรับนำไปวางใน Google Sheet (Extensions > Apps Script)
"""

with open(os.path.join(base_dir, "README.txt"), "w", encoding="utf-8") as f:
    f.write(readme_txt)

# Create ZIP archive in /mnt/data or current working dir
zip_filename = "honey-landing-page-5pages.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir)
            zipf.write(full_path, rel_path)

print("Generated ZIP:", os.path.abspath(zip_filename))
print("Contents:", zipfile.ZipFile(zip_filename).namelist())