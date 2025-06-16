const axios = require('axios');

exports.voiceSave = async (req, res) => {
  try {
    console.log('Voice save request received:', req.body);
    const response = await axios.post('http://0.0.0.0:1000/voice-auth/save', {name: req.user.name, email:req.user.email});
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json({ message: error.message });
  }
};

exports.voiceVerify = async (req, res) => {
  try {
    console.log('Voice verify request received:', req.user);
    const response = await axios.post('http://0.0.0.0:1000/voice-auth/verify', {email: req.user.email});
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json({ message: error.message });
  }
};

