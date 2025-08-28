# stt.py
# Speech-to-text using OpenAI Whisper with dynamic recording
import os
os.environ["PATH"] += os.pathsep + r"C:\Users\airbo\Downloads\ffmpeg-2025-07-17-git-bc8d06d541-full_build\ffmpeg-2025-07-17-git-bc8d06d541-full_build\bin"
import whisper
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wavfile
import webrtcvad

# Change model name here for speed/accuracy tradeoff: 'tiny', 'small', 'base', 'medium', 'large'
model = whisper.load_model('small')

# Parameters for VAD
SAMPLE_RATE = 16000
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)
VAD_MODE = 1  # 0: most sensitive, 3: least sensitive
SILENCE_TIMEOUT = 1.5  # seconds of silence before stopping


def record_audio():
    print("Speak now! (Recording will auto-stop after you finish speaking)")
    vad = webrtcvad.Vad(VAD_MODE)
    audio_buffer = []
    silence_buffer = 0
    stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='int16', blocksize=FRAME_SIZE)
    with stream:
        while True:
            frame, _ = stream.read(FRAME_SIZE)
            frame_bytes = frame.tobytes()
            is_speech = vad.is_speech(frame_bytes, SAMPLE_RATE)
            audio_buffer.append(frame)
            if not is_speech:
                silence_buffer += FRAME_DURATION / 1000
            else:
                silence_buffer = 0
            if silence_buffer > SILENCE_TIMEOUT:
                break
    audio = np.concatenate(audio_buffer, axis=0)
    return audio, SAMPLE_RATE

def transcribe(audio, fs):
    # Create a temp file, close it, then write to it
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
        temp_name = f.name
    wavfile.write(temp_name, fs, audio)
    result = model.transcribe(temp_name)
    os.remove(temp_name)
    return result['text']
