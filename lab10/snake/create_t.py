# init_db.py
import psycopg2

conn = psycopg2.connect(
    dbname="snake",
    user="postgres",
    password="asyl",  
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    username TEXT REFERENCES users(username),
    score INTEGER,
    level INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
cur.close()
conn.close()

print("✅ Таблицы успешно созданы.")
