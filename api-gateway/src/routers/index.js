const express = require("express")
const router = express.Router()
const user = require("./user")





//router.use("/recognizer", recognizer)

router.use("/user", user)
/*router.use("/voice", voice)
router.use("/db", db)
router.use("/device", device)*/
module.exports = router