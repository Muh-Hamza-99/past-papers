class Test:
    def __init__(self, name, grade, stream):
        self.__name = name
        self.__grade = grade
        self.__stream = stream
    def get_test_name(self):
        return self.__name
    def get_test_grade(self):
        return self.__grade
    def get_test_stream(self):
        return self.__stream

class Quiz(Test):
    def __init__(self, name, grade, stream, num_of_questions, num_of_students):
        Test.__init__(self, name, grade, stream)
        self.__out_of = 10
        self.__num_of_questions = num_of_questions    
        self.__num_of_students = num_of_students 
        self.__mcqs = [MCQ for i in range(self.__num_of_questions)]
    def __del__(self):
        for i in range(0, self.__num_of_questions):
            del self.__mcqs[i]
    def get_num_of_questions(self):
        return self.__num_of_questions
    def get_num_of_students(self):
        return self.__num_of_students
    def add_mcq(self, question, choices, correct_answer, marks_awarded):
        counter = 0
        if counter < self.__num_of_questions:
            self.__mcqs[counter] = MCQ(question, choices, correct_answer, marks_awarded)
            counter += 1
        else:
            print(f"Maximum number of questions is {self.__num_of_questions}")
    def print_mcqs(self):
        for i in range(0, self.__num_of_questions):
            current_mcq = self.__mcqs[i]
            print(f"Question {i + 1}:")
            print(f"{current_mcq.get_question()}")
            choices = current_mcq.get_choices()
            for choice in choices:
                print(f"{choice}", end=" ")
            print(f"Marks Awarded: {choice.get_marks_awarded()}")

class EOTExam(Test):
    def __init__(self, name, grade, stream, num_of_mcqs, num_of_short_answers, num_of_long_answers, num_of_students):
        Test.__init__(self, name, grade, stream)
        self.__out_of = 50
        self.__num_of_mcqs = num_of_mcqs
        self.__num_of_short_answers = num_of_short_answers    
        self.__num_of_long_answers = num_of_long_answers
        self.__num_of_students = num_of_students
        self.__mcqs = [MCQ for i in range(self.__num_of_mcqs)]
        self.__short_answers = [ShortAnswer for i in range(self.__num_of_short_answers)]
        self.__long_answers = [LongAnswer for i in range(self.__num_of_long_answers)]
    def __del__(self):
        for i in range(0, self.__num_of_mcqs):
            del self.__mcqs[i] 
        for i in range(0, self.__num_of_short_answers):
            del self.__short_answers[i]
    def print_mcqs(self):
        for i in range(0, self.__num_of_mcqs):
            current_mcq = self.__mcqs[i]
            print(f"Question {i + 1}:")
            print(f"{current_mcq.get_question()}")
            choices = current_mcq.get_choices()
            for choice in choices:
                print(f"{choice}", end=" ")
            print(f"Marks Awarded: {current_mcq.get_marks_awarded()}")
    def print_short_answers(self):
        for i in range(0, self.__num_of_short_answers):
            current_short_answer = self.__short_answers[i]
            print(f"Question {i + 1}:")
            print(f"{current_short_answer.get_question()}")
            print(f"Marks Awarded: {current_short_answer.get_marks_awarded()}")
    def print_long_answers(self):
        for i in range(0, self.__num_of_long_answers):
            current_long_answer = self.__long_answers[i]
            print(f"Question {i + 1}:")
            print(f"{current_long_answer.get_question()}")
            print(f"Marks Awarded: {current_long_answer.get_marks_awarded()}")

class MCQ:
    def __init__(self, question, choices, correct_answer, marks_awarded=1):
        self.__question = question
        self.__choices = choices
        self.__correct_answer = correct_answer
        self.__marks_awarded = marks_awarded
    def get_question(self):
        return self.__question
    def get_choices(self):
        return self.__choices
    def get_correct_answer(self):
        return self.__correct_answer
    def get_marks_awarded(self):
        return self.__marks_awarded

class ShortAnswer:
    def __init__(self, question, marks_awarded=2):
        self.__question = question
        self.__marks_awarded = marks_awarded
    def get_question(self):
        return self.__question
    def get_marks_awarded(self):
        return self.__marks_awarded

class LongAnswer:
    def __init__(self, question, marks_awarded=4):
        self.__question = question
        self.__marks_awarded = marks_awarded
    def get_question(self):
        return self.__question
    def get_marks_awarded(self):
        return self.__marks_awarded