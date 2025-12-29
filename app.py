import streamlit as st

# 1. 設定頁面
st.set_page_config(page_title="醫學研究工具箱", page_icon="📄", layout="wide", initial_sidebar_state="collapsed")

# 2. 定義 HTML (重點：所有 HTML 標籤都必須「靠左對齊」，不能有縮排)
html_code = """
<style>
    :root { --bg: #ffffff; --text: #333333; --blue: #007bff; }
    .stApp { background-color: var(--bg) !important; color: var(--text) !important; }
    header, footer, #MainMenu { display: none !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    .main-box { max-width: 900px; margin: 0 auto; padding: 60px 20px; font-family: sans-serif; line-height: 1.8; }
    h1 { text-align: center; color: #2c3e50; font-size: 2.5rem; margin-bottom: 10px; }
    .sub { text-align: center; color: #666; margin-bottom: 50px; }
    .card { background: #f8f9fa; border-radius: 12px; padding: 40px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin: 30px 0; border: 1px solid #eee; }
    .price { font-size: 2.2rem; color: var(--blue); font-weight: bold; margin: 20px 0; }
    .btn { background: var(--blue); color: white !important; padding: 12px 50px; border-radius: 50px; text-decoration: none; font-weight: bold; border: none; cursor: pointer; }
    .btn:hover { background: #0056b3; }
    .footer { text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; color: #888; font-size: 0.9rem; }
</style>

<div class="main-box">
<div style="text-align: center; font-size: 3rem; margin-bottom: 10px;">📄</div>
<h1>研究工具箱</h1>
<p class="sub">專為研究人員打造的數位效率工具</p>

<div class="card">
<h3 style="color:#333;">研究計畫書標準格式範本 (2025版)</h3>
<p style="color:#666;">包含文獻回顧、研究方法與預期成果的標準段落配置及個段落內容提示。</p>
<div class="price">NT$ 150</div>
<button class="btn" onclick="alert('系統維護中，請稍後再試。')">立即購買範本</button>
</div>

<div class="footer">
<p>Copyright © 2025 Research Tools.</p>
<p>聯絡信箱：coffee.ewa@example.com</p>
<p>聯絡電話：0975-665-509</p>
<p>聯絡人：林小姐</p>
</div>
</div>
"""

# 3. 渲染 (確保 unsafe_allow_html=True)
st.markdown(html_code, unsafe_allow_html=True)




