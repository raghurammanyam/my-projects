"""" this python script is used to insert the data from csv files to database tables in appropriate columns """

import csv
import MySQLdb
HOST = 'localhost'
USER = 'ram'
PASSWORD = 'Raghuram@9'
DATABASE = 'studentreport'


db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
cursor = db.cursor()
#cursor.execute('CREATE TABLE IF NOT EXISTS DETAILS_studentmarks (student_name VARCHAR(30), subject VARCHAR(30),  marks FLOAT(100,2))')
#cursor.execute('CREATE TABLE IF NOT EXISTS DETAILS_subjectfaculty (subject VARCHAR(30), name VARCHAR(30))')

with open('/home/hp/dev/STUDENTS_REPORT/DETAILS/subject_faculty.csv','r') as subject_csv:
    subject_data = csv.reader(subject_csv)
    for y in subject_data:
        print (y)
        cursor.execute('INSERT INTO DETAILS_subject (name,faculty) values(%s ,%s  )',(y[0],y[1]))
with open('/home/hp/dev/STUDENTS_REPORT/DETAILS/student_marks.csv','r') as marks_csv:
    student_data = csv.reader(marks_csv)
    for x in student_data:
        #print (x[2],float(x[2]))
        cursor.execute('INSERT INTO DETAILS_studentmarks (student_name,subject,marks) values(%s ,%s ,%s )',(x[0],x[1],x[2]))

db.commit()
cursor.close()
