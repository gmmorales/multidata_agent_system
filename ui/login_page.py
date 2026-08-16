"""
ui/login_page.py
Vista de inicio de sesión de la aplicación MDAS.
"""

import streamlit as st
from auth.authenticator import UserAuthenticator


class LoginPage:
    """Renderiza el formulario de inicio de sesión."""

    def __init__(self, authenticator: UserAuthenticator):
        self.authenticator = authenticator

    def render(self):
        st.markdown("<h1 style='text-align: center;'>🤖 MDAS Suite</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray;'>Multi-Data Agent System for Data Consulting</p>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader("🔐 Iniciar Sesión")
            with st.form("login_form"):
                username = st.text_input("Usuario", placeholder="ej: gustavo")
                password = st.text_input("Contraseña", type="password")
                submit = st.form_submit_button("Ingresar", use_container_width=True)

                if submit:
                    if self.authenticator.login(username, password):
                        st.success("¡Bienvenido! Redirigiendo...")
                        st.rerun()
                    else:
                        st.error("Usuario o contraseña incorrectos.")