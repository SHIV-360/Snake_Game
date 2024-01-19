------------------------------
run the main.py only 
------------------------------

Game Mechanics:
Movement and Controls:
The Snake class handles the snake's movement based on player input (keyboard controls awsd).
It updates the snake's position and direction, moving it across the game board grid.
Collision Detection:
Utilizes methods inherited from the Entity class for collision detection.
Checks for collisions between the snake's head and the food items or the boundaries of the game board.
Implements game logic to handle collisions, such as growing the snake when it eats food or ending the game upon collision with walls or itself.
Scoring and Game Loop:
Incorporates a scoring system that increments whenever the snake consumes food.
Implements a game loop to continuously update the game state, handle player input, and redraw the game board.
