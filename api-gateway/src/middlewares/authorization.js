const jwt = require('jsonwebtoken');

const authenticate = (req, res, next) => {
  const authHeader = req.headers.authorization;

  // Bearer token olup olmadığını kontrol et
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ success: false, message: 'Token gerekli' });
  }

  const token = authHeader.split(' ')[1]; // "Bearer xxxxxx" yapısından ayır

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    req.user = decoded;
   
    next();
  } catch (err) {
    return res.status(401).json({ success: false, message: 'Geçersiz token' });
  }
};

module.exports = authenticate;