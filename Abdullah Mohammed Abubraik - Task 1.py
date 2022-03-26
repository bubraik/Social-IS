# %%
print('hello from vscode with jupyter extension')

# %%
mystring = "hello"
myint = 12
 
print(mystring)
print(myint)

# %%
mystring
myint

# %%
no_of_apples = 2

if no_of_apples <1:
    print("u have no apples")
elif no_of_apples ==1:
    print("u have one apple")
elif no_of_apples <4:
    print("u have few apples")
else:
    print("u have alot of apples")

# %%
stu_names = ['Mohammed', 'Ali', 'Magdy', 'Marwa']
stu_names[0]
stu_names[1]
stu_names[3]
stu_names[-1]

# %%
stu_names[0:2]

# 

# %%
stu_names[2:4]

# %%
stu_names[2:]

# %%
stu_names[:2]

# %%
stu_names.append("khaled")
stu_names

# %%
stu_names.remove("Abdullah")


# %%
stu_names.insert(0,"Aliaa")
stu_names

# %%
del stu_names[4]

# %%
stu_names

# %%
stu_names.append("tamer")
stu_names.append("tamer")

# %%
for student in stu_names:
    print('Hello ' + student + ' ❤')


# %%
long_names = []
for student_name in stu_names:
    # This is our criterion
    if len(student_name) > 4:
        long_names.append(student_name)

long_names


# %%
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        student_pairs.append(
            (student_name_0, student_name_1)
        )

student_pairs


# %%
student_pairs[0]


# %%
student_grade = ('Alice', 'Spanish', 'A-')
student_grade


# %%
student_grade[1]


# %%
student_grade = ('Alice', 'Spanish', 'A-')
student_name, subject, grade = student_grade

print(student_name)
print(subject)
print(grade)


# %%
student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]
for student_name, subject, grade in student_grades:
    if grade.startswith('A'):
        print('Congratulations', student_name,
              'on getting an', grade,
              'in', subject)


# %%
for student_grade in student_grades:
    if student_grade[2].startswith('A'):
        print('Congratulations', student_grade[0],
              'on getting an', student_grade[2],
              'in', student_grade[1])


# %%
foreign_languages = {
    'Alice': 'Spanish',
    'Bob': 'French',
    'Carol': 'Italian',
    'Dave': 'Italian',
}


# %%
foreign_languages['Bob']

# %%
'Zeke' in foreign_languages


# %%
'bob' in foreign_languages


# %%
'Bob' in foreign_languages


# %%
foreign_languages['Esther'] = 'French'
foreign_languages


# %%
for key in foreign_languages:
    val = foreign_languages[key]
    print(key, " is taking" , val)

# %%
for key,value in foreign_languages.items():
    print(key,"is taking ",value)

# %%
student_grade = ('Alice', 'Spanish', 'A')


# %%
student_name, subject, grade = student_grades[0]
print(student_name, 'got a grade of', grade, 'in', subject)


# %%
record = {
    'name': 'Alice',
    'subject': 'Spanish',
    'grade': 'A',
}
print(record['name'],
      'got a grade of', record['grade'],
      'in', record['subject'])


# %%
student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]


# %%
student_grades[1]

# %%
student_grades[1][2]

# %%
student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records


# %%
student_grade_records[1]


# %%
student_grade_records[1]['grade']


# %%
for record in student_grade_records:
    if record['grade'].startswith('A'):
        print('Congratulations', record['name'], 
              'on getting an', record['grade'], 
              'in', record['subject'])


# %%
foreign_language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    foreign_language_grades[student_name] = record
    
foreign_language_grades


# %%
foreign_language_grades['Alice']


# %%
foreign_language_grades['Alice']['grade']


# %%
student_course_grades = {}
for student_name, subject, grade in student_grades:
    student_course_grades[student_name, subject] = grade
    
student_course_grades


# %%
student_course_grades['Alice', 'Math'] = 'A'
student_course_grades['Alice', 'History'] = 'B'


# %%
student_course_grades


# %%
student_report_cards = {}
for student_name, subject, grade in student_grades:
    # If there is no report card for a student,
    # we need to create a blank one
    if student_name not in student_report_cards:
        student_report_cards[student_name] = {}
    student_report_cards[student_name][subject] = grade


# %%
student_report_cards


# %%
student_report_cards['Alice']['Math'] = 'A'
student_report_cards['Alice']['History'] = 'B'


# %%
student_report_cards


# %%
student_report_cards['Alice']


# %%



