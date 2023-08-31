import tensorflow as tf

def load_and_prepare_data():
    # load the CIFAR-10 dataset and normalize the images
    (training_images, training_labels), (testing_images, testing_labels) = tf.keras.datasets.cifar10.load_data()
    training_images, testing_images = training_images / 255, testing_images / 255

    return training_images, training_labels, testing_images, testing_labels

def define_model():
    # define the CNN model
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Dropout(0.2))

    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Dropout(0.2))

    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    return model


def train_and_evaluate_model(model, training_images, training_labels, testing_images, testing_labels):
    # compile and train the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(training_images, training_labels, epochs=15, validation_data=(testing_images, testing_labels))

    # evaluate the model
    loss, accuracy = model.evaluate(testing_images, testing_labels)
    print(f"loss: {loss}")
    print(f"accuracy: {accuracy}")

    # save the model
    model.save('image_classifier_tensor_2.model')


def main():
    # load the data
    training_images, training_labels, testing_images, testing_labels = load_and_prepare_data()

    # define the model
    model = define_model()

    # train and evaluate the model
    train_and_evaluate_model(model, training_images, training_labels, testing_images, testing_labels)


# run the main function
if __name__ == "__main__":
    main()
