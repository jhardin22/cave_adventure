class GameState:
    def __init__(self):
        self.current_room = None
        self.player_inventory = []
        self.progress_summary = ""
        self.barred = False
        self.entered_from_other_room = False