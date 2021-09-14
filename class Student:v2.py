class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade >= 0 and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else:
            return "Ошибка"

    def __str__(self):
        my_str = "\nИмя: " + self.name + "\nФамилия: " + self.surname + "\ngender: " + self.gender + "\nСредняя оценка за домашнее задание: " + str(self.average_rating()) + "\nКурсы в процессе изучения: "
        for course in self.courses_in_progress:
            my_str += course.str()
        for course in self.finished_courses:
            my_str += "\nЗавершенные курсы: " + course.str()

        return my_str

    def average_rating(self):
        sum = 0
        count = 0
        for course in self.grades:
            for hw in self.grades[course]:
                sum += int(hw)
                count +=1
        if count == 0:
            return 0
        else:
            return sum//count

    def __eq__ (self, other):
        if isinstance (other, Student):
            return self.average_rating() == student2.average_rating()
        return False

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def average_rating(self):
        sum = 0
        count = 0
        for course in self.grades:
            for rates in self.grades[course]:
                sum += int(rates)
                count += 1
        if count == 0:
            return 0
        return sum // count

    def __str__(self):
        return "\nИмя: " + self.name + "\nФамилия: " + self.surname + "\nСредняя оценка за лекции: " + str(self.average_rating())

    def __eq__ (self, other):
        if isinstance (other, Lecturer):
            return self.average_rating() == lecturer2.average_rating()
        return False

class Reviewer(Mentor):

    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def str(self):
        return "\nИмя: " + self.name + "\nФамилия: " + self.surname

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

student = Student("Ruoy", "Eman", "M")
print(student.__str__())
student2 = Student("Aragorn", "Ranger of the North", "M")
print(student2.__str__())
lecturer = Lecturer("Some", "Buddy")
print(lecturer.__str__())
lecturer2 = Lecturer("Frodo", "Buggins")
print(lecturer2.__str__())
reviewer = Reviewer ("Some", "Buddy")
print(reviewer.__str__())

student.average_rating()
student.rate_lecturer("Intro to Classes", "Python", 5)
lecturer.average_rating()
reviewer.rate_hw(best_student, "Python", 5)
student.__str__()
lecturer.__str__()
reviewer.__str__()

def student_average_rating(students, course):
    sum = 0
    count = 0
    for student in students:
         if course in student.grades:
            for grade in student.grades[course]:
                sum += grade
                count += 1
    if count == 0:
        return 0
    else:
        return sum//count

def lecturer_average_rating(lecturers, course):
     sum = 0
     count = 0
     for lecturer in lecturers:
         if course in lecturer.grades:
            for grade in lecturer.grades[course]:
                sum += grade
                count += 1
         if count == 0:
            return 0
     else:
      return sum//count

print(student_average_rating([best_student, student], "Python"))
print(lecturer_average_rating([lecturer], "Python"))