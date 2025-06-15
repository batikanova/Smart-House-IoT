const jwt = require("jsonwebtoken")

generateJwtFromUser = function(name, email){
    const {JWT_SECRET_KEY, JWT_EXPIRE} = process.env
    const payload = {
        name:name,
        email:email
    }
    
    const token = jwt.sign(payload, JWT_SECRET_KEY, {
        expiresIn: JWT_EXPIRE
    })
    return token
}

module.exports = generateJwtFromUser