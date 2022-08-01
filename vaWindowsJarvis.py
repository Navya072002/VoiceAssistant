import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys

#portAudio
#pyaudio


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("I am Jarvis maam, how may I help you?")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r= sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again plese")
        return "None"

    return query

def sendEmail(to, content):
    #enable less secure apps in gmail settings
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    #better to get password through a text file for more security
    server.sendmail('youremail@gmail.com', to, content)
    server.close()  

if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()
        
        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"maam, the time is{strTime}")

        elif 'open code' in query:
            codePath= ""
            os.startfile(codePath)

        elif 'email to Navya' in query:
            try:
                speak("what should I say?")
                content= takeCommand()
                to= "yourEmail@abc.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry maam, I am unable to send the email")

        elif 'thank you' in query :
            speak("your welcome")

        elif 'stop' in query:
            speak('good bye, have a nice day !!')
            sys.exit()

        elif 'bye' in query:
            speak('good bye, have a nice day !!')
            sys.exit()

    #add quit functionality