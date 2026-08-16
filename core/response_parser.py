"""
core/response_parser.py
Utilidades para parsear y estructurar las respuestas generadas por los agentes.
"""

import re
from typing import List


class OutputParser:
    """Clase utilitaria para extracción y análisis de bloques de código en respuestas Markdown."""

    @staticmethod
    def parse_markdown_blocks(text: str) -> List[str]:
        """
        Extrae todo el contenido delimitado por bloques de código Markdown (```...```).
        """
        pattern = r"```(?:\w+)?\n(.*?)```"
        blocks = re.findall(pattern, text, re.DOTALL)
        return [block.strip() for block in blocks]