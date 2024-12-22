# Robo-Speaker
Robo Speaker A Python-based voice assistant that greets users based on the current time of day. This lightweight program uses the pyttsx3 library for text-to-speech functionality, providing personalized greetings and a delightful user interaction experience.


# Robo Speaker

Robo Speaker is a simple Python-based voice assistant that greets the user based on the time of day. It uses the `pyttsx3` library to convert text to speech, making the interaction more engaging and user-friendly.

## Features
- Dynamic time-based greetings:
  - Morning (4:00 AM - 12:00 PM)
  - Afternoon (12:00 PM - 4:00 PM)
  - Evening (4:00 PM - 8:00 PM)
  - Late hours (8:00 PM - 4:00 AM)
- Text-to-speech functionality powered by `pyttsx3`.
- Lightweight and easy to run.

## How It Works
1. The program retrieves the current time using Python's `time` module.
2. Based on the current hour, it generates a greeting message.
3. The greeting is converted to speech and played aloud.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/robo-speaker.git
