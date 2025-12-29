import streamlit as st

# 1. 設定頁面配置 (必須是第一行 Streamlit 指令)
st.set_page_config(
    page_title="醫學研究工具箱", # 瀏覽器標籤名稱
    page_icon="📄",
    layout="wide",            # 使用寬版模式
    initial_sidebar_state="collapsed" # 預設隱藏側邊欄
)

# 2. 讀取 index.html 檔案內容
def load_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Error: index.html not found.</h1>"

html_content = load_html_file("index.html")

# 3. CSS Hack: 移除 Streamlit 預設的邊距與選單，讓 HTML 滿版呈現
# 這樣審查人員才不會覺得「這網站怎麼長得像後台」
hide_streamlit_style = """
            <style>
            /* 隱藏右上角漢堡選單 */
            #MainMenu {visibility: hidden;}
            /* 隱藏頁尾 "Made with Streamlit" */
            footer {visibility: hidden;}
            /* 隱藏頂部 header 裝飾條 */
            header {visibility: hidden;}
            
            /* 移除 Streamlit 預設的 padding，讓背景全黑無白邊 */
            .block-container {
                padding-top: 0rem !important;
                padding-bottom: 0rem !important;
                padding-left: 0rem !important;
                padding-right: 0rem !important;
                max-width: 100% !important;
            }
            
            /* 強制背景色為黑色 (確保與 index.html 一致) */
            .stApp {
                background-color: #000000;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 4. 渲染 HTML 內容
st.markdown(html_content, unsafe_allow_html=True)