const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  user: process.env.DB_USER || 'postgres',
  host: process.env.DB_HOST || 'localhost',
  database: process.env.DB_NAME || 'your_database_name',
  password: process.env.DB_PASSWORD || 'your_password',
  port: process.env.DB_PORT || 5432,
  max: 20,               // Maksimum bağlantı sayısı
  idleTimeoutMillis: 30000,  // Boşta kalma süresi sonrası bağlantıyı kapat
  connectionTimeoutMillis: 2000,  // Bağlantı zaman aşımı
});

pool.on('error', (err) => {
  console.error('Unexpected error on idle client', err);
  process.exit(-1);  // Kritik hata durumunda uygulamayı kapat
});

module.exports = pool;