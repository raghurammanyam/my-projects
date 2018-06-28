import random
import csv
students = ['student'+str(i) for i in range(1, 101)]

faculties  = [('Mathematics', 'Murali Krishna'), ('Telugu', 'Amarnath'), ('English', 'Samuel'),
              ('Social', 'Krishna Reddy'), ('Physics', 'Raja Gopal'), ('Chemistry', 'Ravi') ]

with open('student_marks.csv', 'w') as f:
    #x=csv.writer(f)
    #x.writerow(['studentname','subject','marks'])

    for student in students:
        for sub, fac in faculties:
            f.write(','.join([student, sub, str(random.sample(range(1, 101), 1)[0])]) + '\n')

with open('subject_faculty.csv', 'w') as f:
    #y=csv.writer(f)
    #y.writerow(['subject','faculty'])

    for rec in faculties:
        f.write(','.join(rec) + '\n')
