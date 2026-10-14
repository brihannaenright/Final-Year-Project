import cv2
from luminance import luminance_map
import numpy as np
import matplotlib.pyplot as plt

#Loads the video
cap = cv2.VideoCapture("data/potNoodleAdvert.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)  


prev_lum = None
frame_number = 0

times = []
max_changes = []
changed_fractions = []


while True:
    ret, frame = cap.read()
    if not ret:
       break        # No more frames - end of video

    lum = luminance_map(frame)

    if prev_lum is not None:
        change = lum - prev_lum
        abs_change = np.abs(change)     #The change of brightness, ignoring direction

        biggest = abs_change.max()

        fraction = (abs_change >=0.1).mean()

        times.append(frame_number / fps)
        max_changes.append(biggest)
        changed_fractions.append(fraction)

    prev_lum = lum
    frame_number += 1

cap.release()
print(f"Compared {len(times)} pairs of frames")
print(f"Largest change in the whole video: {max(max_changes):.3f}")

fig, (top, bottom) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))

top.plot(times, max_changes)
top.axhline(0.1, color="red", linestyle="--", label="WCAG 0.1 threshold")
top.set_ylabel("Largest pixel change")
top.legend()

bottom.plot(times, changed_fractions)
bottom.set_ylabel("Fraction of pixels\nchanged by >= 0.1")
bottom.set_xlabel("Time (seconds)")

plt.tight_layout()
#plt.xlim(20,21)
plt.savefig("notes/03_frame_differences.png")
plt.show()