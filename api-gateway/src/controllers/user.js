const axios = require('axios');

exports.login = async (req, res) => {
  try {
    console.log('Login request received:', req.body);
    const response = await axios.post('http://localhost:5000/login', req.body);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json({ message: error.message });
  }
};

exports.register = async (req, res) => {
  try {
    const response = await axios.post('http://localhost:5000/register', req.body);
    res.json(response.data);
  } catch (error) {
    
    res.status(error.response?.status || 500).json({ message: error.response?.data?.message });
  }
};