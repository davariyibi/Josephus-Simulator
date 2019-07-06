# Josephus-Simulator
Simulator for the Extended Feline Josephus Game

## Requirements
Python 2.7

## Files
1. josephus.py - returns array of players in order of death with optional 
 - ex.) ``python josephus.py 10 3 4 2 0 s g`` for a skip-first game showing the graphic of the game
 - ex.) ``python josephus.py 10 3 4 2 0 k n`` for a kill-first game showing no graphic
2. josephus_game_simulator.py - runs simulator but with nicer interface; also allows for varying lives per player
 - ex.) ``python josephus_game_simulator.py``
3. solution_tester.py - compares proved solutions from Extended Feline Josephus Game paper with the simulator
 - ex.) ``python solution_tester.py 10 5 5 2 0 s g`` for a skip-first game showing the graphic of the game
