import argparse
from dataclasses import dataclass
import sys


def validate_json_step1(file_path):
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


def validate_json(file_path):
    with open(file_path, "r") as file:
        while True:
            char = file.read(1)
            if not char:
                break
    return 0  # Return 0 for valid JSON, 1 for invalid JSON


@dataclass
class JsonParserState:
    in_obj: bool = False
    in_key: bool = False
    in_val: bool = False
    in_str: bool = False


class JsonParser:
    def __init__(self, fn):
        self.fn = fn
        self.st = JsonParserState()
        self.objs = {}

    def run(self):
        json_str = ""
        with open(self.fn, "r") as file:
            while True:
                # Read and process the JSON file character by character
                char = file.read(1)
                if not char:
                    break
                # State machine for basic JSON validation (braces, brackets, quotes)
                if char == "{":
                    self.st.in_obj = True
                    self.st.in_key = True
                elif char == '"' and self.st.in_obj:
                    if self.st.in_val:
                        value = json_str
                        json_str = ""
                    self.st.in_str = not self.st.in_str
                elif char == ":" and self.st.in_key:
                    key = json_str
                    json_str = ""
                    self.st.in_key = False
                    self.st.in_val = True
                elif char == "}" and self.st.in_obj and len(key) > 0:
                    if value.isnumeric():
                        value = float(value)
                    self.objs[key] = value
                    self.st.in_obj = False
                    self.st.in_val = False
                elif char == "," and self.st.in_obj and len(key) > 0:
                    if value.isnumeric():
                        value = float(value)
                    self.objs[key] = value
                    self.st.in_key = True
                    self.st.in_val = False
                elif self.st.in_str:
                    json_str += char
                # print(f"{char:2}: {self.st}")
        print(f"State: {self.st}")
        valid = (
            not self.st.in_obj
            and not self.st.in_key
            and not self.st.in_val
            and not self.st.in_str
        )
        return valid


def main():
    # Parse CLI arguments
    parser = argparse.ArgumentParser(description="Validate JSON files.")
    parser.add_argument("fn", help="JSON file")
    args = parser.parse_args()
    print(f"Validating JSON file: {args.fn}")
    json_parser = JsonParser(args.fn)
    valid = json_parser.run()
    print(f"Valid: {valid}, Parsed JSON objects: {json_parser.objs}")
    sys.exit(valid)


if __name__ == "__main__":
    main()
