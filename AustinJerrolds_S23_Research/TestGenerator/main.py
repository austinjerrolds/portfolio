import random
from Student import Student
from LinkedList import LinkedList
from DataMethods import generate_question_time, plus_one_jumps, minus_one_jumps, generate_grade
import csv

if __name__ == "__main__":

    studentList = LinkedList()  # initialize list of students

    examTime = int(input("How much time is given to take the exam?"))  # take user input
    totalStudents = int(input("How many students are in the class?"))
    totalQuestions = int(input("How many questions are on the exam?"))
    cheater = 0

    choiceOfStudent = ["badStudent", "averageStudent", "goodStudent", "cheaterFast", "cheaterSlow"]  # student profiles

    file = open('exams.csv', 'w', newline='')
    writer = csv.writer(file)

    for i in range(totalStudents):
        # generate attributes
        student_id = i + 1  # assign each student object an id
        # randomly choose student type given weights
        studentType = random.choices(choiceOfStudent, weights=(10, 83, 5, 1, 1), k=1)

        if studentType == ['averageStudent']:  # used for formatting student type
            studentType = "Average Student"
        elif studentType == ['goodStudent']:
            studentType = "Good Student"
        elif studentType == ['badStudent']:
            studentType = "Bad Student"
        elif studentType == ['cheaterFast']:
            studentType = "Cheater Fast"
        elif studentType == ['cheaterSlow']:
            studentType = "Cheater Slow"

        if studentType == "Cheater Slow" or studentType == "Cheater Fast":
            cheater = 1  # cheater = 1 if the student is a cheater
        else:
            cheater = 0

        time_array = generate_question_time(examTime, totalQuestions, studentType)  # generate time array
        minus_jumps = minus_one_jumps(totalQuestions, time_array, studentType)
        forward_jumps = plus_one_jumps(totalQuestions, time_array, minus_jumps, studentType)
        grade = generate_grade(studentType)

        studentObject = Student(student_id, sum(time_array), time_array, studentType, minus_jumps, forward_jumps, grade)
        studentList.append_node(studentObject)
        output = [sum(time_array), minus_jumps, forward_jumps, grade, cheater]
        writer.writerow(output)

    studentList.print_list()
    file.close()


