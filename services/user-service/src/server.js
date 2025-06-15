
const express = require("express")
const routers = require("./routers")
const dotenv = require("dotenv")


dotenv.config({
    path: ".env"
})


const app = express()
const PORT = process.env.PORT
const pool = require('./config/db');

pool.connect()

    .then(() => console.log("PostgreSQL veritabanına bağlandı"))
    .catch(err => console.error("PostgreSQL veritabanına bağlanırken hata:", err));

app.get("/",  function (req, res) {
    
    res.send(`<h1> User Service</h1>
    <p>Bu servis kullanıcı yönetimi ile ilgili işlemleri gerçekleştirmektedir.</p>
    <ul>
      <li><strong>Login:</strong> Kullanıcı girişi, username, password, email — <code>login</code></li>
      <li><strong>Register:</strong> Yeni kullanıcı kaydı, username, password, email — <code>register</code></li>
    </ul>`);
});


app.use(express.json())


app.use("/", routers)

app.listen(PORT, () => {
    console.log(`Sunucu Ayakta ${PORT}`)
})