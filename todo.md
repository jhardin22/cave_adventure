1. Implement classes
    -Door
        -self
        -locked
        -key
        -destination, maybe sides?
        -description
        -narrative        
    -Room
        -self
        -name
        -description
        -doors
        -items
        -characters
        -narrative
    -Item
        -self
        -name
        -description
        -use
        -useDescription
        -isEquippable
        -isEquipped
    -Character
        -self
        -name
        -gender
        -description
        -inventory
2. Narrative
    -Create a narrative for the game
        Overview:
            The overall narrative focuses on the player moving through the cave
            The player will enter the cave and start to explore. The cave is a 
            metaphor for the player's mind and/or relationships. The story has
            three basic parts, the red-line, the blue-line, and the dark-line. The hub for the story is a cave with a talking dog and three doors colored respective to the story line.
        Blue-line:
            The blue-line introduces the player's spouse, and the two fall in love
            in a very mysterious and indisticnt way. The idea is that there's a 
            mysterious force within the cave that causes them to fall in love, 
            even though there's no totally apparent reason why they should. The
            cave is a trap for the spouse and he can't get out because he is cursed. The cave is a magical and powerful place and agreeing to marry is binding. The player gets a wedding band as an item, but the curse separates them and sends the player back to the hub. The player can't get back through the door, and has to find a way to break the curse, or leave them behind in the cave.
            1st path: sit and answer the proposal
            2nd path: talk and accept the ring
        Red-line:
            The red-line shows us the cave, and lets us experience some of the things about the cave's nature. The cave presses feelings on the player. Sometimes those feelings are welcome, some times they aren't. Sometimes even against the player's will. There are a lot of mirrors behind the red door, and they will show things about the player and about the people. Some of these things will be true, and some of them will be lies. In here, the player will have to examine themselves and find two crowns. One crown gives light and provides hope that things aren't limited to the way they are in the cave. The other crown can break the spouse's curse, but doesn't open the way back to them.
        Dark-line:
            The dark line is an unknown place full of potential. There are opportunities there. Some of these are worth leaving the cave with. There is a lot of hidden value in the dark, but ultimately these things are all distractions. The true prize in the dark is the book. This book opens the way back to the spouse and provides a chance to remember how he got lost and why he is cursed. Because we know how he got lost we'll be able to open the blue door and find him. The cave will still give feelings, but the ability to intentionally set a goal is what will allow the couple to leave.
    -Create a narrative for each room
    -Create a narrative for each item
    -Create a narrative for each character
3.  update game_utils to call correct endpoint on loads for each room
4.  Make maps