import sqlite3




def create_table_username():
    connection = sqlite3.connect("data_access/mft_db.db")
    cursor = connection.cursor()
    cursor.execute(" create table if not exists users (id integer primary key  autoincrement, username text, password text, nickname text, locked boolean)")
    connection.commit()
    connection.close()


def save_username(username,password,nickname, locked):
    connection = sqlite3.connect("data_access/mft_db.db")
    cursor = connection.cursor()
    cursor.execute("insert into users (username , password , nickname, locked) values(?,?,?,?)",
                   [username, password, nickname, locked])
    connection.commit()
    connection.close()