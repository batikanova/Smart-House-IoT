const axios = require('axios');

exports.voiceRecognizing = async (req, res) => {
  try {
    console.log('Voice recognition request received:', req.body);
    const responseRecognizer = await axios.post('http://0.0.0.0:1000/voice-auth/verify', req.body)
    if (responseRecognizer.data == "True") {
      const response = await axios.post('http://0.0.0.0:2000/recognizer/recognize', req.body);
      res.json(response.data);
    } else {
      res.status(403).json({ message: "Voice verification failed." });
    }
  } catch (error) {
    res.status(error.response?.status || 500).json({ message: error.message });
  }
};