import sys
import json

def validate_json(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            json.loads(content)  # Attempt to parse the JSON
        print("Valid JSON")
        sys.exit(0)  # Exit with code 0 for valid JSON
    except json.JSONDecodeError:
        print("Invalid JSON")
        sys.exit(1)  # Exit with code 1 for invalid JSON

def main():
    if len(sys.argv) != 2:
        print("Usage: python json_parser.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    validate_json(file_path)

if __name__ == "__main__":
    main()
