
class Person:
    __firstname = str()
    __lastname = str()
    __phone = str()
    __person_type = None

    def __init__(self, firstname: str, lastname: str, phone: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone

    def set_firstname_godmode(self, firstname: str):
        self.__firstname = firstname

    def __str__(self):
        return f'{self.__firstname} {self.__lastname} {self.__phone}'

    def to_file(self, filename: str):
        with open(filename, 'a') as file:
            file.write(self.__str__() + '\n')


class Student(Person):
    __group = str()

    def __init__(self, firstname: str, lastname: str, phone: str, group: str):
        super().__init__(firstname, lastname, phone)
        self.set_group(group)

    def get_group(self):
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def __str__(self):
        return f'{super().__str__()} {self.__group}'

    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_group(res[3])


class Teacher(Person):
    __subject = str()

    def __init__(self, firstname: str, lastname: str, phone: str, subject: str):
        super().__init__(firstname, lastname, phone)
        self.set_subject(subject)

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def __str__(self):
        return f'{super().__str__()} {self.__subject}'

    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_subject(res[3])



li = []
li.append(Student('Ivasyk', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
li.append(Student('Grigoiy', 'Terkin', '+387415874165', 'Python21'))
li.append(Student('Anna', 'Chechetkina', '+04478451235', 'C++14'))
li.append(Student('Svetlana', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
li.append(Student('Anatloiy', 'Fedorov', '0991234756', 'C++17'))
li.append(Teacher('Evgeniy', 'Samsonov', '0632586477', 'Python11'))
li.append(Teacher('Ludmila', 'Traser', '0500003325', 'C++17'))

for i in li:
    i.to_file('test.txt')

class Group:
    __name = str()
    __li = list()

    def __init__(self, name: str):
        self.set_name(name)

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def append(self, person: Person):
        self.__li.append(person)

    def li_from_file(self, filename: str = 'test.txt'):
        with open(filename, 'r') as file:
            persons = file.readlines()
            for person in persons:
                person = person.split()
                if person[0] == 'student':
                    self.__li.append(Student(person[1], person[2], person[3], person[4]))
                if person[0] == 'teacher':
                    self.__li.append(Teacher(person[1], person[2], person[3], person[4]))

for i in li:
     print(i)

li[0].to_file('test.txt')

li[0].from_file('test.txt')

import json

student_li = {
    'firstname': 'Ivasyk',
    'lastname': 'Bulkin',
    'phone': '657464646',
    'group': 'Python11',
}
teacher_li = {
    'firstname': 'Ludmila',
    'lastname': 'Traser',
    'phone': '0500003325',
    'subject': 'C++17',
}
group = {
    'Student': student_li,
    'Teacher': teacher_li,
}
json_string = json.dumps(group)
print(json_string)

with open('data_file.txt', 'w', encoding='utf-8') as fl:
    json.dump(group, fl, ensure_ascii=False)

with open('data_file.txt', 'r', encoding='utf-8') as fl:
    des = json.load(fl)
    print(des)