"""
config/settings.py
Configuraciones globales de la aplicación MDAS.
"""

import os
from pathlib import Path


class AppConfig:
    """Clase con constantes y configuraciones globales."""

    # Rutas base del proyecto
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    CONFIG_DIR: Path = BASE_DIR / "config"
    AGENTS_REGISTRY_PATH: Path = CONFIG_DIR / "agents_registry.json"
    PROMPTS_DIR: Path = BASE_DIR / "prompts"

    # Parámetros por defecto para la API de Gemini
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "gemini-3.6-flash")
    DEFAULT_TEMPERATURE: float = 0.1

    # Título y metadatos de la aplicación
    APP_TITLE: str = "MDAS - Multi-Data Agent System"
    APP_ICON: str = "🤖"
    PAGE_LAYOUT: str = "wide"