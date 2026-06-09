import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from typing import List, Dict, Any

class NvidiaService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("NVIDIA_API_KEY")
        # Do not raise error on init to allow registry to load without key
        self._llm = None

    @property
    def llm(self):
        if not self._llm:
            if not self.api_key:
                 raise ValueError("NVIDIA_API_KEY is not set")
            self._llm = ChatNVIDIA(model="nvidia/llama-3.1-405b-instruct", nvidia_api_key=self.api_key)
        return self._llm

    async def generate_response(self, system_prompt: str, user_prompt: str) -> str:
        messages = [
            ("system", system_prompt),
            ("user", user_prompt),
        ]
        response = await self.llm.ainvoke(messages)
        return response.content
