# Sibel Akayoğlu
# HW4 - SIMPLE STUDENT MANAGEMENT SYSTEM

import os

class student:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.lessons = []

    def __str__(self):
        return self.__name + " " + self.__surname

    def full_name(self):
        return self.__name + " " + self.__surname
    
    def add_lesson(self):
        os.system("cls")
        x=1
        y=1

        for c in course_list:
            print("{} - {}".format(x,c))
            x += 1

        chosen_course = int(input('\nSelected course number is '))
        chosen_course -= 1

        os.system("cls")
        for l in lesson_list:
            print("{} - {}".format(y,l))
            y += 1

        chosen_lesson = int(input('\nSelected lesson number is '))
        chosen_lesson -= 1

        self.exam = {"midterm":0,"final":0,"project":0}
        self.lessons.append([course_list[chosen_course], lesson_list[chosen_lesson], self.exam])
    
    def add_exam(self):
        counter = 1
        os.system("cls")
        for s in self.lessons:
            print("{} - {} {}".format(counter, s[0], s[1]))
            counter += 1
            
        chosen_item = int(input('\nSelected lesson number is '))
        chosen_item -= 1

        self.exam = {"midterm":0,"final":0,"project":0}
        self.exam["midterm"] = input('\nMidterm is ')
        self.exam["final"] = input('Final is ')
        self.exam["project"] = input('Project is ')

        self.lessons[chosen_item][2] = self.exam

    def show_lessons(self):
        os.system("cls")
        for s in self.lessons:
            print("##### {} {} #####".format(s[0], s[1]))
            print("Midterm : {}".format(s[2]["midterm"]))
            print("Final : {}".format(s[2]["final"]))
            print("Project : {}".format(s[2]["project"]))

            puan = self.calculate_grade(s[2])

            print("Grade Sum : {}".format(puan))
            print("Letter : {}\n".format(self.calculate_letter(puan))) 

    def calculate_grade(self, lesson):
        midterm = float(lesson["midterm"]) * 0.3
        final = float(lesson["final"]) * 0.5
        project = float(lesson["project"]) * 0.2
        return int(midterm + final + project)

    def calculate_letter(self, grade):
        if grade >= 90:
            grade = "AA"
        elif 70 <= grade < 90:
            grade = "BB"
        elif 50 <= grade < 70:
            grade = "CC"
        elif 30 <= grade < 50:
            grade = "DD"
        else:
            grade = "FF\n__FAILURE__"
        return grade

def initial_screen():
    os.system("cls")
    global is_found, neo, baslik_tire

    print("{}\n{}\n{}".format(baslik_tire,"[1] Add Student\n[2] Show Students\n[3] Show Course List\n[4] Enter the Matrix\n[E] Exit",baslik_tire))

    ops = input("Opinion: ")
    print()
    if ops == "1":
        student_name = input("Student name is ")
        student_surname = input("Student surname is ")
        students.append(student(student_name, student_surname))
        print('\nSuccessfully added...')
        input('\nPress any key to continue...')
        return True
    elif ops == "2":
        os.system("cls")
        print('_NAME SURNAME_')
        for s in students:
            print(s)
        input('\nPress any key to continue...')
        return True
    elif ops == "3":
        os.system("cls")
        print('_COURSE LIST_')
        for c in course_list:
            print(c)
        input('\nPress any key to continue...')
        return True
    elif ops == "4":
        os.system("cls")
        print(baslik_tire)
        print("Example:\nYour full name is Sibel Akayoğlu")
        print(baslik_tire)
        for i in range(3):
            full_name = input("Your full name is ", )
            for s in students:
                if s.full_name().upper() == full_name.upper():
                    neo = s
                    is_found = True
                    break
            if is_found:
                break
            else:
                print("Student name and surname are invalid!")
        if not is_found:
            print('\n Please try again later!') 
            input('\nPress any key to continue...')
        return True    
    elif ops.upper() == "E":
        return False
    else:
        print('Invalid choice!\n')
        return True
    
    input('Press any key to continue...')

def student_screen():
    os.system("cls")
    global is_found, neo, baslik_tire
    add_invisible = True
    show_invisible = True
    exam_invisible = True

    print('Welcome {}\n'.format(neo))

    if len(neo.lessons) < 3:
        print("Take minimum 3 lesson !")
        print("{}\n{}\n{}".format(baslik_tire,"[1] Add a Lesson\n[B] Back to Main",baslik_tire))
        show_invisible = False
        exam_invisible = False
    elif 3 <= len(neo.lessons) < 5:
        print("{}\n{}\n{}".format(baslik_tire,"[1] Add a Lesson\n[2] Add an Exam\n[3] Calculate Lessons Grades\n[B] Back to Main",baslik_tire))
    elif len(neo.lessons) >= 5:
        print("not more 5 lessons")
        print("{}\n{}\n{}".format(baslik_tire,"[3] Show Lessons\n[B] Back to Main",baslik_tire))
        add_invisible = False
        
    ops = input("Opinion: ")
    print()

    if ops == "1":
        neo.add_lesson() if add_invisible else print('Invalid choice!\n')
    elif ops == "2":
        neo.add_exam() if exam_invisible else print('Invalid choice!\n')
    elif ops == "3":
        neo.show_lessons() if show_invisible else print('Invalid choice!\n')
    elif ops.upper() == "B":
        neo = None
        print("Backing to real world.")
        is_found = False 
    else:
        print('Invalid choice!\n')
    
    input('Press any key to continue...')

if __name__ == '__main__': 
    baslik_tire = "-" * 30
    is_found = False
    neo = None
    students = []

    # Pre-defined Students
    students.append(student("Sibel", "Akayoğlu"))
    students.append(student("Emre", "Akayoğlu"))

    # Pre-defined Courses
    course_list = ['Hist','Sci','Math','Chem','Phy']
    lesson_list = ['101','102','103','104','105']
    
    while True:
        if is_found:
            student_screen() 
        else:
            if not initial_screen():
                break