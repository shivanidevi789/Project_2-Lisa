import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()
 
# Girl Voice code
def init_voice():
    try:
        voices = engine.getProperty('voices')
                
        # voice detect(hindi and english)
        for voice in voices:
            if ("female" in voice.name.lower() and "hindi" in str(voice.languages).lower()) or \
               "zira" in voice.name.lower():
                engine.setProperty('voice', voice.id)             
                return
        
        print("\n Female voice not found, using default voice")
    except Exception as e:
        print(f"Voice setting error: {e}")

# Girl voice Initiation
init_voice()

def speak(text):
    engine.say(text)
    engine.runAndWait()

 
def aiProcess(prompt):
        
        API_URL = "https://api.groq.com/openai/v1/chat/completions"
        API_KEY = os.getenv("YOUR_API_KEY")
              
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
                "model": "llama3-70b-8192",  
                "messages": [
                {"role": "system", "content": "You are a assistant named Lisa skilled in general tasks like Alexa"},
                    {"role": "user", "content": prompt}
                ],
        
            "temperature": 0.7
        }
        
        try:
            response = requests.post(API_URL, headers=headers, json=data)
        
            return response.json()['choices'][0]['message']['content']
            

        except Exception as e:
            return f"Error: {str(e)}"
    
 
def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "open chrome" in c:
        webbrowser.open("https://chrome.com")

    elif "thank you" in c:
        speak("Your Welcome, Have a good day!")     
      
    elif "play" in c.lower():
       
        song = c.lower().replace("play", "").strip()

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, song not found.")
     
    else:
        output = aiProcess(c)
        print(output)
        speak(output)

if __name__ == "__main__":
    speak("Initialization complete. Hello, I am Lisa!")
    r = sr.Recognizer()
    mic = sr.Microphone()
    while True:  
        print("Recognizing......")
         
        # recognize speech using google
        try:
                        
            with sr.Microphone() as source:
                print("Listening for wake word 'Lisa'..")
                audio = r.listen(source, phrase_time_limit = 5)
                word = r.recognize_google(audio)

                if((word.lower() == "lisa") or (word.lower() == "ok lisa") or (word.lower() == "hey lisa") or (word.lower() == "hi lisa")):
                    speak("Yes?")

                    #Listen for command
                    with sr.Microphone() as source:
                        print("Listening for your command...")
                        audio = r.listen(source, phrase_time_limit=8)
                        command = r.recognize_google(audio)
                        print("You said:", command)
                        processCommand(command)


        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Google Request error; {e}")
 
  
 