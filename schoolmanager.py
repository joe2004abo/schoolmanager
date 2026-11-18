import sys

school = {}


def add_student(school):
    print('please enter student id, name and city')
    studentid = int(input('>'))
    name = input('>')
    city = input('>')

    if studentid in school:
        print('This id already exists.')
    else:
        school[studentid] = {'name': name, 'city': city, 'grades': {}}
        print('Student added.')


def add_grade(school):
    print('please enter student id, course and grade')
    studentid = int(input('>'))
    course = input('>')
    grade = float(input('>'))

    if studentid not in school:
        print('Student not found.')
    else:
        school[studentid]['grades'][course] = grade
        print('Grade added.')


def showallstudents(school):
    if not school:
        print('No students yet.')
    else:
        print('this is the students')
        for k, v in school.items():
            print(k, v['name'], v['city'], len(v['grades']))


def showonestudentreport(school):
    print('please enter student id')
    studentid = int(input('>'))
    if studentid not in school:
        print('student not found')
    else:
        student = school[studentid]
        print(student['name'], student['city'])
        if not student['grades']:
            print('no grades yet')
        else:
            for course, grade in student['grades'].items():
                print(course, grade)
            average = sum(student['grades'].values()) / len(student['grades'])
            print('Average:', average)


def top_student(school):
    if not school:
        print('no data found')
        return

    best_name = None
    best_average = -1

    for studentid, student in school.items():
        if not student['grades']:
            continue
        average = sum(student['grades'].values()) / len(student['grades'])
        if average > best_average:
            best_average = average
            best_name = student['name']

    if best_name is None:
        print('No grades yet.')
    else:
        print('Top student:', best_name, best_average)


def subject_averages(school):
    if not school:
        print('no data found')
        return

    totals = {}
    counts = {}

    for studentid, student in school.items():
        for course, grade in student['grades'].items():
            totals[course] = totals.get(course, 0) + grade
            counts[course] = counts.get(course, 0) + 1

    if not totals:
        print('No grades yet.')
    else:
        for course in totals:
            print(course, totals[course] / counts[course])


while True:
    print('\n===== Student Manager =====')
    print('1. Add student')
    print('2. Add grade')
    print('3. Show all students')
    print('4. Show one student report')
    print('5. Top student')
    print('6. Subject averages')
    print('7. Undo last change')
    print('8. Exit')

    choice = input('>')

    if choice == '1':
        add_student(school)
    elif choice == '2':
        add_grade(school)
    elif choice == '3':
        showallstudents(school)
    elif choice == '4':
        showonestudentreport(school)
    elif choice == '5':
        top_student(school)
    elif choice == '6':
        subject_averages(school)
    elif choice == '7':
        print('Undo not built yet.')
    elif choice == '8':
        sys.exit()
    else:
        print('Invalid choice')