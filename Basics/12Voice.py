#pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()

name = input("Enter Your Name : ")

engine.say(f"Hello {name}")

engine.runAndWait()