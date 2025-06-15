const bcrypt = require("bcrypt")
const generateJwtFromUser = require("../models/user")

const sendJwtToClient = (user) => {
    
    const token = generateJwtFromUser(user.username, user.email)
    
    return token
}
const comparePassword = async (password, hash) => {
    
        const result = bcrypt.compareSync(password, hash)
        return result

};

module.exports = {sendJwtToClient, comparePassword}