from flask import Flask, render_template, request, session
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Important for sessions (replace with a random string)

# Initialize game state in the session
@app.route("/", methods=["GET", "POST"])
def game():
    if "game_state" not in session:  # New game
        session["game_state"] = {
            "player_inventory": [],
            "current_location": "cave_entrance",
            "output": ["You stand at the entrance of a mysterious cave."], # Start with initial output
        }
        # Load saved game if it exists
        try:
            with open("save_game.json", "r") as f:
                saved_data = json.load(f)
                session["game_state"]["player_inventory"] = saved_data["inventory"]
                session["game_state"]["current_location"] = saved_data["location"]
                session["game_state"]["output"].append("Game loaded successfully!")
        except FileNotFoundError:
            pass  # No save game found, continue with new game

    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            session["game_state"]["output"].append("> " + user_input) # Echo the user input
            process_input(user_input) # Process the input and update the game state
    return render_template("game.html", game_state=session["game_state"])


def process_input(user_input):
    # ... (Put your game logic here, taking user_input and updating session["game_state"])
    # Example:
    if session["game_state"]["current_location"] == "cave_entrance":
        if user_input.lower() == "deeper":
            session["game_state"]["current_location"] = "dog_encounter"
            session["game_state"]["output"].append("You bravely venture deeper...") # Add to output
        # ... other cave entrance logic
    # ... (rest of your game logic)

@app.route("/save", methods=["POST"])
def save_game():
    save_data = {"inventory": session["game_state"]["player_inventory"], "location": session["game_state"]["current_location"]}
    with open("save_game.json", "w") as f:
        json.dump(save_data, f)
    session["game_state"]["output"].append("Game saved!")
    return "Game saved" # Simple response for the AJAX call

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) # host="0.0.0.0" makes it accessible in Docker