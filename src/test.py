# test.py
import os
import json

filepath = "c:/Users/jonathonhardin-nc/Desktop/Projects/Python/cave_adventure/src/narrative/hub.json"  # Absolute path for testing

print("Filepath:", filepath)
print("File Exists:", os.path.exists(filepath))

try:
    with open(filepath, "r") as f:
        data = json.load(f)
        print("JSON loaded successfully:", data)
except FileNotFoundError:
    print("File not found!")
except json.JSONDecodeError:
    print("Invalid JSON format!") # Check for JSON errors
except Exception as e:
    print(f"An error occurred: {e}")  # Catch other errors