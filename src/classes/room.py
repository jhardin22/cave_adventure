import game_utils
from classes.item import Item


class Room:
    def __init__(self, name, filename, events):
        self.name = name
        self.narrative = game_utils.load_narrative_data(filename)
        self.events = {}
        self.locked_out = False          
        
    def enter(self, game_state):
        print(self.narrative.get("description", "You are in a room."))

        initial_event_name = self.narrative.get("initial_event")
        if initial_event_name:
            initial_event_data = self.narrative["events"].get(initial_event_name)
            if initial_event_data:
                outcome = self.handle_event(initial_event_name, initial_event_data, game_state)
                if outcome:
                    return outcome  # Handle room change if needed

        while True:  # Persistent event loop (only after initial events are done)
            # Display ONLY persistent events
            for event_name, event_data in self.narrative.get("persistent_events", {}).items():
                print(f"- {event_data['prompt']}")

            choice = input("What do you do? ").lower()

            if choice in self.narrative.get("persistent_events", {}):
                event_name = choice
                event_data = self.narrative["persistent_events"][event_name]
                self.handle_persistent_event(event_data, game_state)

            elif choice == "quit":
                game_state.player_quit = True
                print("Thanks for playing!")
                return "quit"

            else:
                print("Invalid choice.")


    def handle_event(self, event_name, event_data, game_state):
    # ... (dialogue and description printing - same as before)

        if "options" in event_data:  # Choice point
            for choice, next_event_name in event_data["options"].items():
                print(f"- {choice}")  # Show the choices for THIS event

            choice = input("What do you do? ").lower()

            if choice in event_data["options"]:
                next_event_name = event_data["options"][choice]
                next_event = self.narrative["events"].get(next_event_name)
                if next_event:
                    return self.handle_event(next_event_name, next_event, game_state)  # Recurse
                else:
                    print("Invalid choice.")
                    return None
            elif choice == "quit":
                game_state.player_quit = True
                print("Thanks for playing!")
                return "quit"
            else:
                print("Invalid choice.")
                return None

        elif "leads_to_event" in event_data:  # Automatic transition
            next_event_name = event_data["leads_to_event"]
            next_event = self.narrative["events"].get(next_event_name)
            if next_event:
                return self.handle_event(next_event_name, next_event, game_state)  # Recurse
            else:
                print(f"Warning: Next event '{next_event_name}' not found.")
                return None
        elif "leads_to" in event_data:
            return event_data["leads_to"]
        elif "item" in event_data:
            # Handle item acquisition (if any)
            item_data = event_data["item"]
            new_item = Item(item_data["name"], item_data["description"])
            game_state.player_inventory.append(new_item)
            print(f"You found a {item_data['name']}!")
            return None  # No transition

        return None