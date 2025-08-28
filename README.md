# 🎙️ EchoDesk: Automated Customer Support Agent (Voice-Enabled)

EchoDesk is a **local voice-enabled AI assistant** that listens to users, transcribes speech to text, generates answers using an LLM grounded on a local knowledge base, and speaks responses aloud.  

Designed for customer support scenarios, it can run entirely locally (speech-to-text, scraping, knowledge base) with cloud-powered reasoning (OpenAI API).

---

## 🚀 How It Works (High-Level Flow)

1. **Listen** 🎤 – Captures microphone audio with VAD-based auto-stop.  
2. **Transcribe** ✍️ – Converts speech to text using a local Whisper model.  
3. **Answer** 💡 – Sends text to an OpenAI Chat model with `knowledge_base.json` injected as context.  
4. **Speak** 🔊 – Converts model reply to speech with TTS and plays audio output.  

---

## 📂 Project Structure

```bash
EchoDesk/
│── main.py              # Entry point: infinite listen → transcribe → chat → speak loop
│── stt.py               # Speech-to-text using sounddevice + webrtcvad + Whisper
│── chat.py              # Chat with OpenAI GPT, grounded on knowledge_base.json
│── tts.py               # Text-to-speech with OpenAI TTS API + sounddevice
│── knowledge_base.json  # Grounding data (scraped knowledge)
│── scrape_scholars.py   # Scraper to rebuild/update knowledge_base.json
│── requirements.txt     # Dependencies
│── test.py              # Optional: CUDA availability check
│── .gitignore           # Ignores .env, caches, artifacts
│── __pycache__/         # Python bytecode cache (ignored)
