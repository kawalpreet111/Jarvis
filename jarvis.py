
import json
import subprocess
import os
import subprocess as sp

import keyboard as keyboard
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import datetime
import numpy as np
import voice as voice
import wikipedia
import webbrowser
import os
import smtplib
import cv2
from cv2ools.core import Controller
from django.db.models import Q



from nbformat import current

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("   Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("    Good Afternoon!")

    else:
        speak("  Good Evening!")

    speak("    I am JArvis  Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("say that again  please")
        return "None"
    return query


def sleep():
    pass


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')
    server.sendmail('', to, content)
    server.close()
paths = {'notepad': "C:\Windows\System32\notepad.exe"}




def bluetooth_automation():
    import pyautogui
    from time import sleep
    sleep(2)
    coordinates = pyautogui.position()
    pyautogui.click(x=1799, y=1063)
    pyautogui.sleep(2)
    pyautogui.click(x=1753, y=687)
    pyautogui.sleep(1)
    pyautogui.hotkey('win' + 'k')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')


def speak_news():
    pass


def youtubeAuto():
    speak("What your command ? ")
    comm = takeCommand()

    if 'pause' in comm:
        keyboard.press('space bar')

    elif 'restart' in comm:
        keyboard.press('0')
    elif 'mute' in comm:
        keyboard.press('m')
    elif 'skip' in comm:
        keyboard.press('l')
    elif 'back' in comm:
        keyboard.press('j')
    elif 'full screen' in comm:
        keyboard.press('f')
    elif 'film mode' in comm:
        keyboard.press('t')

        speak("done sir")


def take_command():
    pass


def run_alexa():
    command = take_command()
    print(command)


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'what is jarvis' in query:
            music_dir = 'C:\JAr'
            songs = os.listdir(music_dir)
            print('what is jarvis')
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'joke' in query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)


        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com/accounts/login/')


        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'speaker' in query:
            bluetooth_automation()
            speak('sure SIr')

        elif 'play music' in query:
            music_dir = 'C:\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "what's the time right now" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:/Users/Lavish/PycharmProjects/pythonProjectt/Jarvis.py"
            os.startfile(codePath)

        elif 'Take screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')

        elif 'open email' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')


        elif 'open amazon' in query:
            webbrowser.open(
                'https://www.amazon.in/ref=as_li_ss_tl?ie=UTF8&linkCode=ll2&tag=enin-edge-topsites-curate-ana-21&linkId=fbedcb44d04a4bae8eae32722a2f41c2&language=en_IN')

        elif 'open flipkart' in query:
            webbrowser.open(
                'https://www.flipkart.com/?ef_id=c218ddab93dd1aa34848bc46c15edef3:G:s&s_kwcid=AL!739!10!76347481385536!76347484024120&semcmpid=sem_F1167BY7_Brand_adcenter')

        elif 'my college' in query:
            webbrowser.open('https://www.poornima.edu.in/')

        # poornima university website
        elif 'Todays news' in query:
            speak("News for today")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3f52edc3c9a945e58348656f101fa866"
            news = requests.get(url).text
            news_json = json.loads(news)
            print(news_json["articles"])
            arts = news_json['articles']
            for articles in arts:
                speak(articles['title'])
                speak("Moving to the next news...listen carefully")

            speak("Thanks for listening...")


        elif 'how to learn python' in query:
            speak("by joining the given course you can learn python")
            webbrowser.open(
                'https://www.udemy.com/course/python-the-complete-python-developer-course/?matchtype=p&msclkid=f3c353f237a712dd7763321f64101c8f&utm_campaign=BG-Python_v.PROF_la.EN_cc.INDIA_ti.7380&utm_content=deal4584&utm_medium=udemyads&utm_source=bing&utm_term=_._ag_1217159784871737_._ad__._kw_%2BPython+%2Bhow+%2BClass_._de_c_._dm__._pl__._ti_kwd-76072799117886%3Aloc-90_._li_157639_._pd__._')



        elif 'youtube search' in query:
            speak("ok sir , this is what i found for your search ")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            pyautogui.hotkey('enter')
            speak("done sir")


        elif 'open Telegram' in query:



            Whatsapp_path = "C:\Program Files\WindowsApps"
            os.startfile(Whatsapp_path )



        elif 'play' in query:
            speak("ok sir , this is what i found for your search ")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            pyautogui.hotkey('enter')
            pyautogui.sleep(4)
            pyautogui.click(x=922, y=241)
            speak("done sir")

        elif "open file manager" in query:
            pyautogui.hotkey("Win", "1")
            pyautogui.sleep(1)
            speak("opening")

        elif 'google search' in query:
            speak("this is what i found for your seearch sir")
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("done sir")

        elif "open camera" in query:
            pyautogui.hotkey("Win","9")
            pyautogui.sleep(1)
            speak("Launching")


        elif "open office" in query:
            pyautogui.hotkey("Win", "5")
            pyautogui.sleep(1)
            speak("launching")

        elif "open windows store" in query:
            pyautogui.hotkey("Win", "6")
            pyautogui.sleep(1)
            speak("launching")

        elif "open microsoft edge" in query:
            pyautogui.hotkey("Win", "7")
            pyautogui.sleep(1)
            speak("launching")

        elif "open pycharm" in query:
            pyautogui.hotkey("Win", "8")
            pyautogui.sleep(1)
            speak("launching")


        elif "close" in query:
            pyautogui.hotkey("Alt", "F4")
            speak("closing")

        elif "open settings" in query:
            pyautogui.hotkey("Win", "i")
            pyautogui.sleep(1)

            speak("opening setting")

        elif "wake up" in query:
            pyautogui.hotkey("Win", "Ctrl", "F4")
            music_dir = 'C:\JAr'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            pyautogui.sleep(20)
            pyautogui.hotkey("Alt", "F4")

        elif  "start recording" in query:
            pyautogui.hotkey("Win", "Alt", "r")
            speak("Started recording. just say stop recording to stop.")

        elif "stop recording" in query:
            pyautogui.hotkey("Win", "Alt", "r")

            speak("Stopped recording. check your game bar folder for the video")


        elif "Open notepad" in query:
            file_path = "C:\JAr\notepad"
            os.startfile(file_path)

        elif "open task Manager" in query:
            pyautogui.hotkey("Ctrl", "Shift", "Esc")
            speak("opening task manager")

        elif "open xbox" in query:
            pyautogui.hotkey("Win", "2")
            speak(" ok sir opening xbox")


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""
                sendEmail(to, content)
                speak("Email has been sent!")



            except Exception as e:
                print(e)
                speak("Sorry Kawalpreet Sir . I am not able to send this email")
