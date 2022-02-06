# Tic Tac Toe

### Desctiption:
Tic Tac Toe is a turn based game for 2 players. This application offers multiple
ways of enjoying this timeless masterpiece. You can play on boards of various sizes with your friend or against a computer. To play start the main.py file.

### Navigating menu:
To navigate the menu use keys q, w, e, r and t to select options 1, 2, 3, 4 and 5.

### How to play:
<p>
To place your symbol onto the board you have to write coordinates of the tile where you want to place it. Coordinates are written in the following format: [X Y] (without the brackets). If you want to return to menu type 'quit'.
</p>
In a game for 2 the players are taking turns. In a game against the AI, the player is taking turns with a computer.

### Chosen Algorithm:
The algorithm of choice was the [minimax algorithm](https://en.wikipedia.org/wiki/Minimax) with [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

### Alternative solutions:
The program could be improved greatly by implementing better scoring system for the minimax algorithm, for example different winning positions could be valued higher based on how fast they lead to a victory.

### Flaws
Even though the minimax algorithm works correctly, my implementation of it is pretty slow. It takes couple of seconds for the AI to make a move on 5x5 board and its practically unplayable on 9x9.