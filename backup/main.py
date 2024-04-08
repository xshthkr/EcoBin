import classification_2
import controller
import image_capture

import time

# capture image
image_capture.capture()

captured_image_path = "/home/rpi/Downloads/DATASET_2/TEST/test.jpg"
captured_image = load_and_preprocess_image(captured_image_path)

# Flatten the test image
captured_image_flattened = captured_image.reshape(1, -1)

# Make prediction on the single test image
predicted_label = knn_classifier.predict(captured_image_flattened)[0]

# Print the predicted label
print("Predicted Label:", predicted_label)




# control motor based on prediction

if predicted_label == "O":
	controller.clockwise()
	time.sleep(3)
	controller.counterclockwise()
	time.sleep(3)
	controller.stop()

elif prediction == "R":
	controller.counterclockwise()
	time.sleep(3)
	controller.clockwise()
	time.sleep(3)
	controller.stop()
