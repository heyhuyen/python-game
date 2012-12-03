My text-based console game of chance, written in [Python](http://www.python.org) as an exercise from Zed A. Shaw's [Learn Python the Hard Way](http://learnpythonthehardway.org) book. Written during [Hacker School](https://www.hackerschool.com/), Batch[4], Fall 2012.

## Usage
Run this command: `python my_game.py`. The rest is pretty straightforward. Type your response when prompted. The rules are outlined below.

## Rules
- Win when you reach level 10
- Die if you run out of health points (10 max)

### Minigames
All the minigames are based on chance.

#### Fight a Monster
Fight a monster whose level is randomly chosen between 1 and 10

- If your level is higher, you automatically win and gain a level.
- Otherwise if you fight:
    - you have a 30% chance of defeating the monster and gaining 2 levels.
    - or you lose a level and 4 health points.
- Or you run away:
    - you have a 50% chance of running away unharmed
    - else you lose 2 health points

#### Coin Flip
Guess `heads` or `tails`.

- If you are right, you gain a level.

#### Rock Paper Scissors
Best of 1. Your hand against the computer.

- If you win, you gain a level.

## Todo/Extension Ideas

- Use `re` regex module for better text input handling.
- Add help to explain rules.

## Resources
- Zed A. Shaw's [Learn Python the Hard Way](http://learnpythonthehardway.org)
- Rosetta Code's [Rock Paper Scissors](http://rosettacode.org/wiki/Rock-paper-scissors#Python)
