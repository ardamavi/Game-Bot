"""
This file will make a prediction based on the input data.
Author: Arda Mavi
"""
from PIL import Image
from numpy import size


def predict(model, X):
    """
    This function will make a prediction based on the input data.
    :param model: Which model to use.
    :param X: input data.
    :return: y_pred: prediction.
    """
    # resize it with PIL, because scipy.misc.imresize is deprecated.
    x = X(Image.fromarray(X).resize((size[0] * 4, size[1] * 4),
                                    resample=Image.BICUBIC))
    y = model.predict(x.reshape(1, 150, 150, 3))
    y = y.argmax()
    return y
