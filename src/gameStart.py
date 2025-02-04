import json  # We'll use the json module to save data
##todo - abstract rooms into modules
from rooms import red_door_room, blue_door_room, dark_path # Import the room modules


player_inventory = []  # Player's inventory
current_location = "cave_entrance" # Keep track of where the player is
progress_summary = []  # Keep track of the player's progress

def start_game():
    global current_location  # Access the global current_location
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

    show_options() # Display the correct options for the current location

def game_loop():  ##Todo refactor to use flask
    if current_location == "cave_entrance":
        cave_entrance_options()
    elif current_location == "dog_encounter":
        dog_encounter()
    elif current_location == "red_room":
        red_rooms.transit_door(player_inventory, progress_summary, current_location)
    elif current_location == "blue_room":
        blue_rooms.transit_door(player_inventory, progress_summary, current_location)
    elif current_location == "dark_path":
        dark_path_options()
    # ... Add more locations and their corresponding functions

def cave_entrance_options():
    choice = input("Do you venture deeper into the cave (enter 'deeper') or turn back (enter 'back') or save (enter 'save')? ")

    if choice.lower() == "deeper":
        go_deeper()
    elif choice.lower() == "back":
        turn_back()
    elif choice.lower() == "save":
        save_game()
        cave_entrance_options() # Return to the cave entrance options after saving
    else:
        print("Invalid choice. Please enter 'deeper', 'back', or 'save'.")
        cave_entrance_options()

def go_deeper():
    global current_location
    print("You bravely venture deeper into the cave...")
    print("As you go further, you begin to hear a faint melody.")
    current_location = "dog_encounter"  # Update the current location
    print("The sound grows louder, and you round a corner to see...")
    print("A large, fluffy white dog sitting on a rock, playing a flute!")
    print("The dog looks at you with intelligent eyes and continues to play.")

    choice = input("Do you approach the dog (enter 'approach') or quietly observe from a distance (enter 'observe')? ")

    if choice.lower() == "approach":
        approach_dog()
    elif choice.lower() == "observe":
        observe_dog()
    else:
        print("Invalid choice. Please enter 'approach' or 'observe'.")
        go_deeper()  # Ask the question again

def turn_back():
    if "ring" in player_inventory:
        print("You decide to turn back and leave the cave.")
        print("As you walk back, you feel the warmth of the ring on your finger.")
        print("Greif and loss fill you as you leave the cave. You can feel that something is missing forever.")
        exit()
    print("You wisely decide to turn back.")
    print("You make your way safely out of the cave.")
    print("You have escaped the cave's mysteries... for now.")
    exit()

def approach_dog():
    print("You cautiously approach the dog, careful not to startle it.")
    print("As you get closer, the dog stops playing and wags its tail.")
    print("It seems friendly!")
    print(" 'Hello! I see you have decided to enter the cave. Would you like to pet me?\n"  
          "(enter 'pet') or ask me a question? (enter 'question')'") 
    
    choice = input("Do you pet the dog (enter 'pet') or ask a question (enter 'question')? ")

    if choice.lower() == "pet":
        pet_dog()
    elif choice.lower() == "question":
        print("You ask the dog a question.")
        print(" 'How can you play the flute without fingers or lips?'")
        print("The Dog answers,") 
        print(" 'You're not even going to ask how I can talk?'")
        print(" 'I'm a magical dog, I can do anything I want. I'm here to help you on your journey.'")
        print(" 'I'll give you this bag of dog treats to get started...If you give me something first...(enter 'pet')'")
        approach_dog()
    else:
        print("Invalid choice. Please enter 'pet' or 'question'.")
        approach_dog()  # Ask the question again

def observe_dog():
    print("You decide to observe the dog from a distance.")
    print("The dog continues to play its flute, the music echoing through the cave.")
    print("You enjoy the peaceful melody for a while, then decide to move on.")
    print("The dog continues to play its flute, seemingly lost in the music.")
    print("Do you approach (enter 'approach') or turn back (enter 'back')?")

    choice = input("Do you approach the dog (enter 'approach') or turn back (enter 'back')? ")
    
    if choice.lower() == "approach":
        approach_dog()
    elif choice.lower() == "back":
        turn_back()    
    else:
        print("Invalid choice. Please enter 'approach' or 'back'.")
        observe_dog()  # Ask the question again

def pet_dog():
    global player_inventory, progress_summary
    if "flute" in player_inventory:
        print("You reach out and pet the dog. His long hair starts to fly all around the cavern.")
        print(" 'Thanks! I love pets. If you're looking for advice, I'd start with the blue door.'") 
        dog_encounter()
    print("You reach out and pet the dog. His long hair starts to fly all around the cavern.")
    print(" 'Thanks! I love pets. Since you're so nice, I'll give you this bag to get started'")
    player_inventory.append("dog treats")
    player_inventory.append("bag")
    print(player_inventory)
    print("You receive a bag of dog treats. The dog wags its tail happily.")
    progress_summary.append("You made friends with Murphy")
    dog_encounter()

def dog_encounter():
    global player_inventory, progress_summary, current_location
    current_location = "dog_encounter"
    print(" 'There's a lot of mysteries in this cave. Now that you're here you might as well investigate.'")
    if "flute" in player_inventory:
        print("That flute has lots of uses. Try playing it if you're stuck.")
        three_doors_options()
    else:
        print(" 'Take this flute. You look like you're good at music. Try playing it lots of places, just remember you can't unplay it either.'")
        player_inventory.append("flute")
        print("You toot on the flute. The air around you shimmers and starts to feel heavy.")
    if "ring" in player_inventory:
        print(" 'That ring looks shiny! I bet it's feels good to know you're not alone.'")
    if "crown" in player_inventory:
        print("")
    three_doors_options()

def three_doors_options():
    print("A red (red) door, a blue (blue) door, and a dark (dark) path deeper into the cave appear.")

    choice = input("You stand next to the dog in the cave entrance. Three paths lie before you:\n"
                  "1. A Red Door (enter 'red')\n"
                  "2. A Blue Door (enter 'blue')\n"
                  "3. A Dark Path (enter 'dark')\n"
                  "4. Pet the dog (enter 'pet')\n"
                  if "ring" in player_inventory:
                      "5. Leave the cave (enter 'leave')\n"
                  "Which path do you choose, or do you wish to save (enter 'save')? ")
        
    if choice.lower() == "red":
        red_door_options()
    elif choice.lower() == "blue":
        blue_room.transit_door(player_inventory, progress_summary)
    elif choice.lower() == "dark":
        dark_path_options()
    elif choice.lower() == "pet":
        pet_dog()
    elif choice.lower() == "leave":
        turn_back()    

def silly_flute():
    print("You pull out the flute and play a silly tune. Nothing seems to happen.")
    save_game()

def save_game():
    global player_inventory, current_location, progress_summary
    save_data = {"inventory": player_inventory, "location": current_location, "progress": progress_summary}
    with open("save_game.json", "w") as f:
        json.dump(save_data, f)
    print("Game saved successfully!")
    show_options()  # Show the options again after saving
    ##todo add "save" and "inventory" to event options

start_game()  # Start the game!