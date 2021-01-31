# Arda Mavi
from pynput.mouse import Button, Controller as Mouse
from pynput.keyboard import Controller as Keyboard
import time
# For encoding keyboard keys:
def get_keys():
    return ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space_bar', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

def get_key(id):
    return get_keys()[id]

def get_id(key):
    try:
        print('Key Pressed:',key.char,sep='')
        return get_keys().index(key.char)
    except AttributeError:
        if (str(key)+'') not in get_keys():
            print((str(key)+''),' is not in list')
            return
    print('Key Pressed:',(str(key)+''),sep='')
    return get_keys().index((str(key)+''))

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
    move(x, y)
    return

# Keyboard:
def press(key):
    if key == "space_bar":
        keyboard.press(Key.space)
        time.sleep(0.025)
        keyboard.release(Key.space)
        return
    else:
        keyboard.press(key)
        time.sleep(0.025)
        keyboard.release(key)
    return

def release(key):
    keyboard.release(key)
    return
