# Arda Mavi
import os
import numpy as np
import cv2
from keras.utils import to_categorical
import imageio
from sklearn.model_selection import train_test_split


def get_img(data_path):
    # Getting image array from path:
    img = imageio.imread(data_path)
    """
    The ratio is r. The new image will
    have a height of 50 pixels. To determine the ratio of the new
    height to the old height, we divide 50 by the old height.
    """

    r = 50.0 / img.shape[0]
    dim = (int(img.shape[1] * r), 50)

    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # img = imresize(img, (150, 150, 3)).astype('float32') / 255.

    return img


def save_img(img, path):
    imageio.imsave(path, img)
    return


def get_dataset(dataset_path='Data/Train_Data'):
    # Getting all data from data path:
    try:
        x = np.load('Data/npy_train_data/X.npy')
        y = np.load('Data/npy_train_data/Y.npy')
    except Exception as e:
        print("exception", e)
        labels = os.listdir(dataset_path)  # Geting labels
        x = []
        y = []
        count_category = [-1, '']  # For encode labels
        for label in labels:
            datas_path = dataset_path + '/' + label
            for data in os.listdir(datas_path):
                img = get_img(datas_path + '/' + data)
                x.append(img)
                # For encode labels:
                if data != count_category[1]:
                    count_category[0] += 1
                    count_category[1] = data.split(',')
                y.append(count_category[0])
        # Create dateset:
        x = np.array(x).astype('float32') / 255.
        y = np.array(y).astype('float32')
        y = to_categorical(y, count_category[0] + 1)
        if not os.path.exists('Data/npy_train_data/'):
            os.makedirs('Data/npy_train_data/')
        np.save('Data/npy_train_data/X.npy', x)
        np.save('Data/npy_train_data/Y.npy', y)
    x, x_test, y, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
    return x, x_test, y, y_test
