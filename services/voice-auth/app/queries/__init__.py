

saveVoiceEmbedding = "INSERT INTO vss.user_voice (user_name, user_email, embedding) VALUES (%s, %s, %s) ON CONFLICT (id) DO UPDATE SET embedding = EXCLUDED.embedding"
getVoiceEmbeddings = "SELECT embedding, user_name, user_email FROM vss.user_voice"
getVoiceEmbedding = "SELECT * FROM vss.user_voice WHERE user_email = %s OR user_name = %s"
