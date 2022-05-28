from fileinput import filename
import sqlite3
import json

dbname = "roster.sqlite"
conn =sqlite3.connect(dbname)
cur = conn.cursor()

cur.executescript('''
   DROP TABLE IF EXISTS User;
   DROP TABLE IF EXISTS Course;
   DROP TABLE IF EXISTS Member;

   CREATE TABLE User (
       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
       name TEXT UNIQUE
   );

   CREATE TABLE Course (
       id iNTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
       title TEXT UNIQUE
   );

   CREATE TABLE Member (
       user_id INTEGER,
       Role INTEGER,
       PRIMARY KEY(user_id, course_id)
   )
''')

data =json.load(open('roster_data.json'))

# insert data / entry is the name of our date entry.

for entry in data:
    user = entry[0]
    course = entry [1]
    instructor = entry[2]
#here we can direct each string from our JSON to SQL

    #inserting user
    user_statement = """INSERT OR IGNORE INTO User(name) VALUES( ? )"""
	SQLparams = (user, )
	cur.execute(user_statement, SQLparams)

    #inserting course
    course_statement = """INSERT OR IGNORE INTO Course(title) VALUES( ? )"""
	SQLparams = (course, )
	cur.execute(course_statement, SQLparams)

    #Getting user and course id
	courseID_statement = """SELECT id FROM Course WHERE title = ?"""
    SQLparams = (course, )
    cur.execute(courseID_statement. SQLparams)
    courseID = cur.fetchone()[0]

    userID_statement = """SELECT id FROM User WHERE name =?"""
    SQLparams = (user, )
    cur.execute = cur.fetchone()[0]

    #inserting all Entrys
    member_statement = """INSERT INTO Member(user_id, course_id, role)
		VALUES(?, ?, ?)"""
	SQLparams = (userID, courseID, instructor)
	cur.execute(member_statement, SQLparams)

#saving
conn.commit()

#testing and obtaining the results
test_statement = """
SELECT hex(User.name || Course.title || Member.role) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
"""
cur.execute(test_statement)
result = cur.fetchone()
print('RESULT: ' + str(result))

#Closing the connection
cur.close()
conn.close()