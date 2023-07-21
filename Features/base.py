import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import pyjokes
import os
from time import sleep
import subprocess
import pyautogui as pag
from Features.custom_voices import speak

engine = pyttsx3.init()  # initialise pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-2 range for different voices
voicespeed = 175  # setting speed
engine.setProperty('rate', voicespeed)

#takeCommand function:
def takeCommand():
    """Listen for a command from the user and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print()
        return "---"
    return query

#time function:
def time():
    """Speak the current time."""
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)

#WishMe Function:
def wishme():
    speak("welcome back Master, please be gentle this time")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak('Good morning')
    elif hour>=12 and hour<=18:
        speak('Good afternoon')
    elif hour>=18 and hour<=24:
        speak('Good evening')
    else:
        speak('good night')
    speak('How can i help you today')

#OPopen Chrome
def open_chrome():
    url = 'https://google.co.in/'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    wb.get(chrome_path).open(url)

def openDungeon():
    url = 'https://hitbdsm.com/'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    wb.get(chrome_path).open(url)
