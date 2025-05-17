import cv2
import mediapipe as mp
import time
import logging
import argparse
import os

# Setup argument parser
parser = argparse.ArgumentParser(description="Hand tracking with MediaPipe")
parser.add_argument(
    "--video_path",
    type=str,
    default="0",
    help="Path to video file (default: use webcam)",
)
args = parser.parse_args()

# Setup video capture from file or webcam
if args.video_path != "0":
    if not os.path.exists(args.video_path):
        raise FileNotFoundError(f"Video file not found: {args.video_path}")
    cap = cv2.VideoCapture(args.video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Video properties: {total_frames} frames, {fps} FPS")
else:
    cap = cv2.VideoCapture(0)

# Load MediaPipe hands model
mphands = mp.solutions.hands
hands = mphands.Hands(False)
mpDraw = mp.solutions.drawing_utils

# Initialize time variables
pTime = 0
cTime = 0

# For continuous video capture
while True:
    success, img = cap.read()

    if not success:
        logging.error("Failed to capture video frame")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # below code is for drawing the landmarks on the hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)

    # Elapsed time and fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display fps
    cv2.putText(
        img=img,
        text=f"{int(fps)} fps",
        org=(10, 30),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=2,
        color=(255, 0, 255),
        thickness=2,
    )

    # Display video progress if using file
    if args.video_path != "0":
        current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        progress = int((current_frame / total_frames) * 100)
        cv2.putText(
            img=img,
            text=f"Progress: {progress}%",
            org=(10, 60),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=2,
            color=(255, 0, 255),
            thickness=2,
        )

    # Display the image
    cv2.imshow("Image", img)

    # Break if 'q' pressed or video ends
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Add a delay to reduce CPU usage
    time.sleep(0.1)

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
