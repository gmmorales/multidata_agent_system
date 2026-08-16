"""
auth/authenticator.py
Módulo para la gestión de sesiones y autenticación de usuarios.
"""

import streamlit as st


class UserAuthenticator:
    """Clase para validar credenciales y controlar la sesión del usuario."""

    # Usuario y clave por defecto (puedes personalizarlos)
    DEFAULT_USERS = {
        "administrador": "administrador123",
        "gmorales": "gmorales123",
        "lprado": "lpardo123"
    }

    def __init__(self):
        self._init_session_state()

    def _init_session_state(self) -> None:
        """Inicializa las variables de estado de sesión si no existen."""
        if "authenticated" not in st.session_state:
            st.session_state["authenticated"] = False
        if "username" not in st.session_state:
            st.session_state["username"] = None

    def login(self, username_input: str, password_input: str) -> bool:
        """Valida el usuario y contraseña contra el registro."""
        user = username_input.strip().lower()
        if user in self.DEFAULT_USERS and self.DEFAULT_USERS[user] == password_input:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username_input
            return True
        return False

    def logout(self) -> None:
        """Cierra la sesión activa."""
        st.session_state["authenticated"] = False
        st.session_state["username"] = None
        st.rerun()

    def is_authenticated(self) -> bool:
        """Retorna True si el usuario ya inició sesión."""
        return st.session_state.get("authenticated", False)

    def get_current_user(self) -> str:
        """Retorna el nombre del usuario autenticado."""
        return st.session_state.get("username", "Anónimo")