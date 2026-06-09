from typing import List, Dict, Any
import json

def generate_master_report(project_name: str, vision: str, agent_reports: Dict[str, Dict[str, Any]]) -> str:
    report = f"# MASTER STARTUP REPORT: {project_name}\n\n"
    report += f"## Startup Vision\n{vision}\n\n"

    for agent_name, data in agent_reports.items():
        report += f"## {agent_name.capitalize()} Analysis\n"
        report += f"**Summary:** {data.get('summary', 'N/A')}\n\n"
        report += f"**Key Findings:**\n{data.get('findings', 'N/A')}\n\n"
        report += f"**Risks:**\n{data.get('risks', 'N/A')}\n\n"
        report += f"**Recommendations:**\n{data.get('recommendations', 'N/A')}\n\n"
        report += "---\n\n"

    report += "## 90-Day Roadmap\n"
    report += "1. Validate core assumptions (Days 1-30)\n"
    report += "2. Build MVP (Days 31-60)\n"
    report += "3. Early access launch (Days 61-90)\n"

    return report
