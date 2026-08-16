"""
ui/components/sidebar.py
Componente de barra lateral para selección de agente y parámetros.
"""

import streamlit as st
from core.agent_manager import AgentManager


class SidebarComponent:
    """Renderiza y gestiona el contenido de la barra lateral."""

    @staticmethod
    def render(agent_manager: AgentManager, authenticator):
        st.sidebar.title("🛠️ Configuración MDAS")

        # Muestrario de usuario actual y botón de Logout
        user = authenticator.get_current_user()
        st.sidebar.caption(f"👤 Usuario: **{user}**")
        if st.sidebar.button("🚪 Cerrar Sesión", use_container_width=True):
            authenticator.logout()

        st.sidebar.markdown("---")

        # 1. Selección dinámica del agente registrado
        st.sidebar.subheader("🤖 Agente Activo")
        agents = agent_manager.list_agents()
        agent_options = {f"{a.icon} {a.name}": a.id for a in agents}
        
        selected_label = st.sidebar.selectbox(
            "Seleccionar Agente:",
            options=list(agent_options.keys())
        )
        selected_agent_id = agent_options[selected_label]
        active_agent = agent_manager.get_agent(selected_agent_id)

        st.sidebar.info(active_agent.description)

        st.sidebar.markdown("---")

        # 2. Parámetros específicos para la ejecución
        so_selected = "Windows"
        customer_input = ""
        operator_input = ""
        run_btn = False

        if active_agent.id == "scaffolder":
            st.sidebar.subheader("📋 Parámetros de Scaffolding")
            so_selected = st.sidebar.selectbox("Sistema Operativo Target", ["Windows", "Linux"])
            customer_input = st.sidebar.text_input("Nombre Customer / Proyecto", placeholder="ej: acme_corp")
            operator_input = st.sidebar.text_input("Operador Responsable", value=user)
            run_btn = st.sidebar.button("🚀 Iniciar Proceso", type="primary", use_container_width=True)

        return {
            "active_agent": active_agent,
            "so_selected": so_selected,
            "customer_input": customer_input,
            "operator_input": operator_input,
            "run_btn": run_btn
        }