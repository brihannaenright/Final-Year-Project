from luminance import luminance_map
import time
import cv2

runs = 20
cap = cv2.VideoCapture("data/generated/flash_5hz_1080p.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
       break

    start = time.perf_counter()
    for _ in range(runs):
        small = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)
        luminance_map(small)
    elapsed = time.perf_counter() - start

per_frame_ms = (elapsed / runs) * 1000
print(f"luminance_map at 1080p: {per_frame_ms:.2f} ms per frame")