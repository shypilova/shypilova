class Student():

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"{self.gender}, {self.age}, {self.first_name}, {self.last_name}, {self.record_book} \n  "

