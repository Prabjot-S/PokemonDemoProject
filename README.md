# Pokémon Battle Game - FSM/NFA Model (Python + Pygame)
This project is a simplified turn-based Pokémon battle game built using Python and Pygame, designed to demonstrate how FSMs, specifically a NFA can model sequential game logic and player.

## 🎮 Game Overview

  - Two Pokémon: Giratina vs Blastoise
  - Player actions each turn: Attack (random 10-30 dmg), Heal (+10 HP, max 3 uses), Concede
  - Alternating turns until one Pokémon's HP reaches 0 or the player concedes
  - The stats page displays total wins for each Pokémon


## 🛠 Technologies Used
  - Python 3
  - Pygame
  - Simple file system storage for game stats (JSON)

## 📁 Project Structure
- Game.py (Main game loop, states, battle logic, rendering)
- button.py (Reusable button class for UI)
- assets/ (Sprites, backgrounds, animations)
- pokemon_game_scores.txt (Persists win counts)

## ▶️ How to Run
- Install dependencies: pip install pygame
- Run game: python Game.py

## 📚 Purpose
This project was created for CSCI-312: Theory of Computation to illustrate how automata theory can be applied to real world systems, especially interactive games
