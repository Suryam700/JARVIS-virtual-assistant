import speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsApi = "2eaa023f581743929f7ccc6509c11272"
country = "us"

def speak(text):
    engine.say(text)    
    engine.runAndWait()

def processCommand(c):
    if "open facebook" in c.lower():
        webbrowser.open("http://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif "open linkedin" in c.lower(): 
        webbrowser.open("https://www.linkedin.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        webbrowser.open(musicLibrary.music[song])
    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsApi}")
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", []) 
            for article in articles:
                print(article["title"])
    else:
        # let openAI handle the request
        pass

if __name__ == "__main__": 
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio) 
            print(word)
            if "jarvis" in word.lower():
                print("Condition matched")
                speak("Yaa")
                with sr.Microphone() as source:
                    print("Jarvis activated...")
                    audio = r.listen(source) 
                    command = r.recognize_google(audio)

                    processCommand(command) 

        except Exception as e:
            print("Error; {0}".format(e))



