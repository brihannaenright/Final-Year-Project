import cv2
from luminance import luminance_map
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

    start = time.perf_counter()  
    lum_map = luminance_map(frame)
    brightness = lum_map.mean()
    elapsed = time.perf_counter() - start
    print(f"Took {(elapsed)*1000:.3f} ms to calculate brightness\n Total Brightness: {brightness:.6f}")
    break
                
    #Press Q to quit
    #waitKey() adds a delay in-between frames (I have set it to 100 for safety, usually 25)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()