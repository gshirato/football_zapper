import streamlit as st
import os
import glob

st.sidebar.title("Football Zapper")

if "login_attempts" not in st.session_state:
    st.session_state["login_attempts"] = 0
if "is_authenticated" not in st.session_state:
    st.session_state["is_authenticated"] = False

if not st.experimental_user.is_logged_in:
    if st.sidebar.button("Googleでログイン"):
        st.login("google")
    st.stop()


allowed_users = st.secrets["auth"].get("allowed_users", [])
user_email = st.experimental_user.email
if user_email in allowed_users:
    st.session_state["is_authenticated"] = True
else:
    st.warning(f"ログイン失敗: {user_email}")
    if st.sidebar.button("再ログイン"):
        st.sidebar.login("google")
        st.stop()

if st.session_state["is_authenticated"]:

    root_dir = os.path.abspath(os.path.curdir)

    root_dir = "docs"  # Markdownファイルのルートディレクトリ
    categories = [
        d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))
    ]

    # サイドバーでカテゴリを選択
    selected_category = st.sidebar.selectbox("カテゴリを選択", categories)

    # 選択したカテゴリ内のMarkdownファイルを取得
    category_path = os.path.join(root_dir, selected_category)
    md_files = glob.glob(os.path.join(category_path, "*.md"))

    if md_files:
        md_file_names = [os.path.basename(f) for f in md_files]
        selected_file = st.sidebar.selectbox(
            "ファイルを選択", md_file_names, format_func=lambda x: x.split(".")[0]
        )

        # 選択したMarkdownファイルを表示
        with open(
            os.path.join(category_path, selected_file), "r", encoding="utf-8"
        ) as f:
            md_content = f.read()

        st.markdown(md_content, unsafe_allow_html=True)
    else:
        st.write("このカテゴリにはMarkdownファイルがありません。")

    if st.sidebar.button("Logout"):
        st.logout()
        st.session_state["is_authenticated"] = False
        st.stop()
