import os
import pygame as pg
voice2 = 'ja-JP-NanamiNeural'
def speak(data):
    voice = 'en-US-SteffanNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)
    pg.init()
    pg.mixer.init()
    pg.mixer.music.load("data.mp3")
    try:
        pg.mixer.music.play()
        while pg.mixer.music.get_busy():
            pg.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pg.mixer.music.stop()
        pg.mixer.quit()