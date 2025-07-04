import cv2
import mediapipe as mp
import os
import time

# Change the video file path to your own file
video_path = os.path.join("data", "video_input.mp4")
cap = cv2.VideoCapture(video_path)

# Get video details for the output video
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_video_path = "output_video.mp4"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

mphands = mp.solutions.hands
hands = mphands.Hands(False)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    if not success:
        break  # Break the loop if the video ends or there is an issue reading the video

    # Reduce the image size to half for faster processing
    img = cv2.resize(img, (width, height))

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

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
    )

    cv2.imshow("Image", img)

    # Write the frame to the output video
    out.write(img)

    # Break the loop and close the window when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Add a delay to reduce CPU usage
    time.sleep(0.1)

# Release the video file, output video, and close the window
cap.release()
out.release()
cv2.destroyAllWindows()
