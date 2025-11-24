import os.path
import sqlite3

def init_db() -> None:
    with sqlite3.connect("artilog.db") as connect_db:
        cursor = connect_db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS arti_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL,
                message TEXT NOT NULL,
                time_stamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                tags TEXT
            )
        ''')
        connect_db.commit()

def add_log(target_file: str, message: str, tags: str = "No tags") -> None:

    connect_db = sqlite3.connect("artilog.db")
    cursor = connect_db.cursor()
    cursor.execute('''
                    INSERT INTO arti_log (file_name, message, tags)
                    VAlUES (?,?,?)''', (target_file, message, tags))
    
    connect_db.commit()
    connect_db.close()


def main():
    print("Hello from artilog!")
    init_db()
    print("Database inisilised")

    add_log("README.md", "Starting message", "Admin")
    add_log("README.md", "Second message")
    

if __name__ == "__main__":
    main()