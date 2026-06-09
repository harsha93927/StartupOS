from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseWorkerAgent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def format_report(self, data: Dict[str, Any]) -> str:
        report = f"SUMMARY\n{data.get('summary', 'No summary provided')}\n\n"
        report += f"KEY FINDINGS\n{data.get('findings', 'No findings provided')}\n\n"
        report += f"RISKS\n{data.get('risks', 'No risks provided')}\n\n"
        report += f"OPPORTUNITIES\n{data.get('opportunities', 'No opportunities provided')}\n\n"
        report += f"RECOMMENDATIONS\n{data.get('recommendations', 'No recommendations provided')}\n\n"
        report += f"NEXT ACTIONS\n{data.get('next_actions', 'No next actions provided')}\n"
        return report
