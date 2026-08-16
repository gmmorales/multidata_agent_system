"""
core/gemini_service.py
Servicio para interactuar con la API de Google Gemini (google-genai).
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config.settings import AppConfig

# Carga las variables definidas en el archivo .env ubicado en la raíz del proyecto
load_dotenv()


class GeminiService:
    """Clase para gestionar las llamadas a Gemini usando variables de entorno."""

    def __init__(self, api_key: str = None, model_name: str = AppConfig.DEFAULT_MODEL):
        self.api_key = api_key or os.environ.get("GOOGLE_API_KEY", "")
        self.model_name = model_name

        if not self.api_key:
            raise ValueError("No se encontró la GOOGLE_API_KEY en las variables de entorno.")

    def generate_response(
        self,
        system_instruction: str,
        messages_history: list,
        temperature: float = AppConfig.DEFAULT_TEMPERATURE,
    ) -> str:
        client = genai.Client(api_key=self.api_key)

        config = types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=temperature,
        )

        contents = []
        for msg in messages_history:
            role = "user" if msg["role"] == "user" else "model"
            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=msg["content"])]
                )
            )

        response = client.models.generate_content(
            model=self.model_name,
            contents=contents,
            config=config,
        )

        return response.text