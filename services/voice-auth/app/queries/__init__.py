

saveVoiceEmbedding = "INSERT INTO voice_embeddings (user_name, user_email, embedding) VALUES (%s, %s, %s) ON CONFLICT (user_name) DO UPDATE SET embedding = EXCLUDED.embedding"