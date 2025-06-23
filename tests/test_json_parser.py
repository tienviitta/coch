import subprocess
import os

def test_valid_json():
    file_path = os.path.join("data/json_parser/tests/step1", "valid.json")
    result = subprocess.run(["python", "src/json_parser.py", file_path], capture_output=True, text=True)
    assert result.returncode == 0, "Valid JSON test failed"

def test_invalid_json():
    file_path = os.path.join("data/json_parser/tests/step1", "invalid.json")
    result = subprocess.run(["python", "src/json_parser.py", file_path], capture_output=True, text=True)
    assert result.returncode == 1, "Invalid JSON test failed"
