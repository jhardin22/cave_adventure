from classes.room import Room
from classes.game_state import GameState
import classes.item

game_state = GameState()
game_state.current_room = "hub"
game_state.player_inventory = []
game_state.progress_summary = ""

hub = Room("Hub", "hub", "adventure_start")

#Game Loop
while True:
    current_room = hub
    next_location = current_room.enter(game_state)

    if next_location:
        game_state.current_room = next_location
        print(f"You are now in the {game_state.current_room}.")
        break
    else:
        print("Nothing more to do here.")
        break