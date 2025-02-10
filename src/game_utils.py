import json
import os

def load_narrative_data(filename):
    narrative_dir = os.path.join(os.path.dirname(__file__), "narrative")
    filepath = os.path.join(narrative_dir, f"{filename}.json") 
    print(f"file path: {filepath}")
    print(f"narrative dir: {narrative_dir}")
    try:
        with open(f"{filepath}.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename}.json not found at {filepath}")
        return {}