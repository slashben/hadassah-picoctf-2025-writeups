


![scrambled2](https://github.com/user-attachments/assets/233e4b70-ddae-472c-956d-7d5976c8a7e5)
![scrambled2](https://github.com/user-attachments/assets/ccc3d02b-e495-4d31-af24-e26c92973e9d)



you run this code which contains the two images from the website 
you need to combine the two images in order to get the flag 
once you get the image generated you need to edit the pictures lightening in order to see the flag 
clearly 




# Install dependencies (only needed once)
!pip install pillow numpy

from PIL import Image
import numpy as np
from google.colab import files

# Upload images
uploaded = files.upload()

# Make sure the files are named correctly
im1 = Image.open("scrambled1.png")
im2 = Image.open("scrambled2.png")

# Convert images to numpy arrays
im1np = np.array(im1)
im2np = np.array(im2)

# XOR the two images
result = np.bitwise_xor(im1np, im2np).astype(np.uint8)

# Save the result
Image.fromarray(result).save("flag.png")

# Download the result
files.download("flag.png")



this is the image you get after using the code to combine 
![image](https://github.com/user-attachments/assets/ce9a566b-e82f-4430-a170-76bcddd8ee2c)


