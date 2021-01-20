# Arda Mavi
import os
import numpy
from get_dataset import get_dataset
from get_model import get_model, save_model
from keras.callbacks import ModelCheckpoint, TensorBoard

epochs = 100
batch_size = 5


def train_model(model, x, x_test, y, y_test):
    checkpoints = []
    if not os.path.exists('Data/Checkpoints/'):
        os.makedirs('Data/Checkpoints/')

    checkpoints.append(
        ModelCheckpoint('Data/Checkpoints/best_weights.h5', monitor='val_loss', verbose=0, save_best_only=True,
                        save_weights_only=True, mode='auto', period=1))
    checkpoints.append(
        TensorBoard(log_dir='Data/Checkpoints/./logs', histogram_freq=0, write_graph=True, write_images=False,
                    embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None))

    model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test), shuffle=True,
              callbacks=checkpoints)

    return model


def main():
    x, x_test, y, y_test = get_dataset()
    model = get_model()
    model = train_model(model, x, x_test, y, y_test)
    save_model(model)
    return model


if __name__ == '__main__':
    main()
