# Arda Mavi
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout

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


def get_model(action_total):
    model = Sequential()

    model.add(Conv2D(10, (3,3)))
    model.add(MaxPool2D((2,2)))
    for i in range(3):
        model.add(Conv2D(16, (2, 2)))
        model.add(MaxPool2D((2, 2)))
    #model.add(Dropout(0.4))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(action_total, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

if __name__ == '__main__':
    save_model(get_model())
