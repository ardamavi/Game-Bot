# Arda Mavi
import os
import numpy as np
import cv2
from keras.utils import to_categorical
import imageio
from skimage import *
import skimage.io
from sklearn.model_selection import train_test_split


def get_img(data_path):
    # Getting image array from path:
    img = skimage.io.imread(data_path)
    """
    The ratio is r. The new image will
    have a height of 150 pixels. To determine the ratio of the new
    height to the old height, we divide 150 by the old height.
    """

    r = 150.0 / img.shape[0]
    dim = (int(img.shape[1] * r), 150)

    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # img = imresize(img, (150, 150, 3)).astype('float32') / 255.

    return img


def save_img(img, path):
    sk_img = skimage.io.imread(path)
    sk_img = sk_img.transpose(1, 0, 2).reshape(130, -1)
    image = img_as_ubyte(sk_img)
    skimage.io.imsave(path, image)
    skimage.io.imsave(path, img)
    # skimage.io.imsave(path, img_as_uint(img))
    return


def get_dataset(dataset_path='data\\train_data'):
    # Getting all data from data path:
    try:
        x = np.load('data\\npy_train_data\\x.npy')
        y = np.load('data\\npy_train_data\\y.npy')
    except AttributeError:
        labels = os.listdir(dataset_path)  # getting labels
        x = []
        y = []
        count_category = [-1, '']  # For encode labels
        for label in labels:
            datas_path = dataset_path + '/' + label
            for d_data in os.listdir(datas_path):
                img = get_img(datas_path + '/' + d_data)
                x.append(img)
                # For encode labels:
                if d_data != count_category[1]:
                    count_category[0] += 1
                    count_category[1] = d_data.split(',')
                y.append(count_category[0])
        # Create dateset:
        x = np.array(x).astype('float32') / 255.
        y = np.array(y).astype('float32')
        y = to_categorical(y, count_category[0] + 1)
        if not os.path.exists('data\\npy_train_data/'):
            os.makedirs('data\\npy_train_data/')
        np.save('data\\npy_train_data/x.npy', x)
        np.save('data\\npy_train_data/y.npy', y)
    x, x_test, y, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
    return x, x_test, y, y_test
