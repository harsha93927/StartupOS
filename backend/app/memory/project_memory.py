import json
import os
from typing import Any, Dict

class ProjectMemory:
    def __init__(self, workspace_path: str):
        self.workspace_path = workspace_path
        if not os.path.exists(self.workspace_path):
            os.makedirs(self.workspace_path)

    def _get_path(self, filename: str) -> str:
        return os.path.join(self.workspace_path, filename)

    def save_json(self, filename: str, data: Dict[str, Any]):
        path = self._get_path(filename)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)

    def load_json(self, filename: str) -> Dict[str, Any]:
        path = self._get_path(filename)
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as f:
            return json.load(f)

    def save_report(self, filename: str, content: str):
        reports_dir = os.path.join(self.workspace_path, "reports")
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        path = os.path.join(reports_dir, filename)
        with open(path, 'w') as f:
            f.write(content)
