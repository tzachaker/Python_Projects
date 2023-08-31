# Image Classification - Deep Learning Project

## Abstract
The "Image Classification - Deep Learning Project" utilizes the CIFAR-10 dataset and TensorFlow 2 to implement an image classification system. The project involves using a pre-trained image-classification model to make predictions on a set of images.

The primary objective of this project is to harness the power of TensorFlow 2 and the CIFAR-10 dataset within the Python programming environment to develop and train a deep learning model capable of accurate image classification. The model will be trained using a dataset consisting of 60,000 32x32 color images, each assigned to one of 10 distinct classes. The trained model's performance will be evaluated using a separate set of 10,000 images. The ultimate goal is to achieve a high level of accuracy in classifying images, thereby showcasing the efficacy of TensorFlow 2 and deep learning methodologies in tasks involving image recognition.

## Examples of regular tests:
![image](https://github.com/tzachaker/Image_Classification/assets/76492492/45373497-aed4-41cc-aa29-8a25f6eea6df)
![image](https://github.com/tzachaker/Image_Classification/assets/76492492/9605e74b-e9d3-4a5e-96ef-d5ca3a312efd)

## Examples of complex tests:
- 40% cat + 60% dog:
![image](https://github.com/tzachaker/Image_Classification/assets/76492492/4d79d332-bcb3-4edd-a041-d3aa5e67e908)
![image](https://github.com/tzachaker/Image_Classification/assets/76492492/7224b01b-7b85-4c0e-a010-0959dbb61406)

- 60% deer + 40% horse:
![image](https://github.com/tzachaker/Image_Classification/assets/76492492/e017a555-dc5f-4b82-b866-ead45b02e93c)

## Project Structure
The project consists of the following key scripts:

### modelTensor2.py
This script is responsible for training and saving a Convolutional Neural Network (CNN) model on the CIFAR-10 dataset. The code defines the architecture of the CNN model using TensorFlow's Keras library, leveraging the Sequential API. The model incorporates layers such as 2D convolutional layers with ReLU activation functions, BatchNormalization, MaxPooling2D, and Dropout layers to enhance the model's performance and prevent overfitting.

###  main.py
The main script utilizes the pre-trained CNN model to classify new images. It achieves this by reading images from a specified folder, making predictions using the pre-trained model, and displaying the classification results.

## Project Purpose
The main objective of this project is to effectively leverage TensorFlow 2 and the CIFAR-10 dataset to design, build, and train a sophisticated deep learning model specifically tailored for image classification tasks. By achieving high accuracy in image classification, this project highlights the potential of utilizing advanced machine learning techniques for intricate image recognition challenges.

## Technology Used - Convolutional Neural Network (CNN)
The core technology employed in this project is the Convolutional Neural Network (CNN). The code defines a CNN model using TensorFlow's Keras library. The model architecture consists of several layers designed to process and analyze image data effectively:

- 2D Convolutional Layers: The model starts with 2D convolutional layers that apply convolutional operations on the input images. These layers employ 32 and 64 filters, respectively, along with ReLU activation functions.

- BatchNormalization: This layer normalizes the inputs, enhancing the model's learning process.

- MaxPooling2D: These layers perform max-pooling operations to reduce spatial dimensions and capture important features.

- Dropout: Dropout layers are added to mitigate overfitting, ensuring the model's generalization to unseen data.

- Flatten and Dense Layers: Following the convolutional layers, the model incorporates Flatten and Dense layers to prepare the data for classification.

- Softmax Activation: The final Dense layer employs the softmax activation function to classify input images into one of the 10 classes represented in the CIFAR-10 dataset.

This project underscores the effectiveness of CNNs in image classification tasks and showcases the capabilities of TensorFlow 2 in developing and deploying deep learning models for practical applications.
