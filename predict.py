# Arda Mavi
import numpy as np
import imageio

def predict(model, X):
    X = imageio.imresize(X, (150, 150, 3)).astype('float32') /255.
    Y = model.predict(X.reshape(1,150,150,3))
    Y = Y.argmax()
    return Y
