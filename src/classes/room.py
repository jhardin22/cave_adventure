import game_utils
from classes.item import Item


class Room:
    def __init__(self, name, filename, events):
        self.name = name
        self.narrative = game_utils.load_narrative_data(filename)
        self.events = {}
        self.locked_out = False          
        
    def enter(self, game_state):
        current_event = self.narrative.get("entry")

        while current_event:
            print(current_event["prompt"])

            if "options" in current_event:  # Branching point
                for choice, next_event_name in current_event["options"].items():
                    print(f"- {choice}")

                choice = input("What do you do? ").lower()
                next_event = self.narrative["events"].get(current_event["options"].get(choice)) # Get the next event
                if next_event:
                    current_event = next_event # Change the current event
                else:
                    print("Invalid choice.")
                    continue # Go back to the prompt
            elif "leads_to" in current_event: # Leads to a room
                return current_event["leads_to"]
            else: # Regular event
                print(current_event.get("description", "Nothing happens."))
                # Handle item acquisition, etc.
                current_event = None # End the current path, but allow other options


    def handle_event(self, event_name, event_data, game_state):
        print(event_data.get("description", "Nothing happens."))

        if "item" in event_data:
            item_data = event_data["item"]
            new_item = Item(item_data["name"], item_data["description"], item_data["color"])
            game_state.player_inventory.append(new_item)
            print(f"You got {item_data['name']}!")

        if "leads_to_event" in event_data:
            next_event_name = event_data["leads_to_event"]
            next_event_data = self.narrative["events"].get(next_event_name)
            if next_event_data: #check to see if the event exists
                return self.handle_event(next_event_name, next_event_data, game_state)
            else:
                print(f"Warning: Next event '{next_event_name}' not found!")
                return None
        elif "leads_to" in event_data:
            return event_data["leads_to"]

        return None #Stay in the same room for now