const {voiceRecognizing} = require("../controllers/recognizer")
const express = require("express")
const router = express.Router()
const authenticate = require("../middlewares/authorization")

router.post("/recognizer", authenticate, voiceRecognizing)


module.exports = router