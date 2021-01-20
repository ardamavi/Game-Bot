# Arda Mavi
import cv2


def predict(model, x):
    r = 50.0 / x.shape[0]
    dim = (int(x.shape[1] * r), 50)

    x = cv2.resize(x, dim, interpolation=cv2.INTER_AREA)
    # x = skimage.io.imresize(x, (150, 150, 3)).astype('float32') / 255.
    y = model.predict(x.reshape(1, 150, 150, 3))
    return y
