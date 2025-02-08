import json  # We'll use the json module to save data

class GameState:
    def __init__(self):
        self.player_inventory = []
        self.current_location = "start"  # Initial location
        self.progress_summary = ""
        # ... other game state variables

def save_game(game_state):
    save_data = {"inventory": game_state.player_inventory, "location": game_state.current_location, "progress": game_state.progress_summary}
    with open("save_game.json", "w") as f:
        json.dump(save_data, f)
    print("Game saved successfully!")
    return

def silly_flute(game_state):
    print("You pull out the flute and play a silly tune. Nothing seems to happen.")
    save_game(game_state)


def check_map(game_state):
    print(f"You pull out the map and take a look. Glowing words read {game_state.current_location}.")
    print(f"{game_state.progress_summary}")
    return

def check_inventory(game_state):
    print("You look in your bag and find:")
    for item in game_state.player_inventory:
        print(f"- {item}")
    return
'''   
def action(prompt, valid_choices):
    while True:
        choice = input(prompt).lower()
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice. Please choose from: {', '.join(valid_choices)}"
                  f"{prompt}")
'''
def evaluate_choice(player_choice, event_data, inventory=None):  # Add player_inventory as an optional parameter
    if player_choice in event_data:
        outcome = event_data[player_choice]
        if "requires_item" in outcome and inventory is not None:
            required_item = outcome["requires_item"]
            if required_item not in [item.name for item in player_inventory]:
                return outcome.get("failure", {"description": f"You need a {required_item} to do that."})  # Return failure outcome
        return outcome # Return the outcome
    return None

def handle_leads_to(outcome):
    if "leads_to" in outcome:
        return outcome["leads_to"]
    elif "leads_to_event" in outcome:
        return outcome["leads_to_event"]
    return None

def add_item_to_inventory(game_state, item):
    game_state.player_inventory.append(item)

def update_location(game_state, next_location):
    game_state.current_location = next_location

def update_progress_summary(game_state, progress_summary):
    game_state.progress_summary = progress_summary
