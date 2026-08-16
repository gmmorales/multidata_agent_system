"""
core/agent_manager.py
Cargador dinámico de agentes registrados en agents_registry.json.
"""

import importlib
import json
from typing import Dict, List
from config.settings import AppConfig
from core.base_agent import Agent


class AgentManager:
    """Gestor de agentes dinámico."""

    def __init__(self, registry_path=AppConfig.AGENTS_REGISTRY_PATH):
        self.registry_path = registry_path
        self.agents: Dict[str, Agent] = {}
        self._load_agents()

    def _load_agents(self) -> None:
        """Lee el JSON de registro e instancia dinámicamente los agentes habilitados."""
        if not self.registry_path.exists():
            raise FileNotFoundError(f"No se encontró el registro de agentes en: {self.registry_path}")

        with open(self.registry_path, "r", encoding="utf-8") as f:
            registry_data = json.load(f)

        for agent_id, data in registry_data.items():
            if not data.get("enabled", True):
                continue

            # Importación dinámica del módulo de prompt (ej: 'prompts.scaffolder')
            try:
                module = importlib.import_module(data["prompt_module"])
                system_prompt = getattr(module, data["prompt_var"], "")
            except (ImportError, AttributeError):
                system_prompt = "Instrucciones del sistema no configuradas."

            agent = Agent(
                agent_id=agent_id,
                name=data["name"],
                description=data["description"],
                system_prompt=system_prompt,
                icon=data.get("icon", "🤖"),
                enabled=data.get("enabled", True),
            )
            self.agents[agent_id] = agent

    def get_agent(self, agent_id: str) -> Agent:
        """Obtiene un agente específico por su ID."""
        return self.agents.get(agent_id)

    def list_agents(self) -> List[Agent]:
        """Retorna la lista de todos los agentes habilitados."""
        return list(self.agents.values())