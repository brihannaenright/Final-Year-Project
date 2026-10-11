# using OpenCV for working with videos
# https://www.geeksforgeeks.org/python/python-play-a-video-using-opencv/

# Capturing the frame rate of a video
# https://stackoverflow.com/questions/24361771/frame-rate-of-video-python

# Editing the resolution of a video
# https://www.geeksforgeeks.org/python/how-to-change-video-resolution-in-opencv-in-python/

# Retrieving pixel values
# https://stackoverflow.com/questions/55827496/how-to-read-pixels-from-a-specific-video-frame


import cv2
from luminance import relative_luminance
import time

#Loads the video
cap = cv2.VideoCapture("data/potNoodleAdvert.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"FPS: {fps}\n Frame Count: {frame_count}\n Resolution: {video_width} x {video_height}")    

while True:
    #Fetches each frame
    ret, frame = cap.read()
    if not ret:
       break        # No more frames - end of video

    #Displays the frames   
    cv2.imshow("Video", frame)
    #Captures the resolution of each frame (h, w, values per pixel)
    height, width, channels = frame.shape
    start = time.perf_counter()  
    total = 0;      
    for x in range (0, width):
        for y in range(0, height):
            r = frame[y, x, 2]
            g = frame[y, x, 1]
            b = frame[y, x, 0]
            total = total + relative_luminance(r, g, b)
    brightness = total/(width*height)
    elapsed = time.perf_counter() - start
    print(f"Took {elapsed:.2f} seconds to calculate brightness\n Total Brightness: {brightness:.2f}")
    break
                
            

    #Press Q to quit
    #waitKey() adds a delay in-between frames (I have set it to 100 for safety, usually 25)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()