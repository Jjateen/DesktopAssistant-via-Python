import openai
import os
import pygame
import config
import speech_recognition as sr
#voice = "en-US-ChristopherNeural"
openai.api_key = config.Api


def takeCommand():
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

def speak(data):
    voice1 = "en-GB-SoniaNeural"
    voice3= "ja-JP-NanamiNeural"
    # Split the input text into chunks
    chunks = data.split()
    chunk_size = 100
    chunks = [chunks[i:i + chunk_size] for i in range(0, len(chunks), chunk_size)]

    # Convert and play each chunk
    for chunk in chunks:
        text = ' '.join(chunk)
        command1 = f'edge-tts --voice "{voice1}" --text "{text}" --write-media "data.mp3"'
        os.system(command1)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")

        try:
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(e)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
    return True


while True:
    query = takeCommand().lower()
    print(query)

    # ask = input('Question: ')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    data = response['choices'][0]['text']
    print(data)
    speak(data)