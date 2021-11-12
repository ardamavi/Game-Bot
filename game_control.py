# Arda Mavi
from pynput.mouse import Button, Controller as Mouse
from pynput.keyboard import Key, Controller as Keyboard
import time
import win32api
# For encoding keyboard keys:
def get_keys():
    return ['w', 'a', 's', 'd', 'r', 'f', 'g', 'c', 'Key.space', 'Key.shift']

def get_key(id):
    return get_keys()[id]

def get_id(key):
    try:
        print('Key Pressed:',key.char,sep='')
        return get_keys().index(key.char)
    except:
        if (str(key)+'') not in get_keys():
            print((str(key)+''),' is not in list')
            return 1000
    print('Key Pressed:',(str(key)+''),sep='')
    return get_keys().index((str(key)+''))

keyboard = Keyboard()
mouse = Mouse()

# Mouse:
def move(x, y):
    win32api.SetCursorPos((x,y))
    return

def scroll(x, y):
    mouse.scroll(x, y)
    return

def click(x, y):
    mouse.press(Button.left)
    move(x, y)
    return

# Keyboard:
def press(key):
    if key == 'Key.shift':
        keyboard.press(Key.shift)
    elif key == 'Key.space':
        keyboard.press(Key.space)
    else:
        keyboard.press(key)
    return

def release(key):
    if key == 'Key.shift':
        keyboard.release(Key.shift)
    elif key == 'Key.space':
        keyboard.release(Key.space)
    else:
        keyboard.release(key)
    return
