import sqlite3




def create_table_username():
    connection = sqlite3.connect("data_access/mft_db.db")
    cursor = connection.cursor()
    cursor.execute(" create table username (id integer primary key  autoincrement, username text, password text, nickname text)")
    connection.commit()
    connection.close()


def save_username(username,password,nickname):
    connection = sqlite3.connect("data_access/mft_db.db")
    cursor = connection.cursor()
    cursor.execute("insert into username (username , password , nickname) values(?,?,?)",
                   [username, password, nickname])
    connection.commit()
    connection.close()