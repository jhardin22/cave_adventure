from game_utils import save_game  # Import the save_game function in room module
from game_utils import silly_flute  # Import the silly_flute function in room module
from classes.room import Room  # Import the Room class from classes module
import game_state

# Load the JSON narrative data (outside any functions) - This is key!
try:
    with open("narrative/blue_room_events.json", "r") as f:
        blue_room_data = json.load(f)
except FileNotFoundError:
    print("Error: blue_room.json not found!")
    blue_room_data = {}  # Provide an empty dictionary to prevent errors

blue_room = Room("Blue Room", "blue_room")

while "ring" in player_inventory:

blue_room.enter(player_inventory, current_location, progress_summary):
        return current_location

    
def blue_room_options():
        global player_inventory, current_location, progress_summary
        print("A man sits at a desk in the room, writing in a book. He looks up as you enter and smiles. Hope and excitement inexplicably swell again. \n"
              " 'Wow, I've been here for ages. It's good to see you. I've been alone for a long time. Would you like to sit with me?' \n")
        choice = input("Do you sit? \n"
                        "1. Sit (enter 'sit') \n"
                        "2. Play Flute (enter 'flute') \n"
                        "3. Keep talking (enter 'talk') \n"
                        "4. Save (enter 'save') \n")
        if choice.lower() == "flute":
            ###
        elif choice.lower() == "sit":
            print("You sit down and start talking to the man. He tells you about his life and how he came to be in the room. \n"
                  "As the two of you talk the feeling of hope and excitement ebbs and flows. Something inside of you is drawn to \n"
                  "the man and the room. You feel like you could stay here forever. Nothing about the man seems special, but a bond \n"
                  "forms between you. \n"
                  " 'Will you marry me?' \n" "The question comes out of nowhere. You're not sure how to respond at first, but the longer \n"
                  "with the question the more certain you become. \n")
            choice = input("Do you say yes? (enter 'yes') or no? (enter 'no') \n")
            if choice.lower() == "yes":
                blue_bedroom()
                
def blue_bedroom(game_state):
    print("You say yes! \n" "Tears fill your eyes and the eyes of the man. The two of you get up from the table and hold handsx \n"
                      "You walk to a bed in the corner of the room, sheltered by a screen... \n"
                      "As the two of you sit together, the feeling of hope and excitement has given way to satisfaction and contentment. \n"
                      "The man leans in and kisses you. \n"
                      " 'I love you. Thank you for loving me. I'm trapped here, but take this so we can be together and remember each other.' \n"
                      "The man holds out his hand and shows you two rings. As you reach out to touch them, he takes your left hand and puts a \n" 
                      "small thin band on your ring finger. \n")
    game_state.player_inventory.append("ring")
    print(" 'Would you play me a song?' \n You pull out the flute and play a joyful tune.") 
    print("Music fills the room, and the lights seem to grow brighter. After you finish the song, you reach down and put the other ring on the hand of the man. \n"
                      "You promise your undying love to him. As the ring slips over his last knuckle, the room starts to fade. \n"
                      "You hold on to the headboard of the bed, but a feeling of grief and loss washes over you, as the room fades to black. \n"
                      "Something warm and wet rubs across your face. You open your eyes to see the dog licking your face. \n"
                      " 'You're awake! I was worried you'd never wake up. You've been out for a while.' \n")
    game_state.progress_summary.append("You found, and lost the love of your life.")
