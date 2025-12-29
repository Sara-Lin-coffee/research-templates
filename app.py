import streamlit as st

# 1. 設定頁面配置
st.set_page_config(
    page_title="醫學研究工具箱",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 定義 HTML/CSS 內容
# 注意：以下引號內就是純 HTML，請不要在裡面加上 markdown 的 ``` 符號
html_code = """
<style>
    /* --- 核心設計風格：白底、深灰字、專業藍 --- */
    :root {
        --bg-color: #FFFFFF;           /* 純白背景 */
        --text-color: #333333;         /* 深灰文字 */
        --primary-color: #007bff;      /* 專業藍 (醫學/科技感) */
        --secondary-color: #f8f9fa;    /* 淺灰背景 (卡片用) */
        --highlight-color: #e3f2fd;    /* 淺藍高亮 */
        --font-family: 'PingFang TC', 'Microsoft JhengHei', sans-serif;
    }

    /* 強制覆蓋 Streamlit 的預設背景 */
    .stApp {
        background-color: var(--bg-color) !important;
        color: var(--text-color) !important;
    }
    
    /* 隱藏 Streamlit 預設介面 (Header, Footer, Menu) */
    header[data-testid="stHeader"] {display: none;}
    footer {display: none;}
    #MainMenu {display: none;}
    
    /* 移除頂部空白，讓版面更緊湊 */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        max-width: 100% !important;
    }

    /* 網頁內容容器 */
    .custom-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 60px 20px;
        font-family: var(--font-family);
        line-height: 1.8;
    }

    /* 標題樣式 */
    h1 { 
        font-size: 2.8rem; 
        text-align: center; 
        margin-bottom: 10px; 
        color: #2c3e50;
        font-weight: 700;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 50px;
    }

    h2 { 
        border-left: 5px solid var(--primary-color); 
        padding-left: 15px; 
        margin-top: 50px; 
        margin-bottom: 20px;
        color: #2c3e50;
    }

    h3 { color: #2c3e50; font-weight: 600; }

    /* 重點文字高亮 */
    .highlight {
        background-color: var(--highlight-color);
        color: var(--primary-color);
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: bold;
    }

    /* 商品卡片 (清新風格：淺灰底 + 陰影) */
    .product-card {
        background-color: var(--secondary-color);
        border-radius: 12px;
        padding: 40px;
        margin: 30px 0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); /* 輕微陰影 */
        border: 1px solid #eaeaea;
        transition: transform 0.2s;
    }
    
    .product-card:hover {
        transform: translateY(-5px); /* 滑鼠移過去會浮起來 */
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }

    .price {
        font-size: 2.2rem;
        color: var(--primary-color);
        margin: 20px 0;
        font-weight: bold;
    }

    /* 按鈕樣式 (藍色圓角) */
    .btn {
        display: inline-block;
        background-color: var(--primary-color);
        color: white !important;
        padding: 12px 50px;
        border-radius: 50px;
        text-decoration: none;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        border: none;
        box-shadow: 0 2px 4px rgba(0,123,255,0.3);
    }
    .btn:hover { background-color: #0056b3; }

    /* 政策區域 (字體縮小) */
    .policy-section {
        font-size: 0.9rem;
        color: #666;
        background: #fdfdfd;
        padding: 25px;
        border-radius: 8px;
        border: 1px solid #eee;
        margin-top: 60px;
    }

    /* 頁尾 */
    .footer-text {
        text-align: center;
        margin-top: 50px;
        padding: 30px;
        color: #888;
        font-size: 0.9rem;
        border-top: 1px solid #eee;
    }
</style>

<div class="custom-container">
    <div style="text-align: center; margin-bottom: 20px;">
        <span style="font-size: 3.5rem;">📄</span>
    </div>
    <h1>醫學研究工具箱</h1>
    <p class="subtitle">
        專為研究人員打造的 <span class="highlight">數位效率工具</span> 與文件範本
    </p>

    <div id="products">
        <h2>精選範本</h2>
        <div class="product-card">
            <h3>IRB 研究計畫書標準格式範本 (2025版)</h3>
            <p style="color: #666; margin: 20px 0; line-height: 1.8;">
                不想從頭開始排版？這份範本整理了標準的 IRB 申請架構，<br>
                包含文獻回顧、研究方法與預期成果的標準段落配置。
            </p>
            <p style="font-size: 0.9rem; color: #888;">
                格式：Word (.docx) / PDF <br>
                適用對象：醫學研究生、臨床醫師、研究助理
            </p>
            <div class="price">NT$ 150</div>
            
            <button class="btn" onclick="alert('感謝您的興趣！本站目前進行系統維護中，暫無法結帳。')">
                立即購買範本
            </button>
        </div>
    </div>

    <div>
        <h2>關於作者</h2>
        <p>
            我是資訊工程碩士生，專注於 <span class="highlight">醫療影像 AI</span> 與系統整合。
            在協助多項臨床研究案的過程中，我發現許多研究人員花費大量時間在文件格式調整上。
            因此，我整理了這套高效率的文件範本，希望能幫助大家專注於核心研究。
        </p>
    </div>

    <div class="policy-section">
        <h3 style="margin-top:0; font-size: 1.1rem;">退換貨政策與服務條款</h3>
        <p>1. <strong>數位商品性質</strong>：本站販售之商品為數位內容（非以有形媒介提供），一經購買並發送下載連結後，即視為完成服務。</p>
        <p>2. <strong>退款規定</strong>：依據消費者保護法及通訊交易解除權合理例外情事適用準則，本站數位商品<span style="color: #d9534f; font-weight:bold;">不適用七日鑑賞期</span>，售出後恕不退款。</p>
        <p>3. <strong>使用授權</strong>：購買之範本僅供購買者個人學術研究或工作使用，嚴禁轉售、公開散佈或作為商業營利範本販售。</p>
    </div>

    <div class="footer-text">
        <p>Copyright © 2025 Medical Research Tools. All rights reserved.</p>
        <p>
            聯絡信箱：<strong>your_email@example.com</strong> <br>
            聯絡電話：<strong>09xx-xxx-xxx</strong>
        </p>
    </div>
</div>
"""

# 3. 渲染 HTML
st.markdown(html_code, unsafe_allow_html=True)
