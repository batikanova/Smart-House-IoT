import sounddevice as sd
from app.utils.voice import getEmbedding, compareVoice
from app.config.db import getDB, releaseDB
import numpy as np
from scipy.io.wavfile import write
from app.queries import saveVoiceEmbedding, getVoiceEmbeddings, getVoiceEmbedding

def voiceVerifyService(userMail):
    recording = sd.rec(int(5 * 16000), samplerate=16000, channels=1, dtype='int16')
    sd.wait()
    audioNp = recording.squeeze().astype(np.float32) / 32768.0
    embedding = getEmbedding(audioNp)
    conn = getDB()
    if not conn:
        print("Database connection failed.")
        return False
    else:
        with conn.cursor() as cursor:
            cursor.execute(getVoiceEmbeddings)
            targetVoices = [(row[0], row[2]) for row in cursor.fetchall()]
            result = compareVoice(embedding, targetVoices, userMail)
            print(result)
        releaseDB(conn)
    
    return result

def takeRefVoiceService(userName, userEmail):
    try:
        conn = getDB()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(getVoiceEmbedding, (userEmail, userName))
                targetVoices = cursor.fetchall()
            if targetVoices:
                print("User already has a voice embedding.")
                releaseDB(conn)
                return False
        print(f"Recording for 5 seconds...")
        recording = sd.rec(int(5 * 16000), samplerate=16000, channels=1, dtype='int16')
        sd.wait()
        #write("voices/deneme.wav", 16000, recording)

        audioNp = recording.squeeze().astype(np.float32) / 32768.0
        embedding = getEmbedding(audioNp)
        
        
        with conn.cursor() as cursor:
            cursor.execute(saveVoiceEmbedding, (userName, userEmail, embedding.tolist()))
            conn.commit()
        releaseDB(conn)
        return True
    except Exception as e:
        print(f"Error during voice recording: {e}")
        return False

