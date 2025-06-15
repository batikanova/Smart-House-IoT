

require('dotenv').config();


const {JWT_COOKIE, NODE_ENV} = process.env

const authService = require('../services/user.js');

const login = async (req, res, next) => {
  try {
    const { username, password } = req.body;
    console.log("Login request received:", { username, password });

    const { token, user } = await authService.loginUser({ username, password });

    res.status(200)
      .cookie('access_token', token, {
        httpOnly: true,
        expires: new Date(Date.now() + parseInt(JWT_COOKIE) * 1000 * 60),
        secure: NODE_ENV === 'development' ? false : true,
      })
      .json({
        success: true,
        access_token: token,
        data: {
          name: user.username,
          email: user.email,
        },
        time: new Date(),
      });
  } catch (error) {
    res.status(400).json({
      success: false,
      message: error.message,
    });
  }
};

const register = async (req, res, next) => {
    try {
        const { username, password, email } = req.body;
        console.log("Register request received:", { username, password, email });

        const { token, user } = await authService.registerUser({ username, password, email });

        res.status(201)
          .cookie('access_token', token, {
            httpOnly: true,
            expires: new Date(Date.now() + parseInt(process.env.JWT_COOKIE) * 1000 * 60),
            secure: process.env.NODE_ENV === 'development' ? false : true,
          })
          .json({
            success: true,
            access_token: token,
            data: {
              name: user.username,
              email: user.email,
            },
            time: new Date(),
          });
    } catch (error) {
        res.status(400).json({
            success: false,
            message: error.message,
        });
    }
};
module.exports = {login, register}