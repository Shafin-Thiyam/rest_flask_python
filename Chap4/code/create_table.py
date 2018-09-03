import sqlite3
con=sqlite3.connect("data.db")
cursor=con.cursor()
create_table="create table if not exists users (id integer primary key, username text, password text)"
cursor.execute(create_table)
create_table="create table if not exists Item (name text, price real)"
cursor.execute(create_table)
con.commit()
con.close()
