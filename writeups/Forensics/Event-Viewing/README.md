# Event-Viewing
This is the write-up for the challenge "Event-Viewing" in PicoCTF

# The challenge
The challenge included an .evtx file — a Windows Event Log file format introduced in Windows Vista to replace the older .evt format. These files contain structured XML-based records of system and application events.
In this challenge, the scenario unfolds as follows:
1.	The user installed software using an installer they downloaded from the internet.
2.	Upon running the installed software, it appeared to do nothing.
3.	However, from that point on, every time they boot up and log in to their computer, a black command prompt window briefly flashes on the screen before the system instantly shuts down.
Your task is to analyze the event logs and find evidence for each of these actions — and in doing so, recover the flag (divided into 3 parts) from the relevant events.

## description
The link of the challenge: https://play.picoctf.org/practice/challenge/456 
Go into the link. <br>
You should see this page:
 
![challenge](./challenge.png) 
 
Download the logs file
![Windows_Logs](./Windows_Logs.evtx)

## How to solve it
I performed a manual scan of the log file and organized the events in the following order:
1.	By timestamp
2.	Then by source
3.	And finally, by Event ID
I identified the following events as suspicious:
1.	Install – Event ID 1033
2.	Registry Change – Event ID 4657
3.	Shutdown – Event ID 1074
Each of these events contained a part of the flag:
1.	cGljb0NURntFdjNudF92aTN3djNyXw==
2.	MXNfYV9wcjN0dHlfdXMzZnVsXw==
3.	dDAwbF84MWJhM2ZlOX0=
I used CyberChef to decode the Base64-encoded strings and reconstruct the full flag:
picoCTF{Ev3nt_vi3wv3r_1s_a_pr3tty_us3ful_t00l_81ba3fe9}

The challenge is solved.


