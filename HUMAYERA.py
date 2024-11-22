#Voice Assistant Project

global chrome_path 
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

#import all required modules
from importlib.resources import path
import keyword#for controling keyboard
import queue
import smtplib #needed for sending mails
import webbrowser#for using browser
from click import command
from numpy import take #needed for opening links in browser
import pyttsx3 #needed for our assistant voice
import datetime #needed for getting date and time
import speech_recognition as sr #needed for our assistant to hear and understant our voice
import os
import wikipedia
import pywhatkit
import os
#import pyautogui
import keyboard
import pyjokes
#from PyDictionary import PyDictionary as Dict
#from playsound import playsound as ps




#our assistant voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 140)

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#password input
# for i in range(3):
#     a = input("Enter Password to open Jarvis :- ")
#     pw_file = open("password.txt","r")
#     pw = pw_file.read()
#     pw_file.close()
#     if (a==pw):
#         speak("Loadind...")
#         break
#     elif (i==2 and a!=pw):
#         exit()

#     elif (a!=pw):
#         print("Try Again")

#wishme function - it will wish us
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

print("Hello Sir I am Alexa")
speak("Hello Sir I am Alexa ")
print("How May I Help You?")
speak("How May I Help You?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.phrase_threshold = 0.6
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please....")
        speak("Say that again please....")
        return "None"

    return query

#To send mails (Server to send emails)
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.login('3maqsoodahmed@gmail.com', 'password')
    server.sendmail('3maqsoodahmed@gmail.com', to, content)
    server.close()

#Clossing any app
def closeapp():
    speak("Ok Sir , Wait just a second")

    if 'youtube' in query:
        os.system("TASKKILL /f /ln chrome.exe")

    elif 'chrome' in query:
        os.system("TASKKILL /f /ln chrome.exe")

    elif 'telegram' in query:
        os.system("TASKKILL /f /ln telegra.exe")

    elif '' in query:
        os.system("TASKKILL /f /ln query + .exe")

#Fully Automating Youtube
def YouTubeAuto():
    speak("Whats Your Command ?")
    query = takecommand().lower()

    if 'pause' in query:
        keyboard.press('space-bar')

    elif 'restart' in query:
        keyboard.press('0query')

    elif 'mute' in query:
        keyboard.press('m')

    elif 'skip' in query:
        keyboard.press('i')

    elif 'back' in query:
        keyboard.press('j')

    elif 'fullscreen' in query:
        keyboard.press('f')
        print("entering fullscreen mode")
        speak("entering fullscreen mode")

    elif 'full mode' in query:
        keyboard.press('t')

    speak("Done Sir!")

#takking screenshot
def screenshot():
    speak("Ok Boss , what should i name that file ?")
    path = takecommand()
    pathname = path + ".png"
    path1 = "M:\\" + pathname
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("M:\\")
    speak("Here is your screenshot")

#Dictionory
def Dict():
    speak("Activated Dictionar")
    speak("Tell me the problem")
    prob1 = takecommand().lower()

    if 'meaning' in prob1:
        prob1 = prob1.replace("malsm","")
        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("meaning of","")
        result = dict.meaning(prob1)
        speak(f"The Maning of (prob1) is {result}")

    elif 'synonym' in prob1:
        prob1 = prob1.replace("malsm","")
        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("synonym of","")
        result = dict.synonym(prob1)
        speak(f"The Synonmy of (prob1) is {result}")

    elif 'antonym' in prob1:
        prob1 = prob1.replace("malsm","")
        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("antonym of","")
        result = dict.antonym(prob1)
        speak(f"The Antonym of (prob1) is {result}")

    speak("Exited Dictionary")

#Chrome automate
def ChromeAuto():
    speak("Chrome automation started!")

    command = takecommand().lower()
    
    if 'close this tab' in command:
        keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')

    elif 'open new window' in command:
        keyboard.press_and_release('ctrl + n')

    elif 'back a page' in command:
        keyboard.press_and_release('alt + left arrow')

    elif 'forward a page' in command:
        keyboard.press_and_release('alt + right arrow')

    elif 'display full screen mode' in command:
        keyboard.press_and_release('F11')

    elif 'history' in command:
        keyboard.press_and_release('ctrl + h')

    elif 'downloads' in command:
        keyboard.press_and_release('ctrl + j')

    elif 'open homepage ' in command:
        keyboard.press_and_release('alt + home')

    elif 'history' in command:
        keyboard.press_and_release('ctrl + h')

    elif 'stop loading page' in query or 'stop loading download' in command:
        keyboard.press_and_release('Esc')

    elif 'zoom in' in command:
        keyboard.press_and_release('ctrl + +')

    elif 'zoom out' in command:
        keyboard.press_and_release('ctrl + -')

    elif 'open first tab' in command:
        keyboard.press_and_release('ctrl + 1')

    elif 'open second tab' in command:
        keyboard.press_and_release('ctrl + 2')
    
    elif 'open third tab' in command:
        keyboard.press_and_release('ctrl + 3')
    
    elif 'open fourth tab' in command:
        keyboard.press_and_release('ctrl + 4')
    
    elif 'open fifth tab' in command:
        keyboard.press_and_release('ctrl + 5')
    
    elif 'open sixth tab' in command:
        keyboard.press_and_release('ctrl + 6')
    
    elif 'open seventh tab' in command:
        keyboard.press_and_release('ctrl + 7')
    
    elif 'open eighth tab' in command:
        keyboard.press_and_release('ctrl + 8')
    
    elif 'switch to last tab' in query or 'open the last tab' in command:
        keyboard.press_and_release('ctrl + 9')

    elif 'reset zoom to default' in command:
        keyboard.press_and_release('ctrl + 0')

    elif 'complete address' in query or 'complete link' in command:
        keyboard.press_and_release('ctrl + enter')

    elif 'open clear browsing data' in query or 'open clear browsing' in command:
        keyboard.press_and_release('ctrl + shift + delete')

    elif 'show bookmarks bar' in query or 'hide bookmarks bar' in command:
        keyboard.press_and_release('ctrl + shift + B')

    elif 'select all' in query or 'select everything' in command:
        keyboard.press_and_release('ctrl + a')

    elif 'add bookmark' in query or 'add this page as bookmark' in command:
        keyboard.press_and_release('ctrl + d')

    elif 'open the find bar' in query or 'search on page' in command:
        keyboard.press_and_release('ctrl + f')

    elif'open file in browser' in command:
        keyboard.press_and_release('ctrl + o')

    elif 'open bookmark manager' in command:
        keyboard.press_and_release('ctrl + shift + o')

    elif 'open browser history in new tab' in command:
        keyboard.press_and_release('ctrl + h')

    elif 'open the last closed tab' in command:
        keyboard.press_and_release('ctrl + shift + t')

    elif 'move to next tab' in command:
        keyboard.press_and_release('ctrl + tab')

    elif 'movev to previou tab' in command:
        keyboard.press_and_release('ctrl + shift + tab')

    elif 'open link in new tab in background' in command:
        keyboard.press_and_release('ctrl + left-click')

    elif 'open link in new tab amd switch to new tab' in query or 'open link in new tab and move to new tab' in command:
        keyboard.press_and_release('ctrl + h')

    elif 'open the browser tab to right' in command:
        keyboard.press_and_release('ctrl + pagedown')

    elif 'open the browser tab to left' in command:
        keyboard.press_and_release('ctrl + pageup')

    elif 'move down a page at a time' in command:
        keyboard.press_and_release('spacebar')

    elif 'move up a page at a time' in command:
        keyboard.press_and_release('shift spacebar')

    elif 'go to top of the page' in query or 'top of page' in command:
        keyboard.press_and_release('home')

    elif 'go to bottom of the page' in query or 'end of the page' in command:
        keyboard.press_and_release('end')

    elif 'display previous text' in query or 'open drop down menu' in command:
        keyboard.press_and_release('alt + down arrow')

#Logic for executing tasks based on query
if __name__ == "__main__":
    wishMe()

    
    while True:
        query = command = takecommand().lower()
        
    #Greating Codes
        if 'hello' in query:
            speak("Hello Sir I am Jarvis")
            speak("Kunal's Personal AI")
            speak("How May I Help You?")

        elif 'who are you' in query:
             speak("Hello there! I'm Alexa, your personal voice assistant. I'm at your service. Just ask, and I'll do my best to assist you")

        elif 'are you there' in query:
            speak("For you any time Sir")

        elif 'its time to play' in query:
            speak("Ok sir ! Let's begin")

        elif 'how are you' in query:
            speak("I am Fine Sir!")
            speak("What About You?")

        elif 'you need a break' in query:
            speak("Ok Sir , You can Call me anytime !")
            break

        elif "help me Alexa" in query or "help me" in query:
            speak("how can i help you sir")
            print("how can i help you sir")

        elif "are you there Alexa" in query or 'are you there' in query:
            speak(" For you any time Sir")
            print(" For you any time Sir")

        elif "how are you Jarvis" in query:
            stMsgs = ['I am fine Sir, just doing my work']
            ans_q = (stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = query
            
            if 'fine' in ans_take_from_user_how_are_you in query or 'happy' in ans_take_from_user_how_are_you:
                speak("okey..")
            elif 'not' in ans_take_from_user_how_are_you:
                        speak("oh sorry.. Sir..")
                        break
    #YouTube Codes
        elif 'open youtube' in query:
            speak("opening")
            webbrowser.open("youtube.com")

        elif 'youtube search' in query:
            speak("Ok Sir! Tell me what should I search")
            query = takecommand()
            query = query.replace("jarvis","")
            query = query.replace("youtube","")
            query = query.replace("search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Ok Sir! This is what I found for your search")

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0query')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('i')

        elif 'back' in query:
            keyboard.press('j')

        elif 'fullscreen' in query:
            keyboard.press('f')

        elif 'full mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YouTubeAuto()

    #Chrome Codes
        elif 'open chrome' in query:
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            speak("Ok Sir! opening chrome")
            

        elif 'open browser' in query:
            speak("opening browser")
            webbrowser.open('about:blank')
            
    #Chrome Automation codes
        elif 'activate chrome automation' in query:
            ChromeAuto()
            speak("Opening crome automation")

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
            speak("Closing the tab")
            print("Closing the tab")

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
            speak("Opening the tab")
            print("Opening the tab")

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
            speak("Opening new window")
            print("Closing new window")

        elif 'back a page' in query:
            keyboard.press_and_release('alt + left arrow')
            speak("viewing the previous page")
            print("viewing the previous page")

        elif 'forward a page' in query:
            keyboard.press_and_release('alt + right arrow')
            speak("viewing the next page")
            print("viewing the next page")

        elif 'display full screen mode' in query:
            keyboard.press_and_release('F11')
            speak("viewing in full screeb mode")
            print("viewing in full screeb mode")

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'downloads' in query:
            keyboard.press_and_release('ctrl + j')

        elif 'open homepage ' in query:
            keyboard.press_and_release('alt + home')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            speak("opeing history")
            print("opening history")

        elif 'stop loading page' in query:
            keyboard.press_and_release('Esc')
            print('stoped loading page')
            speak('stoped loading page')

        elif 'stop loading download' in query:
            keyboard.press_and_release('Esc')
            print('stoped loading page')
            speak('stoped loading page')

        elif 'zoom in' in query:
            keyboard.press_and_release('ctrl + +')
            print('zooming in')
            speak('zooming in')

        elif 'zoom out' in query:
            keyboard.press_and_release('ctrl + -')
            print('zooming out')
            speak('zooming out')

        elif 'open first tab' in query:
            keyboard.press_and_release('ctrl + 1')
            print('opening first tab')
            speak('opening first tab')

        elif 'open second tab' in query:
            keyboard.press_and_release('ctrl + 2')
            print('opening second tab')
            speak('opening second tab')
        
        elif 'open third tab' in query:
            keyboard.press_and_release('ctrl + 3')
            print('opening third tab')
            speak('opening third tab')
        
        elif 'open fourth tab' in query:
            keyboard.press_and_release('ctrl + 4')
            print('opening fourth tab')
            speak('opening fourth tab')
        
        elif 'open fifth tab' in query:
            keyboard.press_and_release('ctrl + 5')
            print('opening fifth tab')
            speak('opening fifth tab')
        
        elif 'open sixth tab' in query:
            keyboard.press_and_release('ctrl + 6')
            print('opening sixth tab')
            speak('opening sixtht tab')
        
        elif 'open seventh tab' in query:
            keyboard.press_and_release('ctrl + 7')
            print('opening seventh tab')
            speak('opening seventh tab')
        
        elif 'open eighth tab' in query:
            keyboard.press_and_release('ctrl + 8')
            print('opening eighth tab')
            speak('opening eighth tab')


        elif 'switch to last tab' in query:
            keyboard.press_and_release('ctrl + 9')
            print('opening ninth tab')
            speak('opening ninth tab')

        elif 'open the last tab' in query:
            keyboard.press_and_release('ctrl + 9')
            print('opening ninth tab')
            speak('opening ninth tab')

        elif 'reset zoom to default' in query:
            keyboard.press_and_release('ctrl + 0')
            print('default zoom')
            speak('default zoom')

        elif 'complete address' in query:
            keyboard.press_and_release('ctrl + enter')
            print('address completed')
            speak('address completed')

        elif 'complete link' in query:
            keyboard.press_and_release('ctrl + enter')
            print('address completed')
            speak('address completed')

        elif 'clear browsing data' in query:
            keyboard.press_and_release('ctrl + shift + delete')
            print('clearing browsing data')
            speak('clearing browsing data')

        elif 'clear browsing' in query:
            keyboard.press_and_release('ctrl + shift + delete')
            print('clearing browsing data')
            speak('clearing browsing data')
            
        elif 'show bookmarks bar' in query:
            keyboard.press_and_release('ctrl + shift + B')
            print('showing bookmars')
            speak('showing bookmarks')

        elif 'hide bookmarks bar' in query:
            keyboard.press_and_release('ctrl + shift + B')
            print('hiding bookmars')
            speak('hiding bookmarks')

        elif 'select all' in query:
            keyboard.press_and_release('ctrl + a')
            print('all selected')
            speak('all selected')

        elif 'select everything' in query:
            keyboard.press_and_release('ctrl + a')
            print('all selected')
            speak('all selected')

        elif 'add bookmark' in query or 'add this page as bookmark' in query:
            keyboard.press_and_release('ctrl + d')

        elif 'open the find bar' in query or 'search on page' in query:
            keyboard.press_and_release('ctrl + f')

        elif'open file in browser' in command:
            keyboard.press_and_release('ctrl + o')

        elif 'open bookmark manager' in command:
            keyboard.press_and_release('ctrl + shift + o')

        elif 'open browser history in new tab' in command:
            keyboard.press_and_release('ctrl + h')

        elif 'open the last closed tab' in command:
            keyboard.press_and_release('ctrl + shift + t')

        elif 'move to next tab' in command:
            keyboard.press_and_release('ctrl + tab')

        elif 'movev to previou tab' in command:
            keyboard.press_and_release('ctrl + shift + tab')

        elif 'open link in new tab in background' in command:
            keyboard.press_and_release('ctrl + left-click')

        elif 'open link in new tab amd switch to new tab' in query or 'open link in new tab and move to new tab' in command:
            keyboard.press_and_release('ctrl + h')

        elif 'open the browser tab to right' in command:
            keyboard.press_and_release('ctrl + pagedown')

        elif 'open the browser tab to left' in command:
            keyboard.press_and_release('ctrl + pageup')

        elif 'move down a page at a time' in command:
            keyboard.press_and_release('spacebar')

        elif 'move up a page at a time' in command:
            keyboard.press_and_release('shift spacebar')
            speak("moving up a page at a time")
            print("moving up a page at a time")

        elif 'go to top of the page' in query or 'top of page' in command:
            keyboard.press_and_release('home')

        elif 'go to bottom of the page' in query or 'end of the page' in command:
            keyboard.press_and_release('end')

        elif 'display previous text' in query or 'open drop down menu' in command:
            keyboard.press_and_release('alt + down arrow')
            speak("viewing the previous text")
            print("viewing the previous text")
            

        #Chrome Automation Code Ends Here

        elif 'open google' in query:
            speak("opening google")
            webbrowser.get(chrome_path).open("google.com")
            

        elif 'google search' in query:
            speak("Ok Sir, Tell me what should I search")
            query = takecommand()
            query = query.replace("malsm","")
            query = query.replace("google","")
            query = query.replace("search","")
            query = query.replace("jarvis","")
            pywhatkit.search(query)
            speak("OK Sir , This is what I found for your search")

        elif 'website' in query:
            speak("Ok Sir , Opening the website....")
            query = query.replace("Malsm","")
            query = query.replace("website","")
            query = query.replace("open","")
            query = query.replace("jarvis","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 +'.com'
            webbrowser.open(web2)
            speak("This is what i found for you Sir")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Ok sir Opening Stackoverflow")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\lenovo\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open notepad' in query or "notepad" in query:
            speak("ok sir opening notepad")
            notepad_dir = "C:\\Windows\\notepad.exe"
            os.startfile(notepad_dir)

        elif 'open code' in query:
            codePath = "F:\VSCode\Microsoft VS Code"
            os.startfile(codePath)

        elif 'search wikipedia' or 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search", "")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            closeapp

        elif 'send mail' in query:
            try:
                speak("What should i say? Sir")
                content = takecommand()
                to = takecommand()
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry the email cant be send")

        elif 'screenshot' in query:
            screenshot()

        elif 'joke' or 'tell me a joke' in query:
            get = pyjokes.get_joke()
            print(get)
            speak(get)
            exit

        elif 'goodbye' or 'good bye' or 'exit' in query:
            speak("good bye")
            exit()

        elif "shutdown" in query:
            os.system('shutdown -s')

        elif 'repeat my words' in query:
            speak("Ok Sir Tell me what to speak")
            jj = takecommand()
            speak(f"You said : (jj)")

        elif 'my location' in query:
            speak()

        elif 'dictionary' in query:
            Dict()
            
        elif 'alarm' in query:
            speak("Tell Me the Time")
            time = input(": Enter the Time :")
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up Sir!")
                    ps('iron.mp3')
                    speak("Alarm Closed")
                elif now > time:
                    break