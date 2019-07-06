# Josephus-Simulator
Simulator for the Extended Feline Josephus Game

1. josephus.py - returns array of players in order of death with optional 
 - ex.) ``python josephus.py 10 5 5 2 -s -g`` for a skip-first game showing the graphic of the game
 - ex.) ``python josephus.py 10 5 5 2 -k -n`` for a kill-first game showing no graphic
2. josephus_game_simulator.py - runs simulator but with nicer interface; also allows for varying lives per player
 - ex.) ``python josephus_game_simulator.py``
3. solution_tester.py - compares proved solutions from Extended Feline Josephus Game paper with the simulator
