import sounddevice as sd
from utils.voice import getEmbedding, compareVoice
from clients.db import getVoices, saveVoice

def voiceAuthenticateService():
    recording = sd.rec(int(5 * 16000), samplerate=16000, channels=1, dtype='int16')
    sd.wait()
    embeddingRef = getEmbedding(recording.squeeze())
    targetVoices = getVoices()
    result = compareVoice(embeddingRef, targetVoices)
    return True

def takeRefVoiceService():
    try:
        print(f"Recording for 5 seconds...")
        recording = sd.rec(int(5 * 16000), samplerate=16000, channels=1, dtype='int16')
        sd.wait()
        embedding = getEmbedding(recording.squeeze())
        saveVoice(embedding)
        return embedding
    except Exception as e:
        print(f"Error during voice recording: {e}")
        return False

