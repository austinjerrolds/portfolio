import random


def generate_question_time(exam_time: int, total_questions: int, student_type: str):
    total_time = 0
    time_array = []
    distribution = 0
    mean = 0

    if student_type == "Average Student":  # print student profile type - remove later
        distribution = random.uniform(.9, 1.1)  # set question distribution based on profile
        mean = (exam_time / total_questions)
    elif student_type == "Good Student":
        distribution = random.uniform(0.6, .8)
        mean = (exam_time / (total_questions * 1.5))
    elif student_type == "Bad Student":
        distribution = random.uniform(1.5, 1.8)
        mean = (exam_time / total_questions)
    elif student_type == "Cheater Fast":
        mean = (exam_time / (total_questions * 4))  # this cheater type finishes the exam in less than half the time
        distribution = random.uniform(0.3, 0.5)
    elif student_type == "Cheater Slow":
        mean = (exam_time / total_questions)
        distribution = random.uniform(0.1, 0.2)

    for j in range(total_questions):  # generate question times based on amount of questions

        time_per_question = abs(round(random.gauss(mean, distribution), 2))
        if time_per_question == 0.00:
            time_per_question = 0.2

        if total_time + time_per_question > exam_time:  # if they go over the exam time finish current question
            time_per_question = round(exam_time - total_time, 2)
            time_array.append(time_per_question)
            total_time = round(total_time + time_per_question, 2)
        else:
            time_array.append(time_per_question)  # store question time
            total_time = round(total_time + time_per_question, 2)  # calculate total time
    return time_array


def minus_one_jumps(num_questions: int, question_array: list[float], student_type: str):
    if student_type == "Cheater Fast":  # if the student is of this cheater type they do not check their answers
        return 0
    elif student_type == "Cheater Slow":
        minus_jumps = random.randint(10, 15)
    else:
        minus_jumps = random.randint(0, 1)

    if minus_jumps >= 1 and question_array[num_questions - 1] == 0:
        # if they did not finish exam they do not check answers
        minus_jumps = 0

    return minus_jumps


def plus_one_jumps(num_questions: int, question_array: list[float], minus_jumps: int, student_type: str):
    jumps = 0
    num_returns = minus_jumps / 3  # the amount of times they go backwards that we will update
    for n in range(len(question_array)):  # generate jumps based on questions completed
        if question_array[n] > 0:
            jumps += 1

    if minus_jumps >= 1 and jumps == num_questions and student_type == "Cheater Slow":
        # this loop is used to generate the forward jumps when the cheater slow type is jumping back and forth
        while num_returns > 0:
            new_index = int(random.randint(0, num_questions - 1))  # generate more forward jumps
            for k in range(new_index, random.randint(new_index, num_questions - 1)):
                if question_array[k] > 0:
                    jumps += 1
            num_returns -= 1

    elif minus_jumps >= 1 and jumps == num_questions:  # if they reach the end of the test and go back
        new_index = int(random.randint(0, jumps))  # generate more forward jumps
        for k in range(new_index, random.randint(new_index, jumps)):
            if question_array[k] > 0:
                jumps += 1
    return jumps


def generate_grade(student_type: str):  # generates a random integer between those ranges depending on student type
    if student_type == "Average Student":
        return random.randint(70, 85)
    elif student_type == "Good Student":
        return random.randint(80, 100)
    elif student_type == "Bad Student":
        return random.randint(40, 70)
    elif student_type == "Cheater Fast":
        return random.randint(95, 100)
    elif student_type == "Cheater Slow":
        return random.randint(95, 100)
