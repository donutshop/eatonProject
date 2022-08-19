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

while True:

    df = pd.read_excel(r"C:\Users\jetji\Desktop\test_tooloing_files.xlsx")
    col = pd.DataFrame(df, columns=["T", "RACK/CABINET", "ROW/BOX"])

    x = input("Enter: ")
    x = x.upper()
    x = x.replace(' ', '')

    s = col[df["T"] == x]

    print(s, "ooooooooooooooooo")

    if s.empty:
        speak("Sorry, not found. Do you have another query")
    else:

        loc1 = s["RACK/CABINET"].values
        loc2 = s["ROW/BOX"].values
        print(loc1)
        print(loc2)

        str1 = str(loc1)
        str2 = str(loc2)
        print(str1)
        print(str2)

        message = ("You can find this in cabinet", str1, "row", str2)
        j = ''.join(message)

        print(j)
        speak(j)


