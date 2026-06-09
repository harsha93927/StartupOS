from app.agents.registry import agent_registry
from app.agents.competitor_agent import CompetitorAgent
from app.agents.product_agent import ProductAgent
from app.agents.budget_agent import BudgetAgent
from app.agents.marketing_agent import MarketingAgent

# Register agents
agent_registry.register("competitor", CompetitorAgent())
agent_registry.register("product", ProductAgent())
agent_registry.register("budget", BudgetAgent())
agent_registry.register("marketing", MarketingAgent())
