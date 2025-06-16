const {voiceSave, voiceVerify} = require("../controllers/voice-auth")
const express = require("express")
const router = express.Router()
const authenticate = require("../middlewares/authorization")

router.post("/save", authenticate, voiceSave)
router.post("/verify", authenticate, voiceVerify)

module.exports = router