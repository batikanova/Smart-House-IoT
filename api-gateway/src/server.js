
const express = require("express")
const routers = require("./routers")
const dotenv = require("dotenv")


dotenv.config({
    path: "../.env"
})


const app = express()
const PORT = process.env.PORT

app.get("/",  function (req, res) {
    
    res.send(`<h1>Microservices API Gateway</h1>
    <p>Bu gateway üzerinden aşağıdaki mikroservislere erişebilirsiniz:</p>
    <ul>
      <li><strong>User Service:</strong> Kullanıcı yönetimi, login, register — <code>/user/*</code></li>
      <li><strong>Voice Service:</strong> Ses Doğrulama, Kaydetme yönetimi — <code>/voice/*</code></li>
      <li><strong>Command Recognizer Service:</strong> Ses Tanıma — <code>/recognizer/*</code></li>
      <li><strong>Device Service:</strong> Cihaz yönetimi — <code>/device/*</code></li>
      <li><strong>Database Service:</strong> Veritabanı işlemleri — <code>/db/*</code></li>
    </ul>`);
});


app.use(express.json())


app.use("/", routers)

app.listen(PORT, () => {
    console.log(`Sunucu Ayakta ${PORT}`)
})