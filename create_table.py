import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS pizzas (id INTEGER PRIMARY KEY, name text, price float)"
curosr.execute(create_table)

insert_table = "INSERT INTO pizzas "
create_table = "CREATE TABLE IF NOT EXISTS cart (id INTEGER PRIMARY KEY, name text, price float)"
curosr.execute(create_table)

connection.commit()

connection.close()
