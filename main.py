import pyttsx3
import threading

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
while True:
    x = threading.Thread(target=speak, args=("Du stinkst",))
    x.start()
