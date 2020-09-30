import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')  # is used to take the voice from system
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice', voice[1].id)  # voice[0] or voice[1] is used for male or female voice from system


def speak(audio):  # is used to audiable the system
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # wishme function is used to wish me according to time
    hour = int(datetime.datetime.now().hour)  # datetime give the system to current dtae and time
    if hour > 0 and hour < 12:
        speak('Good Morning Ankit Sir!')
    elif hour > 12 and hour < 18:
        speak("Good Afternoon Ankit Sir!")
    else:
        speak("Good Evening Ankit Sir!")

    speak("This is Veronica Sir, How can I help you Sir?")


def takeCommand():
    '''It take microphone input and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1 #1 is give us some pause while giving command to system
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print('user said: ',query)

    except Exception as e:
        #print(e)
        print('say that again please...')
        return 'None' #None is just a string
    return query
if __name__ == '__main__':  # this will help us to execute
    wishMe()
    #while True:
    while True:
        query= takeCommand().lower()

        if 'wikipedia' in query:
            print('Searching wikipedia...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'play music' in query:
            music_dir='F:\\songs'
            songs=os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randrange(start=0,stop=10)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H,%M.%S')
            speak('Sir,The time is ',strTime)
        elif 'open chrome' in query:
            Search_engine = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(Search_engine)

    #logic for executing task based on query
    # speak("Ankit is a good boy")
