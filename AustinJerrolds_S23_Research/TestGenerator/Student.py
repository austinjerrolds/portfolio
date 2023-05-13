

class Student:
    def __init__(self, student_id, total_time, time_per_question, student_type, m1_jumps, p1_jumps, grade):
        self.__id = student_id
        self.__time = total_time
        self.__question_array = time_per_question
        self.__student_type = student_type
        self.__plus_one_jumps = p1_jumps
        self.__minus_one_jumps = m1_jumps
        self.__exam_grade = grade

    @property
    def minus_one_jumps(self) -> int:
        return self.__minus_one_jumps

    @property
    def plus_one_jumps(self) -> int:
        return self.__plus_one_jumps

    @property
    def id(self) -> int:
        return self.__id

    @property
    def time(self) -> float:
        return self.__time

    @property
    def question_array(self) -> list[float]:
        return self.__question_array

    @property
    def student_type(self) -> str:
        return self.__student_type

    @property
    def exam_grade(self) -> int:
        return self.__exam_grade

    def __str__(self):
        return "Student: " + str(self.id) + "\nStudent Type: " + self.student_type + \
               "\nStudent Time: " + str(round(self.time, 2)) + \
               "\nQuestion Time Array: " + str(self.question_array) + "\n" + \
               "Minus one jumps: " + str(self.minus_one_jumps) + "\n" + \
               "Plus one jumps: " + str(self.plus_one_jumps) + "\n" + \
               "Exam grade: " + str(self.exam_grade) + "\n"

