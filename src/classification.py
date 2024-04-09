# kNN Waste Classification Model

# This is a module to classify waste images using the k-Nearest Neighbors (kNN) algorithm.
# This script is used to classifies waste images using the KNN algorithm.
# It loads the training data from the specified folder, classifies the test image, and displays the result using matplotlib.

import os
import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


class ImageClassifier:


    def __init__(self, train_folder):
        print("[ECOBIN] >> Starting KNN waste classification model...")
        self.train_folder = train_folder
        self.knn_classifier = None


    def load_training_data(self):
        print("[ECOBIN] >> Loading traning data...")
        images_train = []
        labels_train = []
        for label in os.listdir(self.train_folder):
            path = os.path.join(self.train_folder, label)
            if os.path.isdir(path):
                for filename in os.listdir(path):
                    img_path = os.path.join(path, filename)
                    img = self.load_and_preprocess_image(img_path)
                    if img is not None:
                        images_train.append(img)
                        labels_train.append(label)
        images_train = np.array(images_train)
        images_train_flattened = images_train.reshape(images_train.shape[0], -1)
        self.knn_classifier = KNeighborsClassifier(n_neighbors=3)
        self.knn_classifier.fit(images_train_flattened, labels_train)


    def load_and_preprocess_image(self, image_path, target_shape=(100, 100)):
        img = cv2.imread(image_path)
        if img is None:
            print(f"[ECOBIN] >> Error: Unable to load image from {image_path}")
            return None
        img = cv2.resize(img, target_shape)
        return img


    def classify_image(self, image_path):
        print("[ECOBIN] >> Classifying image...")
        test_image = self.load_and_preprocess_image(image_path)
        if test_image is None:
            print("[ECOBIN] >> No image found.")
        else:
            test_image_flattened = test_image.reshape(1, -1)
            predicted_label = self.knn_classifier.predict(test_image_flattened)[0]

            plt.imshow(test_image)
            plt.title(f"Predicted Label: {predicted_label}")
            plt.axis('off')
            plt.show()

            return predicted_label
            
            
if __name__ == "__main__":
    
    train_folder = "/home/rpi/Downloads/DATASET_2/TRAIN"
    model = ImageClassifier(train_folder)
    model.load_training_data()
    path_to_image = "/home/rpi/Downloads/DATASET_2/TEST/test.jpg"
    result = model.classify_image(path_to_image)
    print("Predicted Label:", result)
