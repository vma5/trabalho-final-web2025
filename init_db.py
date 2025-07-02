import sqlite3

conn = sqlite3.connect('meds.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS meds (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  dosage TEXT,
  time TEXT NOT NULL
);
''')
conn.commit()
conn.close()
print('Banco inicializado.')