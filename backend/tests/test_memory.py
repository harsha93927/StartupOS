import sys
import os
import shutil
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from app.memory.project_memory import ProjectMemory

def test_project_memory():
    test_dir = "/tmp/startupos_test_workspace"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

    memory = ProjectMemory(test_dir)
    test_data = {"key": "value"}
    memory.save_json("test.json", test_data)

    loaded = memory.load_json("test.json")
    assert loaded == test_data

    memory.save_report("test_report.txt", "Hello World")
    report_path = os.path.join(test_dir, "reports/test_report.txt")
    assert os.path.exists(report_path)
    with open(report_path, 'r') as f:
        assert f.read() == "Hello World"

    shutil.rmtree(test_dir)

if __name__ == "__main__":
    try:
        test_project_memory()
        print("Project Memory tests passed!")
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
