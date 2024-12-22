import time
import pyttsx3

engine = pyttsx3.init()
current_hour = int(time.strftime("%H"))
print(current_hour)

def speak(message):
    engine.say(message)
    engine.runAndWait()

def greet_user():
    if 4 <= current_hour <= 12:
        greeting = "Hello Sir, Good Morning! How may I assist you?"
    elif 12 <= current_hour < 16:
        greeting = "Hello Sir, Good Afternoon! How may I assist you?"
    elif 16 <= current_hour < 20:
        greeting = "Hello Sir, Good Evening! How may I assist you?"
    else:
        greeting = "Hello Sir, What are you thinking?"
    speak(greeting)

greet_user()