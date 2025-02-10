import json  # We'll use the json module to save data

def save_game(player_inventory, current_location, progress_summary):
    save_data = {"inventory": player_inventory, "location": current_location, "progress": progress_summary}
    with open("save_game.json", "w") as f:
        json.dump(save_data, f)
    print("Game saved successfully!")
    return

def silly_flute():
    print("You pull out the flute and play a silly tune. Nothing seems to happen.")
    save_game()


def check_map(progress_summary, current_location):
    print(f"You pull out the map and take a look. Glowing words read {current_location}.")
    print(f"{progress_summary}")
    return

def check_inventory(player_inventory):
    print("You look in your bag and find:")
    for item in player_inventory:
        print(f"- {item}")
    return
   
def action(prompt, valid_choices):
    while True:
        choice = input(prompt).lower()
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice. Please choose from: {', '.join(valid_choices)} \n"
                  f"{prompt}")