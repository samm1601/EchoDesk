# tts.py
# Text-to-speech using Coqui TTS
import os
import openai
import sounddevice as sd
import numpy as np
import io
import scipy.io.wavfile as wavfile
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY not set. Create a .env with OPENAI_API_KEY=<your_key> or set the environment variable.")

def speak(text, voice="onyx"):
    response = openai.audio.speech.create(
        model="tts-1-hd",  # or "tts-1" for slightly cheaper/faster
        voice=voice,       # voices: "onyx", "nova", "shimmer", "echo", "fable", "alloy"
        input=text
    )
    # The response is a binary stream (mp3)
    audio_bytes = io.BytesIO(response.content)
    # Decode mp3 to numpy array
    import pydub
    audio = pydub.AudioSegment.from_file(audio_bytes, format="mp3")
    samples = np.array(audio.get_array_of_samples()).astype(np.float32) / (2**15)
    sd.play(samples, samplerate=audio.frame_rate)
    sd.wait() 