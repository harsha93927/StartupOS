import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.agents.registry import agent_registry
from app.agents.competitor_agent import CompetitorAgent

def test_agent_registration():
    agent = CompetitorAgent()
    agent_registry.register("competitor_test", agent)
    retrieved = agent_registry.get_agent("competitor_test")
    assert retrieved == agent
    agents = agent_registry.list_agents()
    assert any(a['name'] == "competitor_test" for a in agents)

if __name__ == "__main__":
    test_agent_registration()
    print("Agent Registry tests passed!")
