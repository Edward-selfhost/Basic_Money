import sqlite3

db_path=("/home/edward/Documents/Vsc/Basic_Money/Basic_Money.db")

def create_table():

    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data (
        date TEXT PRIMARY KEY,
        income INTEGER NOT NULL,
        expense INTEGER NOT NULL,
        saving INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def add_data(date, income, expense, saving):
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute("INSERT INTO data (date,income,expense,saving) VALUES(?,?,?,?)", (date,income,expense,saving))
    
    conn.commit()
    conn.close()

def show_data():
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    conn.close()
    return rows

def edit_data(date, income, expense, saving):
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    conn.execute("""
    UPDATE data
    SET income = ?, expense = ?, saving = ?
    where date = ?
    """,(income,expense,saving,date))

    conn.commit()
    cursor.close()

create_table()