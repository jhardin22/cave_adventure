import json
from game_state import GameState
from classes.room import Room


dog_room = Room("Dog Room", "dog_room", "adventure_start")

def handle_choose_door(event_data, game_state):
    print(event_data)
    print(game_state.current_room, game_state.player_inventory)

def handle_pet_dog(event_data, game_state):
    print(event_data)
    print(game_state.player_inventory)