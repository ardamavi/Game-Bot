# Arda Mavi
import os
from keras.models import Model
from database_process import get_data
from keras.optimizers import Adadelta
from keras.layers import Input, Conv2D, Activation, MaxPooling2D, Flatten, Dense, Dropout

def save_model(model):
    if not os.path.exists('Data/Model/'):
        os.makedirs('Data/Model/')
    model_json = model.to_json()
    with open("Data/Model/model.json", "w") as model_file:
        model_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("Data/Model/weights.h5")
    print('Model and weights saved')
    return


def get_model():
    num_class = len(get_data('SELECT id FROM "id_char"'))

    # TODO: Model here

    return model

if __name__ == '__main__':
    save_model(get_model())
