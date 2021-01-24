# Arda Mavi
from pynput.mouse import Button, Controller as Mouse
from pynput.keyboard import Controller as Keyboard

keyboard = Keyboard()

mouse = Mouse()


# For encoding keyboard keys:
def get_keys():
    return ['a', 'd', 's', 'enter', 'return', 'space', 'right', 'left', 'up', 'down']


def get_key(key_id):
    return get_keys()[key_id]


def get_id(key):
    print('key', key)
    print(get_keys(), 'index')
    return
    # return get_keys().index(key)


# Keyboard:
def press(key):
    keyboard.press(key)
    return


def release(key):
    keyboard.release(key)
    return


# Mouse:
"""

def move(x, y):
    mouse.position = (x, y)
    return


def scroll(x, y):
    mouse.scroll(x, y)
    return


def click(x, y):
    mouse.press(Button.left)
    return
"""
