"""
app.py
Punto de entrada principal para Streamlit.
Ejecución: streamlit run app.py
"""

from main import AppOrchestrator

if __name__ == "__main__":
    orchestrator = AppOrchestrator()
    orchestrator.run()