import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

layers = tf.keras.layers

def load_data():
    # This function loads the CIFAR-10 dataset
    (training_images, training_labels), (testing_images, testing_labels) = tf.keras.datasets.cifar10.load_data()
    return training_images, training_labels, testing_images, testing_labels


def preprocess_images(training_images, testing_images):
    # Normalize the images by dividing each pixel value by 255
    training_images, testing_images = training_images / 255, testing_images / 255
    return training_images, testing_images


def create_model():
    # This function loads the pre-trained model from a file
    model = tf.keras.models.load_model('image_classifier_tensor_2.model')
    return model


def make_prediction(model, img):
    # This function uses the given model to make a prediction on the given image
    prediction = model.predict(np.array([img]) / 255)
    return prediction


def display_results(item,prediction, class_names):
    # This function displays the predicted class for the given prediction and list of class names
    index = np.argmax(prediction)
    print(f"{item} = Prediction is {class_names[index]}")
    plt.show()


# main function to run the program
def main():
    class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

    training_images, training_labels, testing_images, testing_labels = load_data()
    training_images, testing_images = preprocess_images(training_images, testing_images)
    model = create_model()
    items = ['plane.jpg', 'car.jpg', 'bird.jpg', 'cat.jpg', 'deer.jpg', 'dog.jpg', 'frog.jpg',
             'horse.jpg', 'ship.jpg', 'truck.jpg','cat_dog.jpg','dog_cat.jpg','deer_horse.jpg']
    for item in items:
        img = cv.imread('images/'+item)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        prediction = make_prediction(model, img)
        display_results(item,prediction, class_names)
        # showing the images
        img = plt.imread('images/'+item)
        plt.imshow(img)
        plt.title(item)
        plt.show()

# run the main function
main()
