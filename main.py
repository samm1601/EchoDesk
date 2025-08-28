# main.py
import os
os.environ["PATH"] += os.pathsep + r"C:\Users\airbo\Downloads\ffmpeg-2025-07-17-git-bc8d06d541-full_build\ffmpeg-2025-07-17-git-bc8d06d541-full_build\bin"
from stt import record_audio, transcribe
from chat import ask_gpt
from tts import speak

if __name__ == "__main__":
    print("Welcome to the Automated Customer Support Agent! Press Ctrl+C to exit.")
    while True:
        audio, fs = record_audio()
        user_text = transcribe(audio, fs)
        print(f"You said: {user_text}")
        response = ask_gpt(user_text)
        print(f"Agent: {response}")
        speak(response) 