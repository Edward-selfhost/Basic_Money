import sqlite3,os,time
from pathlib import Path
from datetime import datetime

db_path=("/workspace/Transfer/projects/Python/Apps/Basic_Money/Basic_Money.db")

#db_path.parent.mkdir(parents=True,exist_ok=True)

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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def new_data_entry():
    date = input("Please enter the date of the data: (YYYY-MM-DD)")
    #date = datetime.now().strftime("%Y-%m-%d")
    income = input("please enter your income:")
    expense = input("Pleae enter your expense:")
    saving = input("Please enter your savings:")
    
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute("INSERT INTO data (date,income,expense,saving) VALUES(?,?,?,?)", (date,income,expense,saving))
    conn.commit()
    conn.close()
    main()

def show_data():
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    print("| DATE      | Income | Expenses | Savings | ")
    for row in rows:
        print(f"|{row[0]} | {row[1]}     | {row[2]}       | {row[3]}      |")
    main()

def edit_data():
    date = input("What is the data of the entry you want to edit? (YYYY-MM-DD)")
    print("Please enter the new correct data.")
    income = input("please enter your income:")
    expense = input("Pleae enter your expense:")
    saving = input("Please enter your savings:")

    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    conn.execute("""
    UPDATE data
    SET income = ?, expense = ?, saving = ?
    where date = ?
    """,(income,expense,saving,date))

    conn.commit()
    cursor.close()
    main()

def main():
    print()
    print("What would you like to do?")
    print("1 --- Add a data entry")
    print("2 --- Show data")
    print("3 --- Edit a existing data entry")
    action = int(input())
    if action == 1:
        clear()
        new_data_entry()
    elif action == 2:
        clear()
        show_data()
    elif action == 3:
        clear()
        edit_data()
    else:
        print("Enter a vaild input.")
        time.sleep(2)
        clear()
        main()
main()