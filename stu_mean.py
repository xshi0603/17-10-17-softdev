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
    #print command
    c.execute(command)

command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"         #put SQL statement in this string
c.execute(command)    #run SQL statement

for rows in peeps:
    command = "INSERT INTO peeps VALUES ('" + rows['name'] + "', " + rows['age'] + ", " + rows['id'] + ")"
    #print command
    c.execute(command)
    
#==========================================================

#==========================================================
def lookup(student_id):
    retList = []
    for x in c.execute("SELECT mark FROM courses WHERE id = %d;"%(student_id)):
        retList.append(x)
    return retList

def findavg(student_id):
    retVal = 0;
    counter = 0;
    for x in c.execute("SELECT mark FROM courses WHERE id = %d;"%(student_id)):
        retVal += x[0]
        counter += 1
    retVal = retVal / counter
    return retVal

def display():
    d = db.cursor()
    for x in d.execute("SELECT name, id FROM peeps"):
        print x[0] + " - " + str(x[1]) + " - " + str(findavg(x[1]))

def createTable():
    d = db.cursor()
    c.execute("CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)")
    
    for x in d.execute("SELECT id FROM peeps"):
        c.execute("INSERT INTO peeps_avg VALUES (%d, %d);"%(x[0], findavg(x[0])))
    
def changeGrade(student_id, new_grade, course):
    c.execute("UPDATE courses SET mark = %d WHERE id = %d AND code = \"%s\";"%(new_grade, student_id, course))

def addRow(student_id, mark, course):
    c.execute("INSERT INTO courses VALUES (\"%s\", %d, %d);"%(course, mark, student_id))
    
#==========================================================

#==========================================================

print("\nprinting ID 1")
print(lookup(1))
print("\nprinting ID 2")
print(lookup(2))

print("\nprinting avg 1")
print(findavg(1))
print("\nprinting avg 2")
print(findavg(2))

print("\ndisplaying")
display()

print("\ncreating table")
createTable()

print("\nchecking table")
for x in c.execute("SELECT * FROM peeps_avg"):
    print x

print("\nchanging grade in id 1")
print("\nbefore")
for x in c.execute("SELECT * FROM courses"):
    print x
    
changeGrade(1, 100, "systems")

print("\nafter")
for x in c.execute("SELECT * FROM courses"):
    print x

print("\nadding row")
print("\nbefore")
for x in c.execute("SELECT * FROM courses"):
    print x
    
addRow(1, 100, "apcs")

print("\nafter")
for x in c.execute("SELECT * FROM courses"):
    print x

                          
#==========================================================

db.commit() #save changes
db.close()  #close database


