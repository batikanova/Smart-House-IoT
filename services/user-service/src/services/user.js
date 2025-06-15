const pool = require('../config/db');
const { sendJwtToClient, comparePassword } = require('../utils/authorization');
const { loginQuery, registerQuery, userFoundQuery } = require('../queries/queries');
const bcrypt = require('bcrypt');

const saltRounds = 10;

async function loginUser({ username, password }) {
   
    
    const values = [username];
    
    const resPg = await pool.query(loginQuery, values);
    if (resPg.rows.length === 0) {
      throw new Error('Kullanıcı bulunamadı');
    }

    const user = resPg.rows[0];
    const password_hash = user.password;

    const isValid = await comparePassword(password, password_hash);
    if (!isValid) {
      throw new Error('Kullanıcı adı veya Parola Yanlış');
    }

    // Token üret
    const token = await sendJwtToClient({ id: user.id, username: user.username }); 

    // Geri dönüşte user bilgileri ve token ver
    return { token, user };
}

async function registerUser({ username, password, email }) {
  
  const existingUser = await pool.query(
    userFoundQuery,
    [email]
  );
  if (existingUser.rows.length > 0) {
    throw new Error('Bu e-posta adresi zaten kullanımda');
  }
    
  try {
    
    const hash = await bcrypt.hash(password, saltRounds);
    const values = [username, new Date(Date.now()), email, hash];
    const resPg = await pool.query(registerQuery, values);
    const user = resPg.rows[0];

    const token = await sendJwtToClient({ id: user.id, username: user.username });

  
    return { token, user };
  } 
  catch (err) {
    if (err.code === '23505') {
      throw new Error('Kullanıcı adı veya e-posta zaten kullanılıyor');
    }
    throw err; 
  }
};

module.exports = {
  loginUser,
  registerUser
};