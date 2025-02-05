import json
import game_utils

class Room:
    def __init__(self, name, narrative_file):
        self.name = name
        self.narrative = game_utils.load_narrative_data(narrative_file)
        self.events = []          
        
    def enter(self, player_inventory):
        print(self.narrative["description"])

        while True:
            for event_name, event_data in self.narrative["events"].items():
                print(f"- {event_data.get('prompt', event_name)}")  # Display prompt or event name

            choice = input("What do you do? ").lower()

            if choice in self.events:  # Check if the choice matches a registered event
                next_location = self.handle_event(choice, player_inventory)
                if next_location:
                    return next_location # Return the next location if there is one
            else:
                print("Invalid choice.")

    def handle_event(self, event_name, player_inventory):
        event_function = self.events.get(event_name)
        event_data = self.narrative["events"][event_name]

        if event_function:
            outcome = event_function(player_inventory, event_data)  # Call the main event function
            while outcome: # Handle a chain of leads_to_event
                next_event = None
                if isinstance(outcome, dict): # Check if it is a dictionary like {"leads_to_event": "next_event"} or a simple {"leads_to": "next_room"}
                    next_event = handle_leads_to(outcome)
                    handle_item(outcome, player_inventory) # Handle item acquisition
                if next_event and next_event in self.narrative["events"]: # Check if leads_to_event exists
                    event_data = self.narrative["events"][next_event]
                    event_function = self.events.get(next_event)
                    outcome = event_function(player_inventory, event_data)
                elif isinstance(outcome, dict): # Check if it is a dictionary like {"leads_to": "next_room"}
                    next_event = handle_leads_to(outcome)
                outcome = next_event # Update the outcome
            return outcome # Return the final result