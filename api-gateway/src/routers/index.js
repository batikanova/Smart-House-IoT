const express = require("express")
const router = express.Router()
const user = require("./user")
const voice = require("./voice")





//router.use("/recognizer", recognizer)

router.use("/user", user)
router.use("/voice-auth", voice)
module.exports = router