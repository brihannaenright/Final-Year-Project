import cv2
from luminance import luminance_map
import numpy as np
import matplotlib.pyplot as plt

#Loads the video
cap = cv2.VideoCapture("data/generated/flash_2hz.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)  


prev_lum = None
frame_number = 0

times = []
max_changes = []
changed_fractions = []
change_brighter = []
change_darker = []


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
        brighter_fraction = (change >= +0.1).mean()
        darker_fraction = (change <= -0.1).mean()

        times.append(frame_number / fps)
        max_changes.append(biggest)
        changed_fractions.append(fraction)
        change_brighter.append(brighter_fraction)
        change_darker.append(darker_fraction)

    prev_lum = lum
    frame_number += 1

cap.release()
print(f"Compared {len(times)} pairs of frames")
print(f"Largest change in the whole video: {max(max_changes):.3f}")

fig, (brighter, darker) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))

brighter.plot(times, change_brighter)
brighter.set_ylabel("Fraction of pixels\nchanged by >= 0.1")
brighter.set_xlabel("Time (seconds)")

darker.plot(times, change_darker)
darker.set_ylabel("Fraction of pixels\nchanged by <= -0.1")
darker.set_xlabel("Time (seconds)")

plt.tight_layout()
plt.savefig("notes/04_flash_2hz.png")
plt.show()