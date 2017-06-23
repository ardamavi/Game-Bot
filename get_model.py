# Arda Mavi
import os
from keras.models import Model
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
    inputs = Input(shape=(150, 150, 3))

    conv_1 = Conv2D(32, (3,3), strides=(1,1))(inputs)
    act_1 = Activation('relu')(conv_1)

    conv_2 = Conv2D(64, (3,3), strides=(1,1))(act_1)
    act_2 = Activation('relu')(conv_2)

    conv_3 = Conv2D(64, (3,3), strides=(1,1))(act_2)
    act_3 = Activation('relu')(conv_3)

    pooling_1 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(act_3)

    conv_4 = Conv2D(128, (3,3), strides=(1,1))(pooling_1)
    act_4 = Activation('relu')(conv_4)

    pooling_2 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(act_4)

    flat_1 = Flatten()(pooling_2)

    fc = Dense(1280)(flat_1)
    fc = Activation('relu')(fc)
    fc = Dropout(0.5)(fc)
    fc = Dense(4)(fc)

    outputs = Activation('sigmoid')(fc)

    model = Model(inputs=inputs, outputs=outputs)

    model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

    return model

if __name__ == '__main__':
    save_model(get_model())
