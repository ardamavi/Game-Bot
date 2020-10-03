# Arda Mavi
import numpy as np, skimage, imageio, matplotlib
from PIL import ImageGrab, Image

def predict(model, X):
    X = np.array(X, (150, 150, 3)).astype('float32')/255.
    Y = model.predict(X.reshape(1,150,150,3))
    return Y
