# Arda Mavi
from pynput.mouse import Button, Controller as Mouse
from pynput.keyboard import Controller as Keyboard

def get_key(id):
    return # TODO: return id's key

def get_id(key):
    return # TODO: return key's id

keyboard = Keyboard()
mouse = Mouse()

# Mouse:
def move(x, y):
    mouse.position = (x, y)
    return

def scroll(x, y):
    mouse.scroll(x, y)
    return

def click(x, y):
    mouse.press(Button.left)
    return

# Keyboard:
def press(key):
    keyboard.press(key)
    return

def release(key):
    keyboard.release(key)
    return
