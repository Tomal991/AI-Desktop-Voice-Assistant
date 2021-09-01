import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import ctypes
import smtplib
import subprocess
import pyjokes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning!")
    elif(hour >= 12 and hour < 17):
        speak("Good Afternoon!")
    elif(hour >= 17 and hour < 20):
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("I am your assistant,Jarvis sir! Please tell me how may I help you?")
    print("I am your assistant,Jarvis sir! Please tell me how may I help you")

def takeCommand():
    s = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        s.pause_threshold = 1
        audio = s.listen(source,timeout=1,phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = s.recognize_google(audio, language='en-bn')
            print(f"You Said: {query}\n")
        except Exception as e:
            # print(e)
            print("Say That Again...")
            return "none"
        return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('intesarulhaquey4@gmail.com', 'hello.991')
    server.sendmail('intesarulhaquey4@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query or 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")

        elif 'google' in query or 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'github' in query or 'open github' in query:
            speak("Opening Github...")
            webbrowser.open("github.com")

        elif 'stack overflow' in query or 'open stack overflow' in query:
            speak("Opening stackoverflow...")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or 'play songs' in query or 'play song' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            speak("Playing Music...")
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play videos' in query or 'play video' in query:
            video_dir = 'D:\\Movies'
            videos = os.listdir(video_dir)
            speak("Playing Video...")
            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'who made you' in query or 'who created you' in query or 'who developed you' in query:
            pic_dir = 'D:\\Pic'
            pic = os.listdir(pic_dir)
            webbrowser.open("https://github.com/Tomal991")
            os.startfile(os.path.join(pic_dir, pic[0]))
            speak("Its Intesarul haque Tomal")

        elif 'the time' in query or "what is the time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            speak(f"the time is {time}")

        elif 'open code' in query or 'vs code' in query:
            codePath = "C:\\Users\\tomal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Vs code...")
            os.startfile(codePath)

        elif 'open postman' in query or 'postman' in query:
            postmanPath = "C:\\Users\\tomal\\AppData\\Local\\Postman\\Postman.exe"
            speak("Opening postman...")
            os.startfile(postmanPath)

        elif 'send a mail' in query or "send a email" in query or "send email" in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                print(f"your message: {content}\n")
                speak("whom should i send")
                to = input("Mail to: ")
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                # print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'Jarvis' in query or 'are you here' in query or 'where are you' in query:
            speak("i am here! Please tell me how may I help you sir?")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me Jarvis sir!")

        elif 'search' in query:
            query = query.replace("search", "")
            speak(f"searching {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'facebook' in query or 'open facebook' in query:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com/")

        elif "who am I" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Intesarul Haque Tomal. further It's a secret")

        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'today' in query:
            today = datetime.date.today().strftime("%A, %d-%B-%Y")
            print(today)
            speak(f"today is {today}")


        elif 'yesterday' in query:
            today = datetime.date.today()
            yesterday = today - datetime.timedelta(days=1)
            y = yesterday.strftime("%A, %d-%B-%Y")
            print(y)
            speak(f"yesterday was {y}")


        elif 'tomorrow' in query:
            today = datetime.date.today()
            tomorrow = today + datetime.timedelta(days=1)
            t = tomorrow.strftime("%A, %d-%B-%Y")
            print(t)
            speak(f"Tomorrow is {t}")

        elif 'notepad' in query or 'open notepad' in query:
            codePath = "C:\Windows\system32\\notepad.exe"
            speak("Opening Notepad...")
            os.startfile(codePath)


        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])


        elif 'joke' in query or 'tell a joke' in query :
            speak(pyjokes.get_joke())


        elif 'exit' in query or 'stop' in query or 'see you later' in query:
            speak("Thanks for giving me your time sir.")
            exit()