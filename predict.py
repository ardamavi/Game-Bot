# Arda Mavi
import numpy as np
import imageio


def predict(model, x):
    x = imageio.imresize(x, (150, 150, 3)).astype('float32') / 255.
    y = model.predict(x.reshape(1, 150, 150, 3))
    return y
