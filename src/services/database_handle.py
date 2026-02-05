import sqlite3
from pathlib import Path

def create_db():
    db_path = Path("data/files.db")
    db_path.parent.mkdir(exist_ok=True)

    return db_path

def create_conn(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    return cur, conn

def close_conn(conn):
    conn.close()

def create_table(conn):
    with open("C:/Users/hunte/OneDrive/Documents/coding_projects/FileNeatly/migrations/001_intial.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())

def insert_statement(cur, conn):
    cur.execute("""
            INSERT INTO files VALUES
                      (1, 2, 'test', 'trial', 3);
            """)
    conn.commit()
    res = cur.execute("SELECT * FROM files")
    rows = res.fetchall()
    print(f"data: {rows}")
    

def db_loop():
    db_path = create_db()
    cur, conn = create_conn(db_path)
    create_table(conn)
    insert_statement(cur, conn)
    if input('input here') == "e":
        print("connection closed")
        close_conn(conn)

def main():
    db_loop()

if __name__ == "__main__":
    main()