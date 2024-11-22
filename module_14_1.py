import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")


for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'user"{i}', f'example{i}@gmail.com', f'{i*10}', str(1000)))


for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance= ? WHERE id = ?", ('500', f'{i}'))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}',))

cursor.execute("SELECT username, email, age, balance FROM Users")

users = cursor.fetchall()
user_not = ['Имя: ', ' | Почта: ', ' | Возраст: ', ' | Баланс: ']
for user in users:
    for i in range(len(user)):
        print(user_not[i], end='')
        print(user[i], end='')
    print()

i = 6
cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}'))

cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
total2 = cursor.fetchone()[0]
print(total2 / total1)


connection.commit()
connection.close()