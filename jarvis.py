import speech_recognition as sr
# now we can write speech-recognition as sr(in short form)
import webbrowser # it's a builtin module no need to download this module form pip
import pyttsx3 # text --> speech

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__": 
    speak("Initializing jarvis...")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using sphinx
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            command = r.recognize_google(audio) 
            print(command)
            # listen when someone says "Jarvis"
            if command.lower() == "jarvis":
                speak("Yahh..")
        except Exception as e:
            print("Error; {0}".format(e))
