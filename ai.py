"""
This is the main file for the AI.

Author: Arda Mavi
"""
import pickle

import time
import numpy as np
from PIL import Image
from tensorflow.keras.models import model_from_json
from mss import mss

from game_control import get_key, press, release, click
from predict import predict


def main():
    """
    Main function.

    :return: None
    """
    with open("Data/Model/model.json", "r") as model_file:
        model = model_file.read()
    model = model_from_json(model)
    model.load_weights("Data/Model/weights.h5")

    print("AI starting now!")
    with open("listfile.data", "rb") as filehandle:
        # read the data as binary data stream
        places_list = pickle.load(filehandle)
    while 1:
        # Get screenshot:
        with mss() as sct:
            monitor = sct.monitors[1]
            sct_img = sct.grab(monitor)
            # Convert to PIL/Pillow Image
            screen = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw",
                                     "BGRX")
            screen = np.array(screen)[
                :, :, :3
            ]  # Get first 3 channel from image as numpy array.
        # 4 channel(PNG) to 3 channel(JPG)
        y_ai = predict(model, screen)
        print(y_ai)
        y_ai = places_list[y_ai]
        y_ai = [int(i) for i in y_ai]
        print(y_ai)
        if y_ai == [0, 0, 0, 0]:
            # Not action
            continue
        if y_ai[0] == -1 and y_ai[1] == -1:
            # Only keyboard action.
            key = get_key(y_ai[3])
            if y_ai[2] == 1:
                # Press:
                press(key)
            else:
                # Release:
                release(key)
        elif y_ai[2] == 0 and y_ai[3] == 0:
            # Click action.
            click(y_ai[0], y_ai[1])

        # else:
        #     # Mouse and keyboard action.
        #     # Mouse:
        #     click(int(y_ai[0]), int(y_ai[1]))
        #     # Keyboard:
        #     key = get_key(int(y_ai[3]))
        #     if y_ai[2] == 1:
        #         # Press:
        #         press(key)
        #     else:
        #         # Release:
        #         release(key)

        time.sleep(0.005)


if __name__ == "__main__":
    main()
