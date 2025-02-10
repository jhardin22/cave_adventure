import game_utils


class Room:
    def __init__(self, name, filename, events):
        self.name = name
        self.narrative = game_utils.load_narrative_data(filename)
        self.events = {}
        self.locked_out = False          
        
    def enter(self, game_state):
        print(self.narrative.get("description", "You are in a room."))

        for event_name in self.narrative.get("events", {}):
            print(f"- {event_name}")

        choice = input("What do you choose to do?").lower()

        if choice in self.narrative.get("events", {}):
            event_data = self.narrative["events"][choice]
            return self.handle_event(choice, event_data, game_state)
        
        else:
            print("Invalid choice.")
            return None


    def handle_event(self, event_name, event_data, game_state):
        print(f"You chose: {event_name}")
        return None #Stay in the same room for now