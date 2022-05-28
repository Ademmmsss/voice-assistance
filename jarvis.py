import keyboard as k
import pyttsx3 
import speech_recognition as sr
import webbrowser as w
import wikipedia
import urllib
import urllib.request
import urllib.parse
import re
import os

x = pyttsx3.init('sapi5')
x.setProperty('rate', 165)
x.setProperty('volume', 5)

def speak(audio):
    x.say(audio)
    x.runAndWait()

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print('Listening')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(mic,duration=1)
        audio = r.listen(mic, phrase_time_limit=3)
    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except sr.UnknownValueError:
        speak('I cant hear you sir')
        return "None"
    except sr.RequestError:
        print('Failed')
        return "None"

    except sr.WaitTimeoutError:
        print('Sorry, we expired')
    
        return "None"
        
        
    
    return query

if __name__ == "__main__":
    speak('Hi sir, jarvis is here.')
    print('Press down key to talk')
    
    while True:
        if k.is_pressed('down'):
            query = Command().lower()
            
            if 'open youtube' in query:
                w.open('https://www.youtube.com')
                speak('Opening youtube')
            elif 'open google' in query:
                w.open('https://www.google.com')
                speak('Opening google')
            elif 'information' in query:
                speak('What do you want to read sir? ')
                info = Command().lower()
                result = wikipedia.summary(info)
                print(result)
                speak(result)
            elif 'turn off light' in query:
                speak('Light turned off')
            elif 'open light' in query:
                speak('Opening light')
            elif 'open discord' in query:
                speak('Opening discord')
                os.startfile('C:\\Users\\Adam\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe')
            elif 'play minecraft' in query:
                speak('Opening minecraft')
                os.startfile('C:\\Users\\Adam\\AppData\\Roaming\\.minecraft\\TLauncher.exe')
            else:
                speak(f'Searching {query} on google')


    