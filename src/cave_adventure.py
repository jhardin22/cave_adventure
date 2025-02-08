import json  # For save/load
from classes import branches # Import room modules
from game_utils import GameState



game_state = GameState()

def start_game(game_state):
    print("You stand at the entrance of a mysterious cave.")
    current_location = "start" # Set the current location
    # Check for save file
    try:
        with open("save_game.json", "r") as f:
            saved_data = json.load(f)
            game_state.player_inventory = saved_data["inventory"]
            game_state.current_location = saved_data["location"]
            game_state.progress_summary = saved_data["progress"]
            print("Game loaded successfully!")
            print(f"You are at the {game_state.current_location}.") # Tell the player where they are.
            print(f"{game_state.progress_summary}") 
    except FileNotFoundError:
        print("No save game found. Starting a new game.")
    while game_state.player_inventory != ["completed"]:
        if current_location == "start":
            branches.hub.handle_entrance(game_state)
        elif current_location == "dog_encounter":
            branches.hub.handle_dog(game_state)
        elif "red_rooms" in current_location:
            branches.red.red_room.enter(game_state)
        elif "blue_rooms" in current_location:
            branches.blue.blue_room.enter(game_state)
        elif "dark_rooms" in current_location:
            branches.dark.dark_room.enter(game_state)
    branches.hub.exit(game_state)
    # ... Add more locations and their corresponding functions   

start_game(game_state)  # Start the game!