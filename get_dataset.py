# Arda Mavi
import os
import sys
import numpy as np
from keras.utils import to_categorical
from scipy.misc import imread, imresize, imsave
from sklearn.model_selection import train_test_split

import pickle
def get_img(data_path):
    # Getting image array from path:
    img = imread(data_path)
    img = imresize(img, (150, 150, 3))
    return img

def save_img(path, img):
    imsave(path + '.jpg', img)
    return


def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]

def get_dataset(dataset_path='Data/Train_Data'):
    # Getting all data from data path:
    labels = os.listdir(dataset_path) # Geting labels
    X = []
    Y = []
    Z = []
    count_categori = [-1,''] # For encode labels
    for label in labels:
        datas_path = dataset_path+'/'+label
        for data in os.listdir(datas_path):
            img = get_img(datas_path+'/'+data)
            X.append(img)
            # For encode labels:
            current_choice = data.split(',')
            del current_choice[4]
            if current_choice != count_categori[1]:
                count_categori[0] += 1
                count_categori[1] = current_choice
                if count_categori[1] not in Z:
                    Z.append(count_categori[1])
            Y.append(count_categori[0])
    with open('listfile.data', 'wb') as filehandle:
        # store the data as binary data stream
        pickle.dump(Z, filehandle)
    X = np.array(X).astype('float32')/255.
    Y = np.array(Y).astype('float32')
    #print(Y)
    Y = to_categorical(Y, count_categori[0]+1)
    #print(Y)
    if not os.path.exists('Data/npy_train_data/'):
        os.makedirs('Data/npy_train_data/')
    np.save('Data/npy_train_data/X.npy', X)
    np.save('Data/npy_train_data/Y.npy', Y)
    X, X_test, Y, Y_test = train_test_split(X, Y, test_size=0.1)
    return X, X_test, Y, Y_test, count_categori[0]+1
