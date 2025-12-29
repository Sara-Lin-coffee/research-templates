import streamlit as st

# 1. 設定頁面配置 (這行必須是第一行)
st.set_page_config(
    page_title="醫學研究工具箱",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 定義 HTML/CSS 內容
html_content = """
<style>
    /* --- 核心設計風格：黑底、白字、橘標題、黃重點 --- */
    :root {
        --bg-color: #000000;
        --text-color: #FFFFFF;
        --primary-color: #FF8C00;
        --highlight-color: #FFD700;
        --card-bg: #1A1A1A;
        --font-family: 'PingFang TC', 'Microsoft JhengHei', sans-serif;
    }

    /* 強制覆蓋 Streamlit 的預設背景 */
    .stApp {
        background-color: var(--bg-color) !important;
        color: var(--text-color) !important;
    }
    
    /* 隱藏 Streamlit 預設介面 */
    header[data-testid="stHeader"] {display: none;}
    footer {display: none;}
    #MainMenu {display: none;}
    
    /* 移除頂部空白 */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }

    /* 網頁內容樣式 */
    .custom-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 40px 20px;
        font-family: var(--font-family);
        line-height: 1.6;
    }

    h1, h2, h3 {
        color: var(--primary-color) !important;
        font-weight: 700;
    }
    
    h1 { font-size: 2.5rem; text-align: center; margin-bottom: 10px; }
    h2 { border-bottom: 2px solid var(--primary-color); padding-bottom: 10px; margin-top: 40px; }

    .highlight {
        color: var(--bg-color);
        background-color: var(--highlight-color);
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
    }

    .product-card {
        background-color: var(--card-bg);
        border-radius: 15px;
        padding: 30px;
        margin: 30px 0;
        text-align: center;
        border: 2px solid #333;
    }
    
    .product-card:hover {
        border-color: var(--primary-color);
    }

    .price {
        font-size: 2rem;
        color: var(--highlight-color);
        margin: 20px 0;
        font-weight: bold;
    }

    .btn {
        display: inline-block;
        background-color: var(--primary-color);
        color: var(--text-color) !important;
        padding: 15px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        border: none;
    }
    .btn:hover { background-color: #FF4500; }

    .policy-section {
        font-size: 0.9rem;
        color: #AAA;
        background: #111;
        padding: 20px;
        border-radius: 10px;
        margin-top: 50px;
    }

    .footer-text {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        color: #666;
        font-size: 0.9rem;
        border-top: 1px solid #333;
    }
</style>

<div class="custom-container">
    <div style="text-align: center; margin-bottom: 20px;">
        <span style="font-size: 3rem;">📄</span>
    </div>
    <h1>醫學研究工具箱</h1>
    <p style="text-align: center; font-size: 1.2rem; color: #fff;">
        專為研究人員打造的 <span class="highlight">數位效率工具</span> 與文件範本
    </p>

    <div id="products">
        <h2>精選範本</h2>
        <div class="product-card">
            <h3>IRB 研究計畫書標準格式範本 (2025版)</h3>
            <p style="color: #ccc; margin: 20px 0;">
                包含文獻回顧、研究方法與預期成果的標準段落配置。<br><br>
                格式：Word (.docx) / PDF <br>
                適用對象：醫學研究生、臨床醫師
            </p>
            <div class="price">NT$ 150</div>
            <button class="btn" onclick="alert('金流系統維護中，請稍後再試。')">
                立即購買範本
            </button>
        </div>
    </div>

    <div>
        <h2>關於作者</h2>
        <p style="color: #fff;">
            我是資訊工程碩士生，專注於 <span class="highlight">醫療影像 AI</span> 與系統整合。
            在協助多項臨床研究案的過程中，我整理了這套高效率的文件範本。
        </p>
    </div>

    <div class="policy-section">
        <h3 style="color: #fff; margin-top:0;">退換貨政策與服務條款</h3>
        <p>1. <strong>數位商品性質</strong>：本站販售之商品為數位內容，發送下載連結後即視為完成服務。</p>
        <p>2. <strong>退款規定</strong>：依據消保法規定，本站數位商品<span class="highlight">不適用七日鑑賞期</span>，售出後恕不退款。</p>
        <p>3. <strong>使用授權</strong>：購買之範本僅供個人學術研究使用，嚴禁轉售。</p>
    </div>

    <div class="footer-text">
        <p>Copyright © 2025 Medical Research Tools.</p>
        <p>
            聯絡信箱：<strong>your_email@example.com</strong> <br>
            聯絡電話：<strong>09xx-xxx-xxx</strong>
        </p>
    </div>
</div>
"""

# 3. 關鍵指令：渲染 HTML
st.markdown(html_content, unsafe_allow_html=True)
