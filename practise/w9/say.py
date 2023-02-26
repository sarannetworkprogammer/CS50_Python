import cowssay
import pyttsx3

engine = pyttsx3.init()

this = input("whats this? ")

cowsay.cow(this)
engine.say(this)

engine.runAndWait()