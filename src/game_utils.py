import json
import os

def load_narrative_data(filename):
    # Construct path RELATIVE TO THE LOCATION OF game_utils.py
    script_dir = os.path.dirname(os.path.abspath(__file__)) # Get the absolute path of the script
    narrative_dir = os.path.join(script_dir, "narrative") # Go up one level and into narrative
    filepath = os.path.join(narrative_dir, f"{filename}.json")

    print("Trying to open:", filepath)
    print("File Exists:", os.path.exists(filepath))
    print("CWD:", os.getcwd())

    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found at: {filepath}")
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON format!")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    
def save_game(game_state, filename="savegame.json"):  # Default filename
    try:
        with open(filename, "w") as f:
            json.dump(game_state.__dict__, f, indent=4)  # Save the game_state dictionary
            print(f"Game saved to {filename}")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game(filename="savegame.json"):
    try:
        with open(filename, "r") as f:
            game_state_data = json.load(f)  # Load the dictionary
            game_state = GameState() # Create a new GameState object
            game_state.__dict__.update(game_state_data) # Update the object's dictionary with loaded data
            print(f"Game loaded from {filename}")
            return game_state
    except FileNotFoundError:
        print(f"No save game found at {filename}")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON format in save file")
        return None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None