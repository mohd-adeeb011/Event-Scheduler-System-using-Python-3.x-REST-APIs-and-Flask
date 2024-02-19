import sqlite3

conn=sqlite3.connect("eventsheduler.sqlite")

cursor=conn.cursor()

sql_query="""CREATE TABLE events (
id integer PRIMARY KEY,
title text NOT NULL,
start text NOT NULL,
end text NOT NULL
)"""

cursor.execute(sql_query)