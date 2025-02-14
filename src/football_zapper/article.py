import streamlit as st
import os


st.title("Football Zapper")

if "login_attempts" not in st.session_state:
    st.session_state["login_attempts"] = 0
if "is_authenticated" not in st.session_state:
    st.session_state["is_authenticated"] = False

if not st.experimental_user.is_logged_in:
    if st.button("Googleでログイン"):
        st.login("google")
    st.stop()


allowed_users = st.secrets["auth"].get("allowed_users", [])
user_email = st.experimental_user.email
if user_email in allowed_users:
    st.session_state["is_authenticated"] = True
else:
    st.warning(f"ログイン失敗: {user_email}")
    if st.button("再ログイン"):
        st.login("google")
        st.stop()

if st.session_state["is_authenticated"]:

    root_dir = os.path.abspath(os.path.curdir)

    st.write("ログインしました!")

    if st.button("Logout"):
        st.logout()
        st.session_state["is_authenticated"] = False
        st.stop()
