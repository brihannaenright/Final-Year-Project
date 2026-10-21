# Feasibility Summary

Findings from my technical feasibility study, 06/10/2026 – 22/10/2026.

---

## 1. Detection Thresholds (WCAG 2.2)

**Source:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/) – most recent publication (12/12/2024)

### Guideline 2.3: Seizures and Physical Reactions

| Success criterion                      | Level | Requirement                                                                                                                                                      |
| -------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.3.1 Three Flashes or Below Threshold | A     | Web pages do not contain anything that flashes more than three times in any one-second period, or the flash is below the general flash and red flash thresholds. |
| 2.3.2 Three Flashes                    | AAA   | Web pages do not contain anything that flashes more than three times in any one-second period.                                                                   |
| 2.3.3 Animation from Interactions      | AAA   | Motion animation triggered by interaction can be disabled, unless the animation is essential to the functionality or the information being conveyed.             |

### Definitions

- **General flash:** a pair of opposing changes in relative luminance of 10% or more of the maximum relative luminance (≥ 0.1), where the relative luminance of the darker image is below 0.80.
  - A _pair of opposing changes_ is an increase followed by a decrease, or a decrease followed by an increase.
- **Red flash:** any pair of opposing transitions involving a saturated red.
- **Area threshold:** content fails only if the combined area of flashes occurring at the same time occupies more than 0.006 steradians within any 10° visual field on the screen (25% of any 10° visual field).

### Progress

**Implemented**

- Experiment 01 and 02 works on calculating average brightness across a frame, returns the brightness for each frame
- Experiment 03 and 04 work on comparing same position/pixel in two neighbouring frames and calculating the change between them

**Not yet implemented**

- Counting flashes per second
- Local area rule (25% of any 10° field)
- Red flashes
- Darker area below 0.80

## 2. Generating Test Data

### Progress

**Implemented**

- Experiment 05 works on creating a video, with two frames flashing a specific rate within a second
- Generated flash_2hz.mp4 which flashes 2 times a second, under the flash threshold
- Generated flash_5hz.mp4 which flashes 5 times a second, over the flash threshold

**Not yet implemented**

- More tests, breaching other thresholds stated above

**Problems I've Encountered**

- After saving videos, luminance change has dropped

## 3. Input Format

- Speed (average of 20 runs):
  | Test | ms per frame | Fits in 33.3 ms (30 fps)? |
  | --- | --- | --- |
  | 320x240 video frame (14 Oct) | 7.0 | Yes |
  | 1920x1080 full size | 251 | No - ~7.5x too slow |
  | 1080p resized to 320x240 + luminance | 9.6 | Yes - ~24 ms spare |

**Problems I've Encountered**

- As fps increases, our time budget gets smaller e.g. 60 fps = 1000/60 - 16.7ms a frame
- 1920 x 1080p video cannot be analysed live with the current approach
- As I added detection for more thresholds, 320x240 may not even be feasible for 30fps

**Solutions**

[Python Speed-up](https://pythonspeed.com/articles/different-ways-speed/)

- Attempt to speed up current solution: lookup tables, parallelisation, C++ etc..
- Keep tool strictly as video upload
- Browser Extension - use content scripts to read video before user has seen it
  [Content Scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts)
  [Video Overlay](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement)
  [Bounding Element](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect)
- Live capture, but resize video or skip frames

## 4. Storing videos

- 1080x1920x3 = 6,220,800 bytes ~6.2MB
- 30 fps: 6.2 x 30 = 187MB per second
- 187 x 60 = 11.2GB per minute of video

- Compression of videos lose detail = lossy vs lossless
- Encoding video takes time and lots of computation
- Woulld have to demux, decode, analyse, modify, encode and mux for each video
- Need FFmpeg to copy audio back in to opencv video
- Live content only has to analyse and modify

## 5 Machine Learning

- Flikcer paper - mentions they use CNN, combining LSTM (for pattern recognition) and RNN. Doesn't describe how these are used.
- Well-known tools are rule based: PEAT, Harding, EA's IRIS
- ML could be used in video editing/modifying, detecting spatial patterns (e.g. someone wearing striped shirt, escalator)
- ITU-R describes harmful patterns, could be used as thresholds
- Could use a CNN stripe detector, train on images of stripes, easy to label
- Limited data, hard to explain why something failed
