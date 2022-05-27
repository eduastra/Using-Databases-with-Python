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


