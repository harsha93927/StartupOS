from app.agents.base import BaseWorkerAgent
from typing import Dict, Any
from app.services.nvidia_service import NvidiaService
import json

class CompetitorAgent(BaseWorkerAgent):
    def __init__(self, api_key: str = None):
        super().__init__(
            name="Competitor Agent",
            description="Analyzes competitors, pricing, strengths, and weaknesses."
        )
        self.nvidia = NvidiaService(api_key)

    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        system_prompt = """You are the Competitor Agent for StartupOS.
        Analyze the startup vision and any provided competitor data.
        Provide a report with SUMMARY, KEY FINDINGS, RISKS, OPPORTUNITIES, RECOMMENDATIONS, and NEXT ACTIONS.
        Respond ONLY in JSON format with these keys."""

        user_prompt = f"Startup Vision: {context.get('vision')}\nContext: {json.dumps(context)}"

        response_text = await self.nvidia.generate_response(system_prompt, user_prompt)
        try:
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            json_str = response_text[start_idx:end_idx]
            return json.loads(json_str)
        except Exception as e:
            return {"error": "Failed to run competitor analysis", "summary": response_text}
