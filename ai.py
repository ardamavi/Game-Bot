
# Arda Mavi
import os
import platform
import numpy as np
from time import sleep
from PIL import Image
from game_control import *
from predict import predict
from game_control import *
from keras.models import model_from_json
from mss import mss
import pickle

def main():
    # Get Model:
    model_file = open('Data/Model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)
    model.load_weights("Data/Model/weights.h5")

    print('AI starting now!')
    with open('listfile.data', 'rb') as filehandle:
        # read the data as binary data stream
        placesList = pickle.load(filehandle)
    while 1:
        # Get screenshot:
        with mss() as sct:
            monitor = sct.monitors[1]
            sct_img = sct.grab(monitor)
            # Convert to PIL/Pillow Image
            screen = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
            screen = np.array(screen)[:,:,:3] # Get first 3 channel from image as numpy array.
        # 4 channel(PNG) to 3 channel(JPG)
        Y = predict(model, screen)
        print(Y)
        Y = placesList[Y]
        Y = [int(i) for i in Y]
        print(Y)
        if Y == [0,0,0,0]:
            # Not action
            continue
        elif Y[0] == -1 and Y[1] == -1:
            # Only keyboard action.
            key = get_key(Y[3])
            if Y[2] == 1:
                # Press:
                press(key)
            else:
                # Release:
                release(key)
        elif Y[2] == 0 and Y[3] == 0:
            # Click action.
            click(Y[0], Y[1])
        '''
        else:
            # Mouse and keyboard action.
            # Mouse:
            click(int(Y[0]), int(Y[1]))
            # Keyboard:
            key = get_key(int(Y[3]))
            if Y[2] == 1:
                # Press:
                press(key)
            else:
                # Release:
                release(key)
        '''
        time.sleep(0.005)
if __name__ == '__main__':
    main()
