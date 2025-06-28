


![scrambled2](https://github.com/user-attachments/assets/233e4b70-ddae-472c-956d-7d5976c8a7e5)
![scrambled2](https://github.com/user-attachments/assets/ccc3d02b-e495-4d31-af24-e26c92973e9d)



you run this code which contains the two images from the website 
you need to combine the two images in order to get the flag 
once you get the image generated you need to edit the pictures lightening in order to see the flag 
clearly 





!pip install pillow numpy

from PIL import Image
import numpy as np
from google.colab import files

uploaded = files.upload()


im1 = Image.open("scrambled1.png")
im2 = Image.open("scrambled2.png")


im1np = np.array(im1)
im2np = np.array(im2)


result = np.bitwise_xor(im1np, im2np).astype(np.uint8)

Image.fromarray(result).save("flag.png")

files.download("flag.png")



this is the image you get after using the code to combine 
![image](https://github.com/user-attachments/assets/ce9a566b-e82f-4430-a170-76bcddd8ee2c)

which contains the FLag : picoCTF{d72ea4af}

