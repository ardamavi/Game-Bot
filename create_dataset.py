# Arda Mavi
import os
import cv2
import sys
import platform
import numpy as np
from time import sleep
from PIL import ImageGrab
from game_control import *
from predict import predict
from game_control import get_id
from get_dataset import save_img
from multiprocessing import Process
from keras.models import model_from_json
from pynput.mouse import Listener as Mouse_Listener
from pynput.keyboard import Listener as Key_Listener

def get_screenshot():
    img = ImageGrab.grab()
    img = np.array(img)[:, :, :3]  # Get first 3 channel from image as numpy array.

    """
    The ratio is r. The new image will
    have a height of 50 pixels. To determine the ratio of the new
    height to the old height, we divide 50 by the old height.
    """

    r = 50.0 / img.shape[0]
    dim = (int(img.shape[1] * r), 50)

    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # img = imresize(img, (150, 150, 3)).astype('float32') / 255.

    return img


def save_event_keyboard(data_path, event, key):
    key = get_id(key)
    data_path = data_path + '/-1,-1,{0},{1}'.format(event, key)
    screenshot = get_screenshot()
    save_img(data_path, screenshot)
    return


def save_event_mouse(data_path, x, y):
    data_path = data_path + '/{0},{1},0,0'.format(x, y)
    screenshot = get_screenshot()
    save_img(data_path, screenshot)
    return


def listen_mouse():
    data_path = 'Data/Train_Data/Mouse'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    def on_click(x, y, button, pressed):
        save_event_mouse(data_path, x, y)

    def on_scroll(x, y, dx, dy):
        pass

    def on_move(x, y):
        pass

    with Mouse_Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()


def listen_keyboard():
    data_path = 'Data/Train_Data/Keyboard'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    def on_press(key):
        save_event_keyboard(data_path, 1, key)

    def on_release(key):
        save_event_keyboard(data_path, 2, key)

    with Key_Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def main():
    dataset_path = 'Data/Train_Data/'
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)

    # Start to listening mouse with new process:
    Process(target=listen_mouse, args=()).start()
    listen_keyboard()
    return


if __name__ == '__main__':
    main()
