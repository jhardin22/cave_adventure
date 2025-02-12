from classes.rooms import dog_room
from game_state import GameState
import classes.item
import game_utils


game_state = GameState() # Start
game_state.current_room = "dog_room"
game_state.player_inventory = []
game_state.progress_summary = ""

def turn_back(game_state):
    if "ring" in game_state.player_inventory:
        print("You decide to turn back and leave the cave.")
        print("As you walk back, you feel the warmth of the ring on your finger.")
        print("Greif and loss fill you as you leave the cave. You can feel that something is missing forever.")
        game_utils.save_game(game_state)
        game_utils.action("Lost things can still be found. Press 'enter'", [""])
        exit()
    elif "crown" in game_state.player_inventory:
        print("")
        game_utils.save_game(game_state)
    elif "book" in game_state.player_inventory:
        print("")
        game_utils.save_game(game_state)
    print("You wisely decide to turn back.")
    print("You make your way safely out of the cave.")
    print("You have escaped the cave's mysteries... for now.")

#Game Loop
while True:
    current_room = game_state.current_room
    next_room = current_room.enter(game_state)

    if next_room:
        game_state.current_room = next_room
        print(f"You are now in the {game_state.current_room}.")
        break
    elif game_state.current_room is "turn_back":
        turn_back(game_state)
            
    else:
        print("Nothing more to do here.")
        break

