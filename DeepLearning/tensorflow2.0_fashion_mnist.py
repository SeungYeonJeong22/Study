import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

class_names = ['shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']

(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()
print(train_images.shape)
print(train_labels.shape)
print(test_images.shape)
print(test_labels.shape)

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
# plt.show()

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape = (28,28)),
    keras.layers.Dense(128,activation = 'relu'),
    keras.layers.Dense(10,activation = 'softmax')
])

model.summary()

model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics= ['accuracy']
)

model.fit(train_images,train_labels,epochs=5)

test_loss, test_acc = model.evaluate(test_images,test_labels,verbose=1)

print('Test accuracy : {0}'.format(test_acc))

prediction = model.predict(test_images)
print(prediction[1])
print(class_names[np.argmax(prediction[1])])

plt.figure()
plt.imshow(test_images[1])
plt.show()

