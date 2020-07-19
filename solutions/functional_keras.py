x = keras.Input(shape=(width, height))
x_reshape = keras.layers.Reshape(target_shape=(width, height, 1))(x)
conv1 = keras.layers.Conv2D(32, (5, 5), activation='relu')(x_reshape)
pool1 = keras.layers.MaxPool2D()(conv1)
conv2 = keras.layers.Conv2D(64, (5, 5), activation='relu')(pool1)
pool2 = keras.layers.MaxPool2D()(conv2)
pool2_flat = keras.layers.Flatten()(pool2)
dense = keras.layers.Dense(1024, activation='relu')(pool2_flat)
dense_drop = keras.layers.Dropout(rate=0.5)(dense)
yhat = keras.layers.Dense(ncats, activation='softmax')(dense_drop)

model = keras.Model(inputs=x, outputs=yhat)
model.summary()