import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from keras import layers
from keras import models
import numpy as np

fashion_mnist = keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

class_names = ['shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']

model = keras.models.Sequential([
    layers.Flatten(input_shape = (28,28)),       #input_layer
    layers.Dense(128,activation='relu'),
    layers.Dense(10,activation='softmax')
])

model.compile(
    optimizer='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(train_images,train_labels,epochs=5)

test_loss, test_acc = model.evaluate(test_images,test_labels,verbose=1)
print('>>>>test_loss ',test_loss)
print('>>>>test_acc ',test_acc)

prediction = model.predict(test_images)
print('>>>>test_images.shape ',test_images.shape)
print('>>>>prediction ',len(prediction))
print('>>>>prediction[121] ',prediction[121])

print(class_names[np.argmax(prediction[121])])

plt.figure()
plt.imshow(test_images[121],interpolation='bicubic')
plt.grid(False)
plt.colorbar()
plt.show()