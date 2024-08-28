import pyttsx3 
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recongnizer =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recongnizer.adjust_for_ambient_noise(source)
        audio =recongnizer.listen(source)
        try:
            print("recognizing...")
            data = recongnizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print(" Not understand")

sptext()