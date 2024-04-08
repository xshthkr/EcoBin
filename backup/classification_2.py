import os
import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

train_folder = "/home/rpi/Downloads/DATASET_2/TRAIN"

# Function to load and preprocess a single image
def load_and_preprocess_image(image_path, target_shape=(100, 100)):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image from {image_path}")
        return None
    # Resize image to target shape
    img = cv2.resize(img, target_shape)
    return img

# Load and preprocess training data
images_train = []
labels_train = []
for label in os.listdir(train_folder):
    path = os.path.join(train_folder, label)
    if os.path.isdir(path):  # Check if it's a directory
        for filename in os.listdir(path):
            img_path = os.path.join(path, filename)
            img = load_and_preprocess_image(img_path)
            if img is not None:
                images_train.append(img)
                labels_train.append(label)

# Convert images to numpy array
images_train = np.array(images_train)

# Flatten images
images_train_flattened = images_train.reshape(images_train.shape[0], -1)

# Create and train KNN classifier
k = 2  # Adjust k as needed
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(images_train_flattened, labels_train)

# Load the single test image
test_image_path = "/home/rpi/Downloads/DATASET_2/TEST/test.jpg"
test_image = load_and_preprocess_image(test_image_path)

if test_image is None:
    print("No test image found.")
else:
    # Flatten the test image
    test_image_flattened = test_image.reshape(1, -1)

    # Make prediction on the single test image
    predicted_label = knn_classifier.predict(test_image_flattened)[0]

    # Print the predicted label
    print("Predicted Label:", predicted_label)
