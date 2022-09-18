#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install wikipedia


# In[2]:


pip install pyttsx3


# In[3]:


pip install speechRecognition


# In[4]:


import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr


# In[5]:


import pyttsx3


# In[6]:


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


# In[7]:


engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# In[8]:


voices[0]


# In[9]:


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
        speak("I am Jarvis Sir. I am here to help you")


# In[10]:


import pyaudio as p


# In[11]:


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        
        audio = r.listen(source)
        print("yes")
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


# In[12]:


import datetime


# In[13]:


pip install pyaudio


# In[14]:


import smtplib


# In[15]:


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('divya.20bczn002@jecrcu.edu.in', 'divya0523@')
    server.sendmail('divya.20bczn002@jecrcu.edu.in', to, content)
    server.close()


# In[ ]:


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        if "Hello" in query:
            speak("Hello! How may i help you?")

        elif "who are you" in query:
            speak("Sir I am Jarvis personal assistant ")
            
        elif "tell me about myself" in query:
            speak("yes! your name is divya lalwani from jecrc university in third year with domain data science")


    
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'open insta' in query:
            webbrowser.open("instagram.com")
        elif 'open linkdin' in query:
            webbrowser.open("linkdin.com")
        elif 'open facebook' in query:
            webbrowser.open("facbook.com")
        elif 'vs code' in query or 'write code' in query:
            subprocess.call('code')
       
        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')
        
        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)
            
        elif 'play music' in query:
            music_dir = "C:\\Users\\divya\\OneDrive\\Desktop\\jarvis\\Beautiful-Piano"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

       
        elif 'email to divya' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "divya.20bczn002@jecrcu.edu.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        elif 'shutdown' in query and 'minutes' in query:
            for word in st.split():
                if(word.isdigit()==1):
                    minutes = word
                    break
            os.system(f'shutdown +{minutes}')
            
        elif 'stop' in query:
            replyToUser("Stopping")
            talk()
            break


# In[ ]:


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


# In[ ]:


def open_notepad():
    os.startfile(paths['notepad'])


# In[ ]:


def open_cmd():
    os.system('start cmd')


# In[ ]:


def open_calculator():
    sp.Popen(paths['calculator'])


# In[ ]:


import requests
import wikipedia
from email.message import EmailMessage
import smtplib


# In[ ]:


{
  "ip": "117.214.111.199"
}


# In[ ]:


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


# In[ ]:


find_my_ip()


# In[ ]:


pip install pywhatkit


# In[ ]:


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


# In[ ]:


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


# In[ ]:


get_random_advice()


# In[ ]:


get_random_joke()


# In[ ]:




