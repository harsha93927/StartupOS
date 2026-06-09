from typing import Dict, Type, Any
from pydantic import BaseModel

class AgentBase(BaseModel):
    name: str
    description: str

class AgentRegistry:
    def __init__(self):
        self._agents: Dict[str, Any] = {}

    def register(self, name: str, agent_class: Any):
        self._agents[name] = agent_class

    def get_agent(self, name: str):
        return self._agents.get(name)

    def list_agents(self):
        return [{"name": name, "description": agent.description} for name, agent in self._agents.items()]

agent_registry = AgentRegistry()
