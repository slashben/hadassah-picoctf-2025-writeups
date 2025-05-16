import numpy as np
from PIL import Image

# Open the images
image1 = Image.open(r"C:\Users\orsha\Downloads\scrambled1.png")
image2 = Image.open(r"C:\Users\orsha\Downloads\scrambled2.png")

# Convert to Numpy arrays
iamge1np = np.array(image1)
iamge2np = np.array(image2)

# Perform pixel-wise addition between the images
result = iamge2np + iamge1np

# Convert back to PIL image and save
Image.fromarray(result).save('resultImage.png')
