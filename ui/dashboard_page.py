"""
ui/dashboard_page.py
Vista principal del panel de agentes y chat interactivo.
"""

import streamlit as st
from core.agent_manager import AgentManager
from core.gemini_service import GeminiService
from core.response_parser import OutputParser
from ui.components.sidebar import SidebarComponent
from ui.components.tabs_renderer import TabsRenderer


class DashboardPage:
    """Renderiza el panel de trabajo principal."""

    def __init__(self):
        self.agent_manager = AgentManager()

    def render(self, authenticator):
        # 1. Render de la Sidebar
        sidebar_data = SidebarComponent.render(self.agent_manager, authenticator)
        active_agent = sidebar_data["active_agent"]

        # 2. Encabezado Principal
        st.title(f"{active_agent.icon} {active_agent.name}")
        st.caption(active_agent.description)

        # 3. Control de cambio de agente en el estado de sesión
        if "current_agent_id" not in st.session_state or st.session_state.current_agent_id != active_agent.id:
            st.session_state.current_agent_id = active_agent.id
            st.session_state.messages = []

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # 4. Historial de Mensajes (Renderiza dinámicamente pestañas si detecta los 3 bloques)
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                if msg["role"] == "assistant":
                    bloques = OutputParser.parse_markdown_blocks(msg["content"])
                    if len(bloques) >= 3:
                        TabsRenderer.render_scaffold_output(bloques, sidebar_data["so_selected"])
                    else:
                        st.markdown(msg["content"])
                else:
                    st.markdown(msg["content"])

        # 5. Lógica del Botón "Iniciar Proceso" (Scaffolder)
        if sidebar_data["run_btn"]:
            prompt_ejecucion = f"""Iniciar proceso.
Sistema Operativo: {sidebar_data['so_selected']}
Nombre del Customer: {sidebar_data['customer_input'] if sidebar_data['customer_input'] else 'No especificado'}
Operador Responsable: {sidebar_data['operator_input'] if sidebar_data['operator_input'] else 'Anónimo'}"""

            st.session_state.messages.append({"role": "user", "content": prompt_ejecucion})

            with st.spinner(f"El {active_agent.name} está trabajando..."):
                try:
                    service = GeminiService()
                    response_text = service.generate_response(
                        system_instruction=active_agent.system_prompt,
                        messages_history=st.session_state.messages
                    )
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                    st.rerun()
                except Exception as e:
                    st.error(f"Error al procesar con Gemini: {e}")

        # 6. Entrada del Chat Estándar
        if user_prompt := st.chat_input(f"Consulta a {active_agent.name}..."):
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            with st.spinner("Procesando..."):
                try:
                    service = GeminiService()
                    response_text = service.generate_response(
                        system_instruction=active_agent.system_prompt,
                        messages_history=st.session_state.messages
                    )
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                    st.rerun()
                except Exception as e:
                    st.error(f"Error en la consulta: {e}")