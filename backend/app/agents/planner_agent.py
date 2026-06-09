from typing import List, Dict, Any, TypedDict
from langgraph.graph import StateGraph, END
from app.services.nvidia_service import NvidiaService
import json

class PlannerState(TypedDict):
    vision: str
    goals: List[str]
    recommended_agents: List[str]
    clarification_questions: List[str]
    current_agent: str
    reports: Dict[str, Any]

class PlannerAgent:
    def __init__(self, api_key: str = None):
        self.name = "Planner Agent"
        self.description = "Chief Operating Officer. Coordinates all worker agents."
        self.nvidia = NvidiaService(api_key)

    async def analyze_vision(self, vision: str) -> Dict[str, Any]:
        system_prompt = """You are the Planner Agent for StartupOS. Your role is to analyze a founder's startup vision and extract structured information.
        You must identify goals, budget, constraints, founder skills, product vision, revenue targets, timeline, and target users.
        Also, recommend specialized worker agents from this list: competitor, product, budget, marketing, branding, technical, validation, growth, operations, research.
        Respond ONLY in JSON format."""

        user_prompt = f"Analyze this startup vision: {vision}"

        response_text = await self.nvidia.generate_response(system_prompt, user_prompt)
        try:
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            json_str = response_text[start_idx:end_idx]
            return json.loads(json_str)
        except Exception as e:
            return {"error": "Failed to analyze vision", "raw": response_text}

    def create_graph(self):
        workflow = StateGraph(PlannerState)

        def planner_node(state: PlannerState):
            # Logic to decide next agent or finish
            if not state.get("current_agent"):
                return {"current_agent": state["recommended_agents"][0]}
            return {"current_agent": END}

        workflow.add_node("planner", planner_node)
        workflow.set_entry_point("planner")
        workflow.add_edge("planner", END)

        return workflow.compile()
