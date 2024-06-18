import cv2
import os

# Create a directory to save frames if it doesn't exist
output_dir = 'frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

video_capture = cv2.VideoCapture('Garden Video.mp4')

def getFrame(sec, count):
    video_capture.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = video_capture.read()
    if hasFrames:
        # Save frame as PNG file
        cv2.imwrite(os.path.join(output_dir, f"image{count}.jpg"), image)
    return hasFrames

sec = 0
frameRate = 0.5  # Capture an image every 0.5 second
count = 1

success = getFrame(sec, count)
while success:
    count += 1
    sec += frameRate
    sec = round(sec, 2)
    success = getFrame(sec, count)

print(f"Extracted {count - 1} frames from the video.")
