import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import json_parser


def test_valid_json():
    file_path = os.path.join("data/json_parser/tests/step1", "valid.json")
    result = json_parser.validate_json(file_path)
    assert result == 0, "Valid JSON test failed"


def test_invalid_json():
    file_path = os.path.join("data/json_parser/tests/step1", "invalid.json")
    result = json_parser.validate_json(file_path)
    assert result == 1, "Invalid JSON test failed"


def test_my_valid_json():
    file_path = os.path.join("data/json_parser/tests/step1", "valid.json")
    result = json_parser.my_validate_json(file_path)
    assert result == 0, "Valid JSON test failed for my_validate_json"


def test_my_invalid_json():
    file_path = os.path.join("data/json_parser/tests/step1", "invalid.json")
    result = json_parser.my_validate_json(file_path)
    assert result == 1, "Invalid JSON test failed for my_validate_json"
