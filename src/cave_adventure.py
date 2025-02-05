import json  # For save/load
from classes import rooms # Import room modules

player_inventory = []  # Player's inventory
current_location = "cave_entrance" # Keep track of where the player is
progress_summary = []  # Keep track of the player's progress

def start_game(player_inventory, current_location, progress_summary):
    print("You stand at the entrance of a mysterious cave.")
    current_location = "cave_entrance" # Set the current location
    # Check for save file
    try:
        with open("save_game.json", "r") as f:
            saved_data = json.load(f)
            player_inventory = saved_data["inventory"]
            current_location = saved_data["location"]
            progress_summary = saved_data["progress"]
            print("Game loaded successfully!")
            print(f"You are at the {current_location}.") # Tell the player where they are.
            print(f"{progress_summary}") 
    except FileNotFoundError:
        print("No save game found. Starting a new game.")
    while player_inventory != ["completed"]:
        if current_location == "cave_entrance":
            rooms.hub.handle_entrance(player_inventory, current_location, progress_summary)
        elif current_location == "dog_encounter":
            rooms.hub.handle_dog(player_inventory, current_location, progress_summary)
        elif "red_rooms" in current_location:
            rooms.red_room.enter(player_inventory, progress_summary, current_location)
        elif "blue_rooms" in current_location:
            rooms.blue_room.enter(player_inventory, progress_summary, current_location)
        elif "dark_rooms" in current_location:
            rooms.dark_room.enter(player_inventory, progress_summary, current_location)
    rooms.hub.turn_back()
    # ... Add more locations and their corresponding functions   

start_game()  # Start the game!