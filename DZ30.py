class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"gender : {self.gender}, age : {self.age}, first_name : {self.first_name}, last_name : {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.gender}, {self.age}, {self.first_name}, {self.last_name}, {self.record_book} \n  "

class UserException(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if (len(self.group)) < 10:
            self.group.add(student)
        else:
            raise UserException("Ошибка добавления студента")

            # try:
            # print('test')
            # if (len(self.group)) == 9:
            #     print('test')
                # raise AssertionError
            # except ValueError:
            #     print("Вы не угадали :Р")

    # def magic_func(self, group):
    #     super().__init__(group)
    #
    #     if self.group == 1:
    #         raise ValueError('This is trouble! x = 1!!!')
    #     else:
    #         return [x]

    def delete_student(self, last_name):
        self.group = {x for x in self.group if last_name not in x.last_name}

    def find_student(self, last_name):
        for students in self.group:
            if last_name in students.last_name:
                return students


    def __str__(self):
        all_students = ''
        for students in self.group:
            all_students += f"{str(students)}"
        return f'Number:{self.number}\n  {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', '1')
st2 = Student('Female', 25, 'Liza', 'Taylor', '2')
st3 = Student('Male', 25, 'Ivan', 'Ivanov', '3')
st4 = Student('Male', 25, 'Petya', 'Petrov', '4')
st5 = Student('Male', 30, 'Ilya', 'Petkov', '5')
st6 = Student('Male', 25, 'Jora', 'Borsh', '6')
st7 = Student('Female', 25, 'Maryna', 'Kolko', '7')
st8 = Student('Female', 25, ',Anja', 'Krok', '8')
st9 = Student('Female', 25, 'Eugenia', 'Schmidt', '9')
st10 = Student('Female', 25, 'Lora', 'NFjugdk', '10')
st11 = Student('Female', 25, 'Inna', 'Hjdf', '11')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)
print(gr)