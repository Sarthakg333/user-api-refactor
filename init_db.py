import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

sample_users = [
    ('John Doe', 'john@example.com', 'password123'),
    ('Jane Smith', 'jane@example.com', 'secret456'),
    ('Bob Johnson', 'bob@example.com', 'qwerty789')
]

cursor.executemany("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", sample_users)

conn.commit()
conn.close()

print("✅ Database initialized with sample data.")

