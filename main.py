"""
main.py
Orquestador de la aplicación MDAS.
"""

import streamlit as st
from config.settings import AppConfig
from auth.authenticator import UserAuthenticator
from ui.login_page import LoginPage
from ui.dashboard_page import DashboardPage


class AppOrchestrator:
    """Orquestador principal que controla la navegación y el ciclo de vida."""

    def __init__(self):
        st.set_page_config(
            page_title=AppConfig.APP_TITLE,
            page_icon=AppConfig.APP_ICON,
            layout=AppConfig.PAGE_LAYOUT
        )
        self.authenticator = UserAuthenticator()
        self.login_page = LoginPage(self.authenticator)
        self.dashboard_page = DashboardPage()

    def run(self):
        """Ejecuta el flujo según el estado de autenticación."""
        if not self.authenticator.is_authenticated():
            self.login_page.render()
        else:
            self.dashboard_page.render(self.authenticator)