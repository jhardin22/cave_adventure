import json
import game_utils
import rooms.hub
from classes import Room

game_utils.load_narrative_data("blue_room")

blue_room = Room("Blue Room", "blue_room")

blue_room.enter(player_inventory, current_location, progress_summary)
