import json
import game_utils
from rooms import blue_room, red_room, dark_room 
from room import Room

hub = Room("Cave Entrance", "cave_entrance")

def handle_entrance(player_inventory, current_location, progress_summary):
    game_utils.check_map(progress_summary, current_location)
    game_utils.check_inventory(player_inventory)
    choice = game_utils.action( , )

    if choice.lower() == "deeper":
        enter(player_inventory, current_location, progress_summary)
    elif choice.lower() == "back":
        turn_back(player_inventory, current_location, progress_summary)
    elif choice.lower() == "save":
        game_utils.save_game(player_inventory, current_location, progress_summary)
        handle_entrance() # Return to the cave entrance options after saving


def enter(player_inventory, current_location, progress_summary):
    print("You bravely venture deeper into the cave...")
    print("As you go further, you begin to hear a faint melody.")
    current_location = "dog_encounter"  # Update the current location
    print("The sound grows louder, and you round a corner to see...")
    print("A large, fluffy white dog sitting on a rock, playing a flute!")
    print("The dog looks at you with intelligent eyes and continues to play.")

    choice = game_utils.action("Do you approach the dog (enter 'approach') or quietly observe from a distance (enter 'observe')?", ["approach", "observe"])

    if choice.lower() == "approach":
        three_doors_options(player_inventory, current_location, progress_summary)
    elif choice.lower() == "observe":
        turn_back(player_inventory, current_location, progress_summary)


def turn_back(player_inventory, current_location, progress_summary):
    if "ring" in player_inventory:
        print("You decide to turn back and leave the cave.")
        print("As you walk back, you feel the warmth of the ring on your finger.")
        print("Greif and loss fill you as you leave the cave. You can feel that something is missing forever.")
        game_utils.save_game(player_inventory, current_location, progress_summary)
        game_utils.action("Lost things can still be found. Press 'enter'", [""])
        exit()
    elif "crown" in player_inventory:
        print("")
        game_utils.save_game(player_inventory, current_location, progress_summary)
    elif player_inventory == ["completed"]:
        print("")
        game_utils.save_game(player_inventory, current_location, progress_summary)
    print("You wisely decide to turn back.")
    print("You make your way safely out of the cave.")
    print("You have escaped the cave's mysteries... for now.")


def approach_dog():
    print("You cautiously approach the dog, careful not to startle it.")
    print("As you get closer, the dog stops playing and wags its tail.")
    print("It seems friendly!")
    print(" 'Hello! I see you have decided to enter the cave. Would you like to pet me?\n"  
          "(enter 'pet') or ask me a question? (enter 'question')'") 
    
    choice = game_utils.action("Do you pet the dog (enter 'pet') or ask a question (enter 'question')? ", ["pet", "question"])

    if choice.lower() == "pet":
        #pet_dog()
    elif choice.lower() == "question":
        print("You ask the dog a question.")
        print(" 'How can you play the flute without fingers or lips?'")
        print("The Dog answers,") 
        print(" 'You're not even going to ask how I can talk?'")
        print(" 'I'm a magical dog, I can do anything I want. I'm here to help you on your journey.'")
        print(" 'I'll give you this bag of dog treats to get started...If you give me something first...(enter 'pet')'")
        approach_dog()

def observe_dog():
    print("You decide to observe the dog from a distance.")
    print("The dog continues to play its flute, the music echoing through the cave.")
    print("You enjoy the peaceful melody for a while, then decide to move on.")
    print("The dog continues to play its flute, seemingly lost in the music.")
    print("Do you approach (enter 'approach') or turn back (enter 'back')?")

    choice = game_utils.action("Do you approach the dog (enter 'approach') or turn back (enter 'back')? ", ["approach", "back"])
    
    if choice.lower() == "approach":
        approach_dog()
    elif choice.lower() == "back":
        turn_back()    

'''
TODO: refactor dog events to take the player_inventory, current_location, and progress_summary as parameters

def pet_dog():
    global player_inventory, progress_summary
    if "flute" in player_inventory:
        print("You reach out and pet the dog. His long hair starts to fly all around the cavern.")
        print(" 'Thanks! I love pets. If you're looking for advice, I'd start with the blue door.'") 
        dog_encounter()
    elif "ring" in player_inventory:
        print("You reach out and pet the dog. His long hair starts to fly all around the cavern.")
        print("The dog licks a stray tear off your face and asks,. \n"
              " 'Sometimes the only way out is through. What do you want to do?'")
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
    global player_inventory, current_location
    print("You cautiously approach the dog, careful not to startle it.")
    print("As you get closer, the dog stops playing and wags its tail.")
    print("It seems friendly!")
    print(" 'Hello! I see you have decided to enter the cave. Would you like to pet me?\n"  
          "(enter 'pet') or ask me a question? (enter 'question')'") 
    current_location = "dog_encounter"
    print(" 'There's a lot of mysteries in this cave. Now that you're here you might as well investigate.'")
    if "flute" in player_inventory:
        print("That flute has lots of uses. Try playing it if you're stuck.")
        three_doors_options()
    elif "ring" in player_inventory:
        print(" 'That ring looks shiny! I bet it's feels good to know you're not alone.'")
    elif "crown" in player_inventory:
        print("")
    else:
        print(" 'Take this flute. You look like you're good at music. Try playing it lots of places, just remember you can't unplay it either.'")
        player_inventory.append("flute")
        print("You toot on the flute. The air around you shimmers and starts to feel heavy.") 
    three_doors_options()
'''

def three_doors_options(player_inventory, current_location, progress_summary):
    print("A red (red) door, a blue (blue) door, and a dark (dark) path deeper into the cave appear.")

    choice = game_utils.action("You stand next to the dog in the cave entrance. Three paths lie before you:\n"
                  "1. A Red Door (enter 'red')\n"
                  "2. A Blue Door (enter 'blue')\n"
                  "3. A Dark Path (enter 'dark')\n"
                  "4. Pet the dog (enter 'pet')\n"
                  "5. Leave the cave (enter 'leave')\n"
                  "Which path do you choose, or do you wish to save (enter 'save')? ", ["red", "blue", "dark", "pet", "leave", "save"])
        
    if choice.lower() == "red":
        red_room.enter(player_inventory, progress_summary, current_location)
    elif choice.lower() == "blue":
        blue_room.enter(player_inventory, progress_summary, current_location)
    elif choice.lower() == "dark":
        dark_room.enter(player_inventory, progress_summary, current_location)
    elif choice.lower() == "pet":
        pet_dog()
    elif choice.lower() == "leave":
        turn_back(player_inventory, current_location, progress_summary)
    elif choice.lower() == "save":
        game_utils.save_game(player_inventory, current_location, progress_summary)
        three_doors_options()