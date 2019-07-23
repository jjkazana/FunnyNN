from tensorflow import keras
import tensorflow as tf


def new_model(inputSize):
    model = keras.Sequential([
        keras.layers.Dense(inputSize, activation=tf.nn.sigmoid),
        keras.layers.Dense(4096, activation=tf.nn.sigmoid),
        keras.layers.Dense(2048, activation=tf.nn.sigmoid),
        keras.layers.Dense(1024, activation=tf.nn.sigmoid),
        keras.layers.Dense(3, activation=tf.nn.sigmoid),
        keras.layers.Dense(1024, activation=tf.nn.sigmoid),
        keras.layers.Dense(2048, activation=tf.nn.sigmoid),
        keras.layers.Dense(4096, activation=tf.nn.sigmoid),
        keras.layers.Dense(inputSize),
        ])

    model.compile(optimizer=tf.keras.optimizers.RMSprop(), 
              loss='mean_squared_error',
              metrics=['accuracy'])


    return model





