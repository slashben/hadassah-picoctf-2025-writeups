# CTF Challenge: flags are stepic (Forensics)
<img width="924" height="875" alt="Screenshot 2025-07-28 032921" src="https://github.com/user-attachments/assets/ea0782b4-d6e6-4bd9-9c83-42f5e2f298d9" />

## Challenge Description
A group of hackers was suspected of using steganography to hide messages in image files on a legitimate-looking website. Your task was to uncover their hidden communication.

**Challenge Type**: Forensics/Steganography  
**Difficulty**: Medium  
**CTF**: picoCTF 2025  

## Solution Walkthrough

### Step 1: Analyzing Clues
- **Key Hint**: "In the country that doesn't exist, the flag persists"
- Discovered reference to "Upanzi, Republic The" (fictional country)
- Located suspicious PNG file: `upz.png`

### Step 2: Steganography Detection
1. Installed required tool:
   ```bash
   pip install stepic pillow
<img width="1250" height="852" alt="Screenshot 2025-07-28 033510" src="https://github.com/user-attachments/assets/3d11d6b6-49c5-4da4-8b3f-c2b1f2eeee03" />
<img width="1608" height="179" alt="Screenshot 2025-07-28 033215" src="https://github.com/user-attachments/assets/35bf4513-85e4-4a96-b520-7c097ea1a4a7" />
<img width="217" height="162" alt="Screenshot 2025-07-28 033011" src="https://github.com/user-attachments/assets/b49ae244-d11d-4923-bb60-ff3fbec43041" />
<img width="1691" height="877" alt="Screenshot 2025-07-28 032936" src="https://github.com/user-attachments/assets/e1ed1314-1b74-4fd8-aed6-49ddc424b48d" />
<img width="949" height="787" alt="Screenshot 2025-07-28 034445" src="https://github.com/user-attachments/assets/85fffd2d-d02d-419a-aa06-62e216921ecd" />
<img width="919" height="809" alt="Screenshot 2025-07-28 034457" src="https://github.com/user-attachments/assets/d425c018-cb53-4fd4-8226-c8301f08fc1c" />


picoCTF{fl4g_h45_fl4g6f5548ea}
