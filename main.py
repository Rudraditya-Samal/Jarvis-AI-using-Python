import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak function wil pronounce the string which is passed to it.
def speak(text):
    engine.say(text)
    engine.runAndWait()


# This function will wish as per the current time
def wishMe():
    time = datetime.datetime.now().hour

    if time>=0 and time<12:
        print("Good Moning Sir...")
        speak("Good Moning Sir...")

    elif time>=12 and time<18:
        print("Good Afternoon Sir...")
        speak("Good Afternoon Sir...")

    else:
        print("Good Evening Sir...")
        speak("Good Evening Sir...")

    # speak("I am jarvis.How may I help you")

# This function will take command from microphone
def tekeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = 'en')
        print(f"user said: {query}")

    except Exception as e:
        print("Say that again please")
        query = None

    return query



# Main program starts here
print("Initialising Jarvis...")
wishMe()
query = tekeCommand()

# Logic for executing basic tasks as per the query
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences= 2)
    print(results)
    speak(results)

elif 'youtube' in query.lower():
    url = "youtube.com"
    edge_path = '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" %s'
    webbrowser.get(edge_path).open(url)

elif 'google' in query.lower():
    url = "google.com"
    edge_path = '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" %s'
    webbrowser.get(edge_path).open(url)

elif 'stackoverflow' in query.lower():
    url = "stackoverflow.com"
    edge_path = '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" %s'
    webbrowser.get(edge_path).open(url)

elif 'bootstrap' in query.lower():
    url = "getbootstrap.com"
    edge_path = '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" %s'
    webbrowser.get(edge_path).open(url)

if 'play music' in query.lower():
    songs_dir = "D:\\SONGS\\Spiritual Songs"
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[0]))
    