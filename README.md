# Hand Tracking using MediaPipe and OpenCV

## About The Project

This Python script utilizes OpenCV and MediaPipe to perform real-time hand tracking using a webcam. The code captures video input from the default camera, processes the frames to detect and track hand landmarks using the MediaPipe Hands module, and subsequently visualizes the landmarks on the live feed.

For each detected hand, the script identifies and prints the coordinates of the landmarks, with a distinctive filled circle highlighting the first landmark (index 0). The frame rate is calculated and displayed in the corner, providing insights into the processing speed.

Overall, this script combines the power of computer vision libraries to create a hands-on experience, quite literally, by bringing hand-tracking capabilities to your fingertips. It's a practical demonstration of the intersection between software and real-world interaction, opening doors to diverse applications such as virtual reality, gaming, and accessibility interface.

## Built With

- Opencv
- Mediapipe

## Local Setup

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. Clone the repo

   ```sh
   git clone https://github.com/pedropcamellon/hand-tracking-mediapipe-opencv.git
   cd hand-tracking-mediapipe-opencv
   ```

2. Install the required libraries using poetry

   ```sh
   poetry install
   ```

3. Run the Project

   ```sh
   python app.py
   ```
