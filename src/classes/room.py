import json
import game_utils

class Room:
    def __init__(self, name, narrative_file):
        self.name = name
        self.narrative = game_utils.load_narrative_data(narrative_file)
        self.events = []          

    def handle_event(self, event_name, player_inventory):
        event_function = self.events.get(event_name)
        event_data = self.narrative["events"][event_name]

        if event_function:
          outcome = event_function(player_inventory, event_data)
        if outcome:
            # ... (handle item acquisition if needed)
            if handle_item.
            next_location = handle_leads_to(outcome)
            return next_location
            return None
    
    def enter(self, game_state):
      print(self.narrative["description"])
'''
        while True:
            for event_name, event_data in self.narrative["events"].items():
                print(f"- {event_data.get('prompt', event_name)}")  # Display prompt or event name

            choice = input("What do you do? ").lower()

            if choice in self.events:  # Check if the choice matches a registered event
                next_location = self.handle_event(choice, game_state)
                if next_location:
                    return next_location # Return the next location if there is one
            else:
                print("Invalid choice.")
'''

