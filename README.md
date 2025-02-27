<h1 align="center">Tic Tac in Python</h1>

Overview:
=================

<p align="justify">Introduction to Artificial Intelligence. Implementation of the old-fashioned game in Python language, for the Artificial Intelligence course.</p>
<p align="justify">Tic-tac-toe, despite its simplicity, is a classic testing ground for artificial intelligence. By developing an AI to play tic-tac-toe, programmers can explore fundamental concepts of decision-making and strategy in a controlled environment.</p>
<p align="justify">One of the most widely used algorithms to create an unbeatable AI at tic-tac-toe is minimax. This technique allows the machine to explore all possible sequences of moves, assigning values ​​to each state of the game and always choosing the option that maximizes its chances of winning or minimizes the chances of losing.</p>


<h3>How does minimax work?</h3>
=================

<p align="justify">Game tree: The algorithm creates a tree where each node represents a possible game state.</p>
<p align="justify">State evaluation: Each leaf of the tree (final state) is evaluated: win, lose, or draw.</p>
<p align="justify">Value propagation: Values ​​are propagated from bottom to top in the tree, alternating between maximizing (for the AI) and minimizing (for the opponent).</p>
<p align="justify">Best move selection: The AI ​​chooses the move that leads to the best possible value at the root node.</p>

<h3>Why is minimax ideal for tic-tac-toe?</h3>
=================

<p align="justify">Limited search space: Tic-tac-toe has a relatively small number of possible states, making full exploration of the game tree feasible.</p>
<p align="justify">Complete information: Both players have complete knowledge of the game state at any given time.</p>
<p align="justify">Zero-sum game: What one player wins, the other loses.</p>

=================
<p align="justify">In short, tic-tac-toe and the minimax algorithm are a perfect pair to demonstrate the ability of artificial intelligence to make strategic decisions in a simple yet challenging environment. By understanding this application, we can appreciate the sophistication of AI algorithms and their importance in a variety of areas, from games to real-world problems.</p>

<h3>How to Play?</h3>
=================

<p align="justify">First, run the file "Program.py"!</p>

<p align="justify">The board with the squares will appear on the home screen. First select the difficulty, choosing the specific number.</p>
<p align="justify">0 - I want my mother</p>
<p align="justify">1 - I still wet the bed</p>
<p align="justify">2 - I'm Batman!</p>
<p align="justify">3 - Birl! Chuck Norris!</p>

<img src="img/inicio.png" width="300">

<p align="justify">After selecting the difficulty, choose whether you want to start the game:</p>
<p align="justify">0 - Yes</p>
<p align="justify">1 - No</p>

<img src="img/jogador.png" width="300">

<p align="justify">Then the board will appear. Type your move in the 'move' field. For example, a1, which corresponds to square a1 on the board.</p>

<img src="img/move.png" width="300">

<p align="justify">After that, the machine will execute its move. After that, it will be yours again. Keep playing until you reach the end of the game.</p>

<img src="img/final.png" width="300">
