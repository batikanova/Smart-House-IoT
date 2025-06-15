
from scipy.spatial.distance import cosine
from resemblyzer import preprocess_wav, VoiceEncoder


def getEmbedding(audioNp):
    encoder = VoiceEncoder()
    wav = preprocess_wav(audioNp, sample_rate=16000)
    embedding = encoder.embed_utterance(wav)
    return embedding

def compareVoice(embedding, targetVoices):
    try:
        for targetVoice in targetVoices:
            if targetVoice is None:
                continue

            distance = cosine(embedding, targetVoice)
            print(f"Cosine distance: {distance}")
            if distance < 0.5:  # Threshold for similarity
                print("Voice match successful.")
                return True
            else:
                print("Voice match failed.")
                return False
    except Exception as e:
        print(f"Error during voice comparison: {e}")
        return False