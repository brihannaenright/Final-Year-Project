# Using openCV for generating videos
# https://opencv.org/reading-and-writing-videos-using-opencv/#h-writing-a-video-in-opencv

import numpy as np
from luminance import luminance_map
import cv2

frame1 = np.full((1080, 1920, 3), 64, dtype=np.uint8)
frame2 = np.full((1080, 1920, 3), 128, dtype=np.uint8)

print(f"Frame 1 Luminance: {luminance_map(frame1)[0, 0]}\n Frame 2 Luminance: {luminance_map(frame2)[0, 0]}\n")

fps = 30
rate = 5
duration = 3

writer = cv2.VideoWriter(f"data/generated/flash_{rate}hz_1080p.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (1920, 1080))


for i in range (duration*fps):
    t = i/fps
    state = int(t * 2 * rate) % 2
    if(state==0):
        writer.write(frame1)
    else:
        writer.write(frame2)

writer.release()