"""
Currently testing checkbox and radio buttons with cnn method for verification.
ref: 1. https://medium.com/nybles/create-your-first-image-recognition-classifier-using-cnn-keras-and-tensorflow-backend-6eaab98d14dd
     2. https://towardsdatascience.com/check-mark-state-recognition-will-take-nlp-projects-to-the-next-level-668a1013408f

Once method is working, I will update documents.
"""
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense

# Initializing the CNN
classifier = Sequential()
classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Flatten())

classifier.add(Dense(output_dim=128, activation="relu"))
classifier.add(Dense(output_dim=1, activation="sigmoid"))

classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)


"""
check image size python
    form PIL import Image
    img1 = Image.open('1.jpg')
    img1.size
"""
training_set = train_datagen.flow_from_directory('omr_dataset/train',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('omr_dataset/test',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

from IPython.display import display
from PIL import Image

classifier.fit_generator(training_set,
                         steps_per_epoch=4000,
                         epochs=10,
                         validation_data=test_set,
                         validation_steps=800)

# Test random jpeg
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('random.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] >= 0.5:
    prediction = 'dog'
else:
    prediction = 'cat'
print(prediction)
