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
    model_file = open('Data/Model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)
    model.load_weights("Data/Model/weights.h5")

    print('AI start now!')

    while 1:
        # Get screenshot:
        screen = ImageGrab.grab()
        # Image to numpy array:
        screen = np.array(screen)
        # 4 channel(PNG) to 3 channel(JPG)
        Y = predict(model, img)

        # TODO: Use Game Control

if __name__ == '__main__':
    main()
