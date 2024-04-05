class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

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