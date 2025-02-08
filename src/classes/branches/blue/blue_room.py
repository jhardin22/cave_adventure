import json
import game_utils
import rooms.hub
import blue_bedroom
from classes import Room

game_utils.load_narrative_data("blue_room")

blue_room = Room("Blue Room", "blue_room")

def handle_man_in_room(game_state):
  outcome = game_utils.evaluate_choice(game_state, event_data["outcome"])