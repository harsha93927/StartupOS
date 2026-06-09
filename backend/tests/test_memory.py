import sys
import os
import shutil
import unittest

# Dynamic path adjustment for various environments
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app.memory.project_memory import ProjectMemory

class TestProjectMemory(unittest.TestCase):
    def setUp(self):
        self.test_dir = "/tmp/startupos_test_workspace"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        self.memory = ProjectMemory(self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_save_load_json(self):
        test_data = {"key": "value"}
        self.memory.save_json("test.json", test_data)
        loaded = self.memory.load_json("test.json")
        self.assertEqual(loaded, test_data)

    def test_save_report(self):
        content = "Hello World"
        self.memory.save_report("test_report.txt", content)
        report_path = os.path.join(self.test_dir, "reports/test_report.txt")
        self.assertTrue(os.path.exists(report_path))
        with open(report_path, 'r') as f:
            self.assertEqual(f.read(), content)

if __name__ == "__main__":
    unittest.main()
