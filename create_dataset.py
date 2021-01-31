# Arda Mavi
import os
import sys
import platform
import numpy as np
from time import sleep
from PIL import ImageGrab
from game_control import *
from predict import predict
from scipy.misc import imresize
from game_control import get_id
from get_dataset import save_img
from multiprocessing import Process
from keras.models import model_from_json
from pynput.mouse import Listener as mouse_listener
import string
from threading import *
import keyboard as kb
def get_screenshot():
    img = ImageGrab.grab()
    img = np.array(img)[:,:,:3] # Get first 3 channel from image as numpy array.
    img = imresize(img, (150, 150, 3)).astype('float32')/255.
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

    with mouse_listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

def listen_keyboard():
    data_path = 'Data/Train_Data/Keyboard'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    keys = list(string.ascii_lowercase)
    keys.append("space_bar")
    
    def pressed(key):
        while True:
            continue_or_na = kb.is_pressed(key)
            if continue_or_na:
                save_event_keyboard(data_path, 1, key)
    
   
            
    
    thread1 = [Thread(target=pressed, kwargs={"key":key}, daemon=True) for key in keys]
    for thread in thread1:
        thread.start()
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
