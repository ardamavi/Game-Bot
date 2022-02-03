# Game Bot
### By Arda Mavi

Artificial intelligence that learns to play any game by watching you.

## How does this work?
- First: Run program and play any game for a little bit.
- Second: Run program and watch the artificial intelligence play the game.

## How does it work behind the scenes?
When you run the training program, the program listens for your keyboard and mouse moving, then it saves those movements.<br>
Artificial intelligence learn: When I push any button?<br/>
And when you run the program, it plays the game just like you!

## But how does it learn?
##### Magic! (just joking)
With deep learning.<br/>
Deep Learning is a subfield of machine learning with neural networks inspired by the structure of the brains artificial neural networks.

### Playing with Artificial Intelligence:
1. Open your desired game (If you have already trained the artificial intelligence).
2. Run `python3 ai.py` command in terminal.

### Creating Training Dataset:
1. Change the desired kets in the game_control.py file's get keys function, by changing return keys to desired ones
1. Run `python3 create_dataset.py` command in terminal.
2. Play your desired game.
3. Stop `create_dataset` program with `ctrl-C` in terminal.

### Model Training:
`python3 train.py`

### Using TensorBoard:
`tensorboard --logdir=Data/Checkpoints/logs`

### Important Notes:
- Tested in Python version 3.6.0

- Install necessary modules with `sudo pip3 install -r requirements.txt` command.

## WINDOWS Installation:
- Install Python 3.6.0 : https://www.python.org/downloads/release/python-360/
- Run CMD and Input Command `pip3 install -r requirements.txt`

### This project is still being worked on ...
