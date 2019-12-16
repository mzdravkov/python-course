import sqlite3 as sqlite


DB_NAME = "example.db"

conn = sqlite.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS post
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS comment
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        post_id INTEGER,
        FOREIGN KEY(post_id) REFERENCES post(id)
    )
''')
conn.commit()


class SQLite(object):

    def __enter__(self):
        self.conn = sqlite.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
