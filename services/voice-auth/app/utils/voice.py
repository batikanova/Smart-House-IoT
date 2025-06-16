
from scipy.spatial.distance import cosine
from resemblyzer import preprocess_wav, VoiceEncoder


def getEmbedding(audioNp):
    encoder = VoiceEncoder()
    wav = preprocess_wav(audioNp)
    embedding = encoder.embed_utterance(wav)
    
    return embedding

def compareVoice(embedding, targetVoices, userMail):
    try:
        for targetVoice in targetVoices:
            if targetVoice[0] is None:
                continue

            distance = cosine(embedding, targetVoice[0])
            print(f"Cosine distance: {distance}")
            if distance < 0.5:  # Threshold for similarity
                if targetVoice[1] == userMail:
                    print("Voice match successful.")
                    return True
                else:
                    print("Voice match successful but email does not match.")
                    return False
            else:
                print("Voice match failed.")
                return False
    except Exception as e:
        print(f"Error during voice comparison: {e}")
        return False