#coding = utf-8
__author__ = 'aresowj'

import sqlite3, os

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)	#Delete the file if exists

#Initialize database
conn = sqlite3.connect(db_file)
cur = conn.cursor()	#Get the cursor
cur.execute('create table user(id int primary key, name varchar(20), score int)')
cur.execute(r"insert into user values (1, 'Ares', 95)")
cur.execute(r"insert into user values (2, 'Bob', 63)")
cur.execute(r"insert into user values (3, 'Carry', 76)")
cur.close()
conn.commit()	#Apply changes
conn.close()

def get_score_in(low, high):
	conn = sqlite3.connect(db_file)
	cur = conn.cursor()	#Get the cursor
	#Sort by score, ascending by default
	cur.execute('select name from user where score >= ? and score <= ? order by score', (low, high))
	
	result = cur.fetchall()
	name = []
	
	for r in result:
		name.append(r[0])
		
	return name

def main():
	print(get_score_in(80, 95))
	print(get_score_in(60, 80))
	print(get_score_in(60, 100))

if __name__ == '__main__': main()
