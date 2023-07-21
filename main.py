import os
from time import sleep
import pyjokes
import wikipedia as wb
import pyautogui as pag
from Features.base import takeCommand, wishme, time, open_chrome
from Features.custom_voices import speak
import subprocess

from Features.playSong import play_songs

#Da Loop:
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "good morning" in query:
            speak("good morning master")
        elif "time" in  query:
            time()
        elif "chrome" in query:
            open_chrome()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wb.summary(query, sentences = 2)
            speak(result)
        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "joke" in query:
            speak(pyjokes.get_jokes())

        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")
        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            speak('restarting in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")

        elif "open notepad" in query:  # if open notepad in statement
            speak("opening notepad")  # speak
            location = "C:/WINDOWS/system32/notepad.exe"  # location
            notepad = subprocess.Popen(location)  # location of a software you want tot opem

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()  # terminate

        #================================================pag====================================================
        elif "hidden menu" in query:
        #win + x for hidden menu
            pag.hotkey('winleft','x')
        elif "task manager" in query:
        # Ctrl+Shift+Esc: Open the Task Manager
            pag.hotkey('ctrl', 'shift', 'esc')
        elif "task view" in query:
        # Win+Tab: Open the Task view
            pag.hotkey('winleft', 'tab')

        elif "take screenshot" in query:
        # win+perscr
            pag.hotkey('winleft', 'prtscr')
            speak("done")

        # Take screenshot save in Given location

        #elif "take screenshot" in query:
        #    img = pag.screenshot()
        #    img.save("D:/screenshot_1.png")  # file mane and location
        #    speak("Done")

        elif "snip" in query:
            pag.hotkey('winleft', 'shift', 's')
        elif "close the app" in query:
            pag.hotkey('alt','f4')
        elif "setting" in query:
        # win+i = open setting
            pag.hotkey('winleft', 'i')
        elif "new virtual desktop" in query:
        # Win+Ctrl+D: Add a new virtual desktop
            pag.hotkey('winleft', 'ctrl', 'd')

        elif "play songs" in query:
            play_songs()