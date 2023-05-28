"""
This file will create a dataset of images and labels for training.

Author: Arda Mavi
"""
import os
import time
from multiprocessing import Process

import numpy as np
from PIL import Image
from mss import mss
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
        img = Image.fromarray(img)
        img = img.resize((150,  150), resample=Image.NEAREST)
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


def save_event_mouse(data_path, x_coordinate, y_coordinate, button, pressed):
    """
    This function will save the event of the mouse.
    :param data_path: path to save the event
    :param x_coordinate: x coordinate
    :param y_coordinate: y coordinate
    """
    # 539,996,0,0,1643879876.0606766
    # 539 x coordinate
    # 996 y coordinate

    # 1643879876.0606766 time since epoch
    # button is an enum

    # cut button at dot and keep the last part.
    button = button.name.split('.')[-1]
    data_path = data_path + '/{0},{1},{2},{3},{4}'.format(x_coordinate, y_coordinate, button, int(pressed),
                                                          time.time())
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

    def on_click(x_coordinate, y_coordinate, button, pressed):
        """
        This function will get the x and y coordinate of the mouse, when a click happens.
        :param x_coordinate: int
        :param y_coordinate: int
        :TODO: fix the function. Help from: https://pynput.readthedocs.io/en/latest/mouse.html
        """
        print(data_path, x_coordinate, y_coordinate, button, pressed)
        save_event_mouse(data_path, x_coordinate, y_coordinate, button, pressed)

    def on_scroll(x_cord, y_cord, dx, dy):
        """
        This function will get the new x and y coordinate of the mouse, when a scroll happens.
        dx and dy are the amount of scrolling.
        :param x_cord: int
        :param y_cord: int
        :param dx: int
        :param dy: int
        :return: None
        """
        pass

    def on_move(x_cord, y_cord):
        """
        This function will get the new x and y coordinate of the mouse, when a move happens.
        If this callback raises an exception, or returns False, the mouse tracking will be stopped.
        :param x_cord: int
        :param y_cord: int
        :return: None
        """
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
