import sqlite3
import os

# ایجاد مسیر مطلق برای پایگاه داده
DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'network_data.db')

def init_db():
    try:
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
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")

def insert_speed_test(data):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO speed_tests (download, upload, ping) VALUES (?, ?, ?)', 
                       (data["download"], data["upload"], data["ping"]))
        conn.commit()
        conn.close()
        print("Speed test data inserted successfully!")
    except Exception as e:
        print(f"Error inserting speed test data: {e}")

def insert_bandwidth_usage(data):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # اگر داده‌ها برای چند رابط شبکه باشد، باید هرکدام را به طور جداگانه وارد کنیم
        if isinstance(data, dict):  # بررسی اینکه آیا data یک دیکشنری است
            for interface, usage in data.items():
                cursor.execute('INSERT INTO bandwidth_usage (sent, received) VALUES (?, ?)',
                               (usage["sent"], usage["received"]))
        else:
            cursor.execute('INSERT INTO bandwidth_usage (sent, received) VALUES (?, ?)',
                           (data["sent"], data["received"]))
        
        conn.commit()
        conn.close()
        print("Bandwidth usage data inserted successfully!")
    except Exception as e:
        print(f"Error inserting bandwidth usage data: {e}")

# فراخوانی تابع برای تست
init_db()
