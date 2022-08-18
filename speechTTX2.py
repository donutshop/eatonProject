
import os
import playsound
import time
import speech_recognition as sr
from gtts import gTTS

def speak(text): #saves and converts text to speech
    tts = gTTS(text=text, lang="en-gb")
    filename = os.path.dirname(__file__)+"\\voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something: ")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

        return said

while True:

  x = get_audio()
  speak(x)
