import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hallo, guten Morgen")
        print("Hallo, guten Morgen")
    elif hour>=12 and hour<18:
        speak("Hallo guten Tag")
        print("Hallo guten Tag")
    else:
        speak("Hallo guten Abend")
        print("Hallo guten Abend")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='de-at')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Bitte Wiederholen sie sich")
            return "None"
        return statement

while True:
    while True:
        statement = takeCommand().lower()
        if 'hey pai' in statement:
            break

    if __name__=='__main__':


        while True:
            speak("Wie kann ich dir helfen?")
            statement = takeCommand().lower()
            if statement==0:
                continue

            elif 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)


            elif 'öffne youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube ist jetzt offen")
                time.sleep(2)

            elif 'öffne google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google ist jetzt offen")
                time.sleep(2)

            elif 'öffne gmail' in statement:
                webbrowser.open_new_tab("https://www.gmail.com")
                speak("gmail ist jetzt offen")
                time.sleep(2)

            elif 'zeit' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Es ist {strTime}")
                print(f"Es ist {strTime}")
                time.sleep(2)

            elif 'wetter' in statement:
                api_key="6fe978f2e9ea1220f05602b05d64984b"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("In welcher Stadt?")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                    print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))
                time.sleep(2)

            if "off" in statement or "ausschalten" in statement or "stop" in statement or "stopp" in statement or "nichts" in statement:
                speak('Wird ausgeschaltet...')
                print('Wird ausgeschaltet...')
                break