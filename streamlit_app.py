import streamlit as st

st.set_page_config(
    page_title="Remote Job Search",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Remote Job Search")
st.write("フルリモート求人を探すための求人検索ツール")

st.divider()

st.subheader("求人検索条件")

col1, col2 = st.columns(2)

with col1:
    keyword = st.text_input(
        "キーワード",
        placeholder="例：未経験 Webクリエイター"
    )

with col2:
    salary = st.selectbox(
        "希望年収",
        ["指定なし", "300万円以上", "350万円以上", "400万円以上", "500万円以上"]
    )

remote = st.checkbox("フルリモートのみ")
weekend = st.checkbox("土日祝休み")

if st.button("🔍 求人を検索"):
    st.success("検索条件を受け付けました！")

    st.write("### 検索条件")
    st.write(f"キーワード：{keyword or '指定なし'}")
    st.write(f"希望年収：{salary}")
    st.write(f"フルリモート：{'指定あり' if remote else '指定なし'}")
    st.write(f"土日祝休み：{'指定あり' if weekend else '指定なし'}")

    st.info("現在は検索画面の試作版です。次の段階で求人情報の取得機能を追加します。")
