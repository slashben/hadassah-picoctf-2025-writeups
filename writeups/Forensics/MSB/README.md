## Challenge Description

This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...

## Challenge Link
https://play.picoctf.org/practice/challenge/359?category=4&difficulty=2&page=1

---
## Files Provided

The challenge provided a single image file:

* `Ninja-and-Prince-Genji-Ukiyoe-Utagaw<img width="1074" height="1500" alt="Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada flag" src="https://github.com/user-attachments/assets/102f6e42-7c70-4751-995e-226ac37289a3" />

---
## Solution Approach

The core task was to extract a hidden flag from an image file. The challenge description and the file's visual "corruption" were the main clues.

### 1. Identifying the Steganography Technique

The challenge title "MSB" and the description's focus on "visual artifacts" strongly suggested that the flag was hidden using **MSB (Most Significant Bit) steganography**, not the more common LSB (Least Significant Bit) method. LSB changes are typically invisible, while MSB changes create significant visual noise, which matched the provided image perfectly. The strategy was to isolate and view the individual bit planes of the image to find the hidden data.

### 2. Extraction Using an Online Tool

An online steganography tool was used to analyze the image's bit planes without needing to write a script.

* **Tool Selection:** An online tool with a "Bit Plane" analysis feature was chosen, such as the one at [StegOnline](https://stegonline.georgeom.net/upload).


* **Step 1: Visual Analysis with "Browse Bit Planes"**
    * The `Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.jpg` image was uploaded to the tool.
    * I used the **"Browse Bit Planes"** feature to inspect each bit plane (0-7) for all three color channels (RGB).
    * This visual inspection confirmed that the flag's text was clearly visible within **Bit Plane 6** of the Green channel (and also present in Red and Blue).
<img width="1158" height="1432" alt="blue" src="https://github.com/user-attachments/assets/6a626031-a3df-459f-b62b-f35112c8810d" />
<img width="1006" height="1404" alt="green" src="https://github.com/user-attachments/assets/8993296d-e09b-4b79-912a-1890fc69d111" />
<img width="1012" height="1428" alt="red" src="https://github.com/user-attachments/assets/59eedee0-f88e-4cc2-84fb-1d315f0c1947" />

* **Step 2: Extracting the Data**
    * After identifying that the data was in Bit Plane 6, I returned to the main tool interface.
    * I used the **"Extract Files/Data"** feature. This function is designed to pull raw data from the bit planes.
    * The tool extracted the contents from the bit planes into a downloadable file.
  <img width="1522" height="882" alt="Screenshot 2025-07-25 121000" src="https://github.com/user-attachments/assets/ea95bd13-00fc-4921-805d-cc1f036b515c" />


* **Step 3: Finding the Flag**
    * I opened the extracted data file with a text editor.
    * A simple text search for `picoCTF` within the file immediately revealed the full flag.
  <img width="3834" height="2012" alt="picoflag" src="https://github.com/user-attachments/assets/5eef680a-2919-414c-962d-b48462cc7c8b" />



---
## Flag

picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_ee3cb4d8}
