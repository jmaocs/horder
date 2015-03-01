import sqlite3

user_table = sqlite3.connect('/home/jmao/horder/db/user.db') # Warning: This file is created in the current directory
user_table.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, first_name char(100) NOT NULL, last_name char(100) NOT NULL, email char(100) NOT NULL)")
user_table.execute("INSERT INTO user (first_name,last_name, email) VALUES ('jing', 'mao', 'jingmao88@gmail.com')")
user_table.commit()

