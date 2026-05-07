import json

def parse_json(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
        return None
    finally:
        print("Execution complete.")

# Test
print(parse_json('{"name": "John", "age": 30}'))  # {'name': 'John', 'age': 30}
print(parse_json('Invalid JSON'))  # None