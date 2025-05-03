import streamlit as st
import os
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(page_title="Football Zapper", page_icon=":tv:", layout="wide")
st.sidebar.title("Football Zapper")


def get_nav_from_category(category):
    folder = ".streamlit"
    return get_nav_from_toml(os.path.join(folder, f"{category}.toml"))


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
    st.write(f"Logged in as {st.experimental_user.name}")
    root_dir = os.path.abspath(os.path.curdir)

    root_dir = "src/football_zapper/pages"  # Markdownファイルのルートディレクトリ
    categories = [
        d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))
    ]

    # サイドバーでカテゴリを選択
    selected_category = st.sidebar.selectbox("カテゴリを選択", categories)

    nav = get_nav_from_category(selected_category)

    page = st.navigation(nav)

    add_page_title(page)
    page.run()

    if st.sidebar.button("Logout"):
        st.logout()
        st.session_state["is_authenticated"] = False
        st.stop()
