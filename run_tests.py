import os
import subprocess
import unittest

def run_tests():
    test_dir = "data/json_parser/tests/step1"
    test_files = ["valid.json", "invalid.json"]

    for test_file in test_files:
        file_path = os.path.join(test_dir, test_file)
        print(f"Testing {file_path}...")

        result = subprocess.run(["python", "src/json_parser.py", file_path], capture_output=True, text=True)
        print("STDERR:", result.stderr)  # Print stderr for debugging

        if test_file.startswith("valid"):
            assert result.returncode == 0, f"Failed: {file_path} should be valid"
            print("Passed: Valid JSON")
        else:
            assert result.returncode == 1, f"Failed: {file_path} should be invalid"
            print("Passed: Invalid JSON")

if __name__ == "__main__":
    run_tests()
    unittest.TextTestRunner().run(unittest.defaultTestLoader.discover("tests"))
