# TRICKSTER
This is the write-up for the challenge "Trickster" challenge in PicoCTF

# The Challange
## Description
I found a web app that can help process images: PNG images only! http://atlas.picoctf.net:63035/
## Hints
(none)

## Initial look
Leads to a webpage titled as a PNG processing app. There is a 'choose file' button and an 'upload file' button.

# How to solve it
Uploading a png file is successful.
I guessed the uploaded files are stored in http://atlas.picoctf.net:63035/uploads/filename
[img 1] 

I tried to upload a blank file and recieved the message: 
> "Error: File name does not contain '.png'."

This suggested that the site checks only for `.png` in the filename.
[img 2]

Next, I renamed a JPEG file to `a .png file.jpeg` and tried uploading it.  
This time, the error message changed to:  
> "Error: The file is not a valid PNG image: ffd8ffe0"

From this, I concluded the server also performs a **file signature** check to ensure it's a valid PNG.

### Bypassing the checks
The goal was to trick the server into accepting a file that could **execute code**, a **PHP webshell**.

1. The upload filter allows filenames that **contain `.png`**, even if it’s not the extension.
2. The server checks the **file signature**, so I added PNG to the top of the PHP file.
3. I named the PHP webshell: `webshell.png.php`

entering the URL: http://atlas.picoctf.net:63035/uploads/webshell.png.php gave me access:

[img 3]

Using `ls -a /` I saw there is a challenge dir, but I have no permission to access it. After some exploration I tried `ls -a /var/www/html` and found an interestingly named file

[img 4]

Using cat I looked into it and found the flag: **picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_d3ac625b}**


