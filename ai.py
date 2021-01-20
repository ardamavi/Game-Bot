# Arda Mavi
import os
import platform
import numpy as np
from time import sleep
from PIL import ImageGrab
from game_control import *
from predict import predict
from game_control import *
from keras.models import model_from_json


def main():
    # Get Model:
    model_file = open('data/model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)
    model.load_weights('data/model/weights.h5')

    print('AI training has begun')

    while 1:
        # Get screenshot:
        screen = ImageGrab.grab()
        # Image to numpy array:
        screen = np.array(screen)
        # 4 channel(PNG) to 3 channel(JPG)
        y = predict(model, screen)
        if y == [0, 0, 0, 0]:
            # Not action
            continue
        elif y[0] == -1 and y[1] == -1:
            # Only keyboard action.
            key = get_key(y[3])
            if y[2] == 1:
                # Press:
                press(key)
            else:
                # Release:
                release(key)
        elif y[2] == 0 and y[3] == 0:
            # Only mouse action.
            pass
            # click(y[0], y[1])
        else:
            # Mouse and keyboard action.
            # Mouse:
            # click(y[0], y[1])
            # Keyboard:
            key = get_key(y[3])
            if y[2] == 1:
                # Press:
                press(key)
            else:
                # Release:
                release(key)


if __name__ == '__main__':
    main()
