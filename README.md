# Scripter
## Introduction
Scripter is a Tkinter based text editor similar to Notepad with added functionalities like text-to-speech, 
theme setting and more. It serves the basic features as well like open a text file, save file
and font and appearance as per user's need.
## Modules Used:
### pyttsx3
 * pyttsx3  is a text-to-speech conversion library in Python. <br /> 
 * Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
### Installation
 * pip install pyttsx3<br /> 
 * If you recieve errors such as No module named win32com.client,<br /> 
 * No module named win32, or No module named win32api, you will need to additionally install pypiwin32.
 ### Usage:
  import pyttsx3<br />
  engine = pyttsx3.init()<br />
  engine.say("I will speak this text")<br />
  engine.runAndWait()<br />
