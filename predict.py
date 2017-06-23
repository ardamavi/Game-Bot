# Arda Mavi
import numpy as np
from scipy.misc import imresize

def predict(model, X):
    X = imresize(X, (150, 150, 3)).astype('float32')/255.
    Y = model.predict(X.reshape(1,150,150,3))
    return Y
