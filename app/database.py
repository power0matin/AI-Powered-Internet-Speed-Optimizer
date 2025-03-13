import sqlite3

DB_PATH = 'data/network_data.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS speed_tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            download REAL,
            upload REAL,
            ping REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bandwidth_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sent REAL,
            received REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_speed_test(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO speed_tests (download, upload, ping) VALUES (?, ?, ?)', 
                   (data["download"], data["upload"], data["ping"]))
    conn.commit()
    conn.close()

def insert_bandwidth_usage(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bandwidth_usage (sent, received) VALUES (?, ?)',
                   (data["sent"], data["received"]))
    conn.commit()
    conn.close()