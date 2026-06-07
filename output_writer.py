import json


def write_json(result, filename="compiler_output.json"):
    with open(filename, "w") as f:
        json.dump(result, f, indent=4)
