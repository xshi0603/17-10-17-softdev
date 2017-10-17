import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

courses = csv.DictReader(open("courses.csv"))
peeps = csv.DictReader(open("peeps.csv"))

command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"         #put SQL statement in this string
c.execute(command)    #run SQL statement

for rows in courses:
    command = "INSERT INTO courses VALUES (" + '"' + rows['code'] + '"' + ", " + rows['mark'] + ", " + rows['id'] + ")"
    print command
    c.execute(command)

command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"         #put SQL statement in this string
c.execute(command)    #run SQL statement

for rows in peeps:
    command = "INSERT INTO peeps VALUES ('" + rows['name'] + "', " + rows['age'] + ", " + rows['id'] + ")"
    print command
    c.execute(command)
    
#==========================================================
db.commit() #save changes
db.close()  #close database


