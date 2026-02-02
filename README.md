🎮 Hangman Game

A lightweight, browser-based implementation of the classic Hangman word-guessing game.

## Overview

This project provides an interactive Hangman game with a clean, modern UI built with HTML, CSS, and JavaScript. The game logic is managed through a Python script that generates and serves the HTML interface.

## Files

- **Hangman.py** - Python script that generates the HTML/CSS/JS UI and opens it in your default browser
- **hangman_ui.html** - The generated HTML file containing the complete game interface

## Features

- **Interactive Gameplay** - Guess letters to uncover the hidden word
- **Visual Feedback** - See remaining attempts and guessed letters at a glance
- **Word Bank** - Game selects from 5 different words: WEATHER, GRAPES, COMPUTER, STUDENT, FOOTBALL
- **Responsive Design** - Clean, modern blue and white color scheme that works on different screen sizes
- **Easy Reset** - Click the "Reset" button to start a new game anytime

## How to Play

1. Run the Python script:
   ```
   python Hangman.py
   ```

2. The game will automatically open in your default web browser

3. **Guess letters** by clicking the letter buttons on the keyboard

4. **Win** by revealing all letters in the word before running out of attempts

5. **Game Over** occurs when attempts reach 0

6. Click **Reset** to start a new game

## Game Rules

- You start with **6 attempts**
- Each incorrect guess costs **1 attempt**
- Correct guesses reveal all instances of that letter in the word
- Win by revealing the entire word before attempts run out
- Lose if attempts reach 0

## Requirements

- Python 3.x
- A modern web browser (Chrome, Firefox, Safari, Edge)

## Technical Details

- **Color Scheme**: White cards on light blue background
- **Keyboard Layout**: 26 interactive letter buttons in a grid
- **Game Status**: Real-time display of attempts remaining and guessed letters
- **Win/Loss Messages**: Clear feedback when game ends
