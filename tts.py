import asyncio
import edge_tts
import tempfile
import os
import time
import threading
from playsound import playsound

async def _speak_edge(text: str):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_path = fp.name
        communicate = edge_tts.Communicate(text, voice="en-IN-NeerjaNeural")
        await communicate.save(temp_path)
        playsound(temp_path)
        time.sleep(0.3)
        os.remove(temp_path)
    except Exception as e:
        print(f"❌ TTS Error: {e}")

def speak_text(text: str):
    asyncio.run(_speak_edge(text))

async def stream_and_speak(text: str):
    def run_tts():
        asyncio.run(_speak_edge(text))
    tts_thread = threading.Thread(target=run_tts)
    tts_thread.start()
