"""
core/base_agent.py
Clase que representa la estructura base de un agente dentro del ecosistema MDAS.
"""


class Agent:
    """Representa a un agente del sistema MDAS."""

    def __init__(
        self,
        agent_id: str,
        name: str,
        description: str,
        system_prompt: str,
        icon: str = "🤖",
        enabled: bool = True,
    ):
        self.id = agent_id
        self.name = name
        self.description = description
        self.system_prompt = system_prompt
        self.icon = icon
        self.enabled = enabled

    def __repr__(self):
        return f"<Agent id='{self.id}' name='{self.name}'>"