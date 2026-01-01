import streamlit as st

# 1. 頁面設定
st.set_page_config(
    page_title="研究工具箱 | Research Tools",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Uber 風格 CSS 優化 (針對新版 Streamlit 強制修正)
st.markdown("""
<style>
    /* --- Uber Day Style 變數 --- */
    :root {
        --uber-black: #000000;
        --uber-white: #FFFFFF;
        --uber-gray-text: #545454;
        --uber-border: #E0E0E0;
        --font-stack: 'Uber Move', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* 全站基礎設定 */
    .stApp {
        background-color: var(--uber-white);
        color: var(--uber-black);
        font-family: var(--font-stack);
    }
    
    /* 隱藏 Streamlit 原生介面 */
    header[data-testid="stHeader"], footer, #MainMenu {display: none;}
    
    /* 調整頂部間距 */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 5rem !important;
        max-width: 960px !important;
    }

    /* --- 標題 Typography --- */
    .main-title {
        text-align: left;
        font-size: 3rem;
        font-weight: 700;
        color: var(--uber-black);
        letter-spacing: -0.02em;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        text-align: left;
        font-size: 1.25rem;
        color: var(--uber-gray-text);
        margin-bottom: 4rem;
        font-weight: 400;
    }
    
    h1, h2, h3 { color: var(--uber-black) !important; }
    p { color: var(--uber-gray-text); line-height: 1.6; }

    /* --- 商品卡片 --- */
    div[data-testid="column"] {
        background-color: var(--uber-white);
        border: 1px solid var(--uber-border);
        border-radius: 12px;
        padding: 24px;
        transition: all 0.2s ease;
        height: 100%;
    }
    div[data-testid="column"]:hover {
        border-color: var(--uber-black);
        transform: translateY(-2px);
    }
    
    /* --- 按鈕樣式 (終極修正版) --- */
    
    /* --- 按鈕樣式 (終極修正版：強制滿版) --- */
    
    /* 關鍵修正 1：外層容器必須設為 100% */
    div[data-testid="stButton"] {
        width: 100% !important;
        display: block;
    }
    
    /* 關鍵修正 2：按鈕本體設為 100% */
    div[data-testid="stButton"] > button {
        width: 100% !important;        /* 強制撐開 */
        background-color: #000000;     /* 純黑背景 */
        color: #FFFFFF !important;     /* 純白文字 */
        border: none;
        border-radius: 8px;
        padding: 14px 0;
        font-size: 1rem;
        font-weight: 700;
        transition: all 0.2s ease;
        display: block !important;     /* 確保是區塊元素 */
    }
    /* 3. 強制覆蓋按鈕內 <p> 標籤的顏色 (解決文字灰灰的問題) */
    div[data-testid="stButton"] > button p {
        color: #FFFFFF !important;
        width: 100%; 
    }
    
    /* 4. 滑鼠懸停 (Hover) 效果：背景變深灰 */
    div[data-testid="stButton"] > button:hover {
        background-color: #333333;
        transform: translateY(-2px);
        border-color: #000000;
        color: #FFD700 !important;      /* 文字變金 */
        width: 100%; 
    }

    /* 5. 滑鼠懸停時，內層文字也要變金 */
    div[data-testid="stButton"] > button:hover p {
        color: #FFD700 !important;
        width: 100%; 
    }

    /* --- 輸入框樣式 --- */
    .stTextInput > div > div > input {
        border-color: var(--uber-border);
        color: var(--uber-black);
        border-radius: 8px;
    }
    .stTextInput > div > div > input:focus {
        border-color: var(--uber-black);
        box-shadow: none;
    }

    /* --- 法律條款區塊 --- */
    .legal-header {
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 10px;
        color: var(--uber-black);
    }
    .legal-text {
        font-size: 0.85rem;
        color: var(--uber-gray-text);
        line-height: 1.6;
    }
    .streamlit-expanderHeader {
        font-weight: 500;
        color: var(--uber-gray-text);
    }
</style>
""", unsafe_allow_html=True)

# 3. 狀態管理
if 'cart_item' not in st.session_state:
    st.session_state.cart_item = None
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 頁面內容開始 ---

# Header
st.markdown('<div class="main-title">研究工具箱</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">為研究人員打造的高效論文與計畫書排版範本</div>', unsafe_allow_html=True)

# 模擬結帳成功頁面
if st.session_state.page == 'success':
    st.success("✅ 訂單已建立！感謝您的購買。")
    st.info("這是一個測試訂單。由於目前處於審核階段，不會實際進行扣款，也不會寄送檔案。")
    if st.button("返回首頁"):
        st.session_state.page = 'home'
        st.session_state.cart_item = None
        st.rerun()

# 填寫資料頁面
elif st.session_state.page == 'checkout':
    st.markdown(f"### 🛒 結帳確認")
    st.markdown(f"""
    <div style="padding: 20px; background: #F9F9F9; border-radius: 8px; margin-bottom: 20px;">
        <strong style="color: black;">商品：</strong> <span style="color: #555;">{st.session_state.cart_item['name']}</span><br>
        <strong style="color: black;">金額：</strong> <span style="color: black; font-weight: bold;">NT$ {st.session_state.cart_item['price']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("checkout_form"):
        st.write("請填寫訂購人資訊 (僅供測試，請勿填寫真實敏感個資)")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("姓名", placeholder="王小明")
        with col2:
            phone = st.text_input("手機號碼", placeholder="0912345678")
        
        email = st.text_input("Email (用於接收下載連結)", placeholder="example@email.com")
        
        st.markdown("---")
        st.caption("點擊下方按鈕即表示您同意本站之服務條款與隱私權政策。")
        
        submitted = st.form_submit_button("確認付款 (模擬)")
        
        if submitted:
            if not name or not email:
                st.error("請填寫姓名與 Email")
            else:
                st.session_state.page = 'success'
                st.rerun()
                
    if st.button("取消", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()

# 首頁：商品列表
else:
    col1, col2 = st.columns(2)

    # 商品 1
    with col1:
        st.image("https://placehold.co/600x400/000000/ffffff?text=Proposal+Template", use_container_width=True)
        st.markdown("### 研究計畫書標準格式範本")
        st.markdown("""
        **格式**：Word (.docx)  
        **適用**：大專院校專題計畫、國科會計畫申請  
        
        依照最新學術計畫格式編排，包含摘要、研究動機、文獻回顧及預期成果之標準排版設定，解決繁瑣的縮排與引用格式問題。也提供撰寫Reference List各種注意事項，讓您的計劃書專業度升級。
        """)
        st.markdown("#### NT$ 150")
        if st.button("立即購買", key="btn1", use_container_width=True):
            st.session_state.cart_item = {"name": "國科會/學術專題計畫書標準範本", "price": 150}
            st.session_state.page = 'checkout'
            st.rerun()

    # 商品 2
    with col2:
        st.image("https://placehold.co/600x400/333333/ffffff?text=Poster+Pack", use_container_width=True)
        st.markdown("### 學術研討會海報排版懶人包")
        st.markdown("""
        **格式**：PowerPoint (.pptx)  
        **適用**：國內外學術研討會 (Conference Poster)  
        
        內含 5 款常用的直式/橫式學術海報版型。已預設好高解析度尺寸與配色方案，只需替換文字與圖表即可輸出。
        """)
        st.markdown("#### NT$ 250")
        if st.button("立即購買", key="btn2", use_container_width=True):
            st.session_state.cart_item = {"name": "學術研討會海報排版懶人包", "price": 250}
            st.session_state.page = 'checkout'
            st.rerun()

# --- 法律條款區 ---
st.markdown("---")
st.markdown("### 商店資訊與法律條款")

with st.expander("查看【隱私權政策】"):
    st.markdown("""
    <div class="legal-text">
    <div class="legal-header">隱私權政策 (Privacy Policy)</div>
    本網站非常重視您的隱私權。本政策說明我們如何收集、使用及保護您的個人資訊。<br>
    1. 資料收集：當您購買商品時，我們僅收集必要的聯絡資訊（如姓名、Email），用於寄送數位檔案及訂單通知。<br>
    2. 資料使用：您的資料僅用於處理訂單與客戶服務，絕不會出售或透露給第三方。
    </div>
    """, unsafe_allow_html=True)

with st.expander("查看【退款政策與消費者權益】"):
    st.markdown("""
    <div class="legal-text">
    <div class="legal-header">退款政策 (Refund Policy)</div>
    1. 數位商品性質：本站販售之商品為「非以有形媒介提供之數位內容」，一經提供即為完成服務。<br>
    2. 無鑑賞期：依據《消費者保護法》，本站數位商品<strong>不適用七日鑑賞期</strong>。<br>
    3. 例外處理：若檔案有毀損，請於購買後 3 日內聯繫客服補寄。
    </div>
    """, unsafe_allow_html=True)

with st.expander("查看【服務條款】"):
    st.markdown("""
    <div class="legal-text">
    <div class="legal-header">服務條款 (Terms of Service)</div>
    1. 授權範圍：購買之範本僅供購買者個人學術研究、工作或教學使用。<br>
    2. 禁止轉售：嚴禁將本站範本進行轉售、公開散佈。<br>
    3. 免責聲明：本站範本僅供格式參考，內容撰寫概由使用者自行負責。
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align: left; margin-top: 40px; color: #888; font-size: 0.8rem; border-top: 1px solid #E0E0E0; padding-top: 20px;">
    <strong>Research Tools</strong> © 2026<br><br>
    聯絡信箱：coffee.ewa@gmail.com <br>
    聯絡電話：0917-xxx-xxx
</div>
""", unsafe_allow_html=True)


