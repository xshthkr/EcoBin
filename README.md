# EcoBin: kNN-Waste-Segregation
EcoBin is a waste segregation smart dustbin that classifies and separates recyclable and organic waste. This project has been submitted to the CS210 Artificial Intelligence semester final at NIT Surat, 2024.

This repository holds the ```.py``` files for the Raspberry Pi module of EcoBin. This repository DOES NOT include the dataset used in the KNN model.


## Members of Team EcoBin
- Shashank Thakur, U22CS060
- Kevalya Shah, U22CS021
- Misbah Shaikh, U22CS043
- Raj Vadodaria, U22CS077


## Custom Modules
- `classification.py`: This module is responsible for classifying waste images using the k-Nearest Neighbors (kNN) algorithm. It loads the kNN model, preprocesses the input image, and predicts the class of the waste.
- `image_capture.py`: This module captures and saves a frame image from the webcam to a specified path.
- `motor_controller.py`: This module controls a DC motor.
- `servo_controller.py`: This module controls one or more servo motors.
- `servo_controller_threaded.py`: This module controls 2 servos in parallel.
- `main.py`: This is the main module that assembles the components of all other modules for the project.


## Components
- KNN model for waste classification
- Raspberry Pi 3 B+
- Servo motors


## Installation and Setup
1. Clone this repository to your local machine.
2. Install the necessary Python libraries with `pip install -r requirements.txt`.
3. Run `python main.py` to start the program.
