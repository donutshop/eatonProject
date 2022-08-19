import pandas as pd
import os
import playsound
import time
import speech_recognition as sr
from gtts import gTTS

def speak(txt):
    tts = gTTS(text=txt, lang="en")
    filename = os.path.dirname(__file__)+"\\voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def audio():
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

    df = pd.read_excel(r"C:\Users\jetji\Desktop\test_tooloing_files.xlsx")

    col = pd.DataFrame(df, columns=["T", "RACK/CABINET", "ROW/BOX"])

    x = audio()
    x = x.upper()
    x = x.replace(' ', '')

    print(x)

    s = col[col["T"] == x]
    if s.empty:
        speak("Sorry, not found. Do you have another query")
    else:
        loc1 = s["RACK/CABINET"].values
        loc2 = s["ROW/BOX"].values
        str1 = str(loc1)
        str2 = str(loc2)
        message = ("You can find this in cabinet", str1, "row", str2)
        j = ''.join(message)

        print(j)
        speak(j)