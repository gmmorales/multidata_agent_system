"""
ui/components/tabs_renderer.py
Componente para visualizar y descargar los bloques de salida del Scaffolder.
"""

import streamlit as st
from typing import List


class TabsRenderer:
    """Renderiza las pestañas con los entregables de código/documentación."""

    @staticmethod
    def render_scaffold_output(bloques: List[str], so_selected: str):
        if len(bloques) >= 3:
            st.success("✅ Andamiaje generado exitosamente en 3 bloques independientes.")
            tab1, tab2, tab3 = st.tabs(["📄 Instrucciones de Inicio", "📝 Log de Operaciones", "💻 Script de Automatización"])

            with tab1:
                st.markdown(bloques[0])
                st.download_button(
                    "Descargar instrucciones_inicio.md",
                    data=bloques[0],
                    file_name="instrucciones_inicio.md",
                    mime="text/markdown"
                )

            with tab2:
                st.markdown(bloques[1])
                st.download_button(
                    "Descargar log.md",
                    data=bloques[1],
                    file_name="log.md",
                    mime="text/markdown"
                )

            with tab3:
                lang = "powershell" if so_selected == "Windows" else "bash"
                ext = "ps1" if so_selected == "Windows" else "sh"
                st.code(bloques[2], language=lang)
                st.download_button(
                    f"Descargar setup_scaffold.{ext}",
                    data=bloques[2],
                    file_name=f"setup_scaffold.{ext}",
                    mime="text/plain"
                )
        else:
            st.warning("⚠️ La respuesta del agente no contiene los 3 bloques en el formato estricto.")