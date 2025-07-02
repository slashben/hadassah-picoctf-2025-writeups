The link of the challenge: [Challenge Link](https://play.picoctf.org/practice/challenge/265?category=4&difficulty=2&page=2)

Go to the link and you should see this:
![challenge_link](./img/enhance_start.png)

Click on "Download image file" and download the file **drawing.flag.svg** <br>
![file](./img/file_screenshot.png)
<br>
thats whats inside:
![inspect css](./img/file_img.png)

Open the Terminal and type the command **"strings drawing.flag.svg"**:
![terminal command](./img/part1.png)

The command will show all the readable text from the file:
![readable text](./img/part2.png)

We cannot really understand and see something unusual from the readable text, <br>
so lets try to find the "{" symbol for the flag by the command **strings drawing.flag.svg | grep "{"** :
![look for a symbol](./img/part3.png)

Found something that looks like the middle of the flag text. <br>
lets find more **tspan** tags by using the command **strings drawing.flag.svg | grep "tspan" :
![find the flag](./img/part4.png)

The flag is found inside the tspan tags! <br>
enter the flag into the challenge text-box:
![solved](./img/finish.png)
:trophy: the challenge is **solved**.  

#### The flag is: picoCTF{3nh4nc3d_aab729dd}
