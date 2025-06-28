Description : "Can you handle APKs?"
Since I have some experince with APKS I took this one.

1) I downloaded the apk.
2) first hint is : "Did you know you can unzip APK files?" - so I unzipped them.
3) I have lots of files so I went over the directories to see if I found something interesting.
4) most of the files are xml files so Im not sure what to do with them
5) I found interesting txt file between lots of xml files named "flag" so I opened it.
the file is under res/color directory.
6) The content of the file is a string : "7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f61336562356163327d"
so it looks like a hash?
7) Now I use CyberChef which is one of my favorit tools
8) first I try base64 but its not this one
9) I tried HEX and found the flag : picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_a3eb5ac2}
