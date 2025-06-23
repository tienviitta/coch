import json
import argparse
import re


def validate_json(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            json.loads(content)  # Attempt to parse the JSON
        print("Valid JSON")
        return 0  # Return code 0 for valid JSON
    except json.JSONDecodeError:
        print("Invalid JSON")
        return 1  # Return code 1 for invalid JSON


def my_validate_json(file_path):
    stack = []
    with open(file_path, "r") as file:
        while True:
            char = file.read(1)
            if not char:
                break
            if char == "{" or char == "}":
                stack.append(char)
    if len(stack) == 0 or len(stack) % 2 != 0:
        return 1  # Return 1 for invalid JSON
    count = 0
    for char in stack:
        if char == "}":
            count += 1
        if char == "{":
            count -= 1
    return 0 if count == 0 else 1  # Return 0 for valid JSON, 1 for invalid JSON


def main():
    parser = argparse.ArgumentParser(description="Validate JSON files.")
    parser.add_argument("file_path", help="Path to the JSON file to validate.")
    args = parser.parse_args()

    file_path = args.file_path
    validate_json(file_path)


if __name__ == "__main__":
    main()
