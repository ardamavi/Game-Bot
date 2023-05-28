"""
This file will get the dataset.

Author: Arda Mavi
"""
import os
import pickle

import numpy as np
from PIL import Image
from tensorflow.keras.utils import to_categorical
from numpy import size
from sklearn.model_selection import train_test_split
from imageio import imread, imsave


def get_img(data_path):
    """
    Getting image array from path and read it.
    :param data_path: The image_array path.
    :return: the image
    """
    img = imread(data_path)
    return img


def save_img(path, img):
    """
    Saving image to path.
    :param path: The path to save the image.
    :param img: Which image to save.
    """
    imsave(path + '.jpg', img)


def before(value, a):
    """
    Find first part and slice it.
    :param value: The value to slice.
    :param a: The value to slice.
    :return: value before a
    """
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1:
        return ""
    return value[:pos_a]


def get_dataset(dataset_path='Data/Train_Data'):
    """
    Getting all data from data path:
    :param dataset_path: The path to the dataset.
    :return: x_dataset, y_dataset, x_test, y_test
    """
    labels = os.listdir(dataset_path)  # Getting labels
    x_dataset = []
    y_dataset = []
    z_dataset = []
    count_category = [-1, '']  # For encode labels
    for label in labels:
        datas_path = dataset_path + '/' + label
        for data in os.listdir(datas_path):
            img = get_img(datas_path + '/' + data)
            x_dataset.append(img)
            # For encode labels:
            current_choice = data.split(',')
            del current_choice[4]
            if current_choice != count_category[1]:
                count_category[0] += 1
                count_category[1] = current_choice
                if count_category[1] not in z_dataset:
                    z_dataset.append(count_category[1])
            y_dataset.append(count_category[0])
    with open('listfile.data', 'wb') as filehandle:
        # store the data as binary data stream
        pickle.dump(z_dataset, filehandle)
    x_dataset = np.array(x_dataset).astype('float32') / 255.
    y_dataset = np.array(y_dataset).astype('float32')
    # print(y_dataset)
    y_dataset = to_categorical(y_dataset, count_category[0] + 1)
    # print(y_dataset)
    if not os.path.exists('Data/npy_train_data/'):
        os.makedirs('Data/npy_train_data/')
    np.save('Data/npy_train_data/x_dataset.npy', x_dataset)
    np.save('Data/npy_train_data/y_dataset.npy', y_dataset)
    x_dataset, x_test, y_dataset, y_test = train_test_split(x_dataset, y_dataset, test_size=0.1)
    return x_dataset, x_test, y_dataset, y_test, count_category[0] + 1
