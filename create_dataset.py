"""
This file will create a dataset of images and labels for training.

Author: Arda Mavi
"""
import os
from multiprocessing import Process
import time

import numpy as np
from PIL import Image
from mss import mss
from numpy import size
from pynput.keyboard import Listener as key_listener
from pynput.mouse import Listener as mouse_listener

from game_control import get_id
from get_dataset import save_img


def get_screenshot():
    """
    This function will get the screenshot of the game.
    :return: num_array of the screenshot
    """
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
        img = np.array(img)[:, :, :3]  # Get first 3 channel from image as numpy array.
        # resize it with PIL, because scipy.misc.imresize is deprecated.
        img = img(Image.fromarray(img).resize((size[0] * 4, size[1] * 4), resample=Image.BICUBIC))
        # img = imresize(img, (150, 150, 3)).astype('float32') / 255.
        return img


def save_event_keyboard(data_path, event, key):
    """
    This function will save the event of the keyboard.
    :param data_path: path to save the event
    :param event: down or up
    :param key: which key is pressed
    """
    key = get_id(key)
    if key != 1000:
        data_path = data_path + '/-1,-1,{0},{1},{2}'.format(event, key, time.time())
        screenshot = get_screenshot()
        save_img(data_path, screenshot)


def save_event_mouse(data_path, x, y):
    """
    This function will save the event of the mouse.
    :param data_path: path to save the event
    :param x: x coordinate
    :param y: y coordinate
    """
    data_path = data_path + '/{0},{1},0,0,{2}'.format(x, y, time.time())
    screenshot = get_screenshot()
    save_img(data_path, screenshot)


def listen_mouse():
    """
    This function will listen the mouse and save the event.
    :return: None
    """
    data_path = 'Data/Train_Data/Mouse'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    def on_click(x, y, button, pressed):
        save_event_mouse(data_path, x, y)

    def on_scroll(x, y, dx, dy):
        pass

    def on_move(x, y):
        pass

    with mouse_listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()


def listen_keyboard():
    """
    This function will listen the keyboard and save the event.
    :return: None
    """
    data_path = 'Data/Train_Data/Keyboard'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    def on_press(key):
        save_event_keyboard(data_path, 1, key)

    def on_release(key):
        save_event_keyboard(data_path, 2, key)

    with key_listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def main():
    """
    This is the main function.
    """
    dataset_path = 'Data/Train_Data/'
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)

    # Start to listening mouse with new process:
    Process(target=listen_mouse, args=()).start()
    listen_keyboard()


if __name__ == '__main__':
    main()
