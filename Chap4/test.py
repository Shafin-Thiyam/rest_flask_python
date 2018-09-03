import sqlite3

con=sqlite3.connect('data.db')

cursor=con.cursor()
create_table="CREATE TABLE users(id int, username text, password text)"
cursor.execute(create_table)
user= (1, 'shafin', 'haiqa')
insert_q="INSERT INTO users values (?, ?, ?)"
cursor.execute(insert_q, user)

users=[
    (2, 'haiqa', 'shafin'),
    (3, 'hamna', 'haiqa')
]
cursor.executemany(insert_q,users)
select_q="select * from users"
for row in cursor.execute(select_q):
    print(row)
con.commit()
con.close()
