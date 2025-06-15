import sounddevice as sd
from app.utils.voice import getEmbedding, compareVoice
from app.models.db import getVoices, saveVoice
import numpy as np
from scipy.io.wavfile import write


def voiceAuthenticateService():
    recording = sd.rec(int(5 * 16000), samplerate=16000, channels=1, dtype='int16')
    sd.wait()
    embeddingRef = getEmbedding(recording.squeeze())
    targetVoices = getVoices()
    result = compareVoice(embeddingRef, targetVoices)
    return result

def takeRefVoiceService(userName, userEmail):
    try:
        print(f"Recording for 5 seconds...")
        recording = sd.rec(int(5 * 16000), samplerate=16000, channels=1, dtype='int16')
        sd.wait()
        #write("voices/deneme.wav", 16000, recording)

        audioNp = recording.squeeze().astype(np.float32) / 32768.0
        embedding = getEmbedding(audioNp)
        #saveVoice(embedding, userName, userEmail)
        return True
    except Exception as e:
        print(f"Error during voice recording: {e}")
        return False

