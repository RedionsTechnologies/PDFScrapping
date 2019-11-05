"""
Currently testing checkbox and radio buttons with cnn method for verification.
ref: 1. https://medium.com/nybles/create-your-first-image-recognition-classifier-using-cnn-keras-and-tensorflow-backend-6eaab98d14dd
     2. https://towardsdatascience.com/check-mark-state-recognition-will-take-nlp-projects-to-the-next-level-668a1013408f

Once method is working, I will update documents.
"""
# Importing required libraries
# from tensorflow_core.python.framework import ops
# ops.reset_default_graph()
import os
import PIL
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import MaxPooling2D, Flatten, Dense, Convolution2D
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model


# Check if saved model file is available then load, Else build model
# Save/Load model ref- https://machinelearningmastery.com/save-load-keras-deep-learning-models/
classifier = None
if os.path.isfile('classifier_checkbox.h5'):
    classifier = load_model("classifier_checkbox.h5")

else:
    # Initializing the CNN
    classifier = Sequential()
    classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation="relu"))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    classifier.add(Flatten())

    classifier.add(Dense(output_dim=128, activation="relu"))
    classifier.add(Dense(output_dim=1, activation="sigmoid"))
    classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    train_datagen = ImageDataGenerator(rescale=1. / 255,
                                       shear_range=0.2,
                                       zoom_range=0.2,
                                       horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

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

    # from IPython.display import display

    classifier.fit_generator(training_set,
                             steps_per_epoch=4000,
                             epochs=10,
                             validation_data=test_set,
                             validation_steps=800)

    # Save trained keras model into file for further loading.
    # cause training model again takes more than 60 minutes.
    # Todo: Update logic of script to check for saved model first else train model.
    classifier.save("classifier_checkbox.h5")


# Test random jpeg file
import numpy as np
from keras.preprocessing import image

# test checked box
test_image = image.load_img('random.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict(test_image)
# training_set.class_indices
if result[0][0] >= 0.5:
    prediction = 'unchecked'
else:
    prediction = 'checked'
print(prediction)

# test unchecked image box
test_image1 = image.load_img('random1.jpg', target_size=(64, 64))
test_image1 = image.img_to_array(test_image1)
test_image1 = np.expand_dims(test_image1, axis=0)
result1 = classifier.predict(test_image1)
if result1[0][0] >= 0.5:
    prediction1 = 'unchecked'
else:
    prediction1 = 'checked'
print(prediction1)