import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import gtts

# initialise dependencies
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def say(text):
    engine.say(text)
    engine.runAndWait()


def listen_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                command = command.replace('alex', '')
                print('search' + command)

    except:

        pass

    return command

def run_it():
    command = listen_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        say('ok, playing' + song)
        pywhatkit.playonyt(song)

while True:
    run_it()

auto_start = True