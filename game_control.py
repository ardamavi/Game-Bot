# Arda Mavi
from pynput.mouse import Button, Controller as Mouse
from pynput.keyboard import Key, Controller as Keyboard

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
