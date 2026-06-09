from app.agents.base import BaseWorkerAgent
from typing import Dict, Any
from app.services.nvidia_service import NvidiaService
import json

class MarketingAgent(BaseWorkerAgent):
    def __init__(self, api_key: str = None):
        super().__init__(
            name="Marketing Agent",
            description="Plans launch, acquisition, and content strategy."
        )
        self.nvidia = NvidiaService(api_key)

    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        system_prompt = "You are the Marketing Agent for StartupOS. Provide a marketing plan in JSON format."
        user_prompt = f"Vision: {context.get('vision')}"
        response_text = await self.nvidia.generate_response(system_prompt, user_prompt)
        try:
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            return json.loads(response_text[start_idx:end_idx])
        except:
            return {"summary": response_text}
