from src.student import Student
import json


class Group:
    def __init__(self):
        self.__students = []

    @property
    def students(self):
        return [x for x in self.__students]

    def add_student(self, name: str, surname: str, student_id: str) -> None:
        if student_id not in [x.id for x in self.__students]:
            self.__students.append(Student(name, surname, student_id))
        else:
            raise ValueError("nie wolno dodać dwóch takich samych studentów")

    def delete_student(self, student_id: str) -> None:
        id_dict = {x.id: idx for idx, x in enumerate(self.__students)}
        if student_id in id_dict:
            del self.__students[id_dict[student_id]]
        else:
            raise ValueError("nie wolno usuwac nieistniejących studentów")

    def add_meet(self, date: str) -> None:
        for student in self.__students:
            student.add_meet(date)

    def save(self, file_name: str) -> None:
        data = {idx: x.make_json() for idx, x in enumerate(self.__students)}
        with open(f"{file_name}.txt", "w") as outfile:
            json.dump(data, outfile)

    def read(self, file_name: str) -> None:
        with open(f"{file_name}.txt") as json_file:
            data = json.load(json_file)
        for key, student in data.items():
            self.add_student(student["name"], student["surname"], student["id"])
            for mark in student["marks"]:
                self.__students[key].add_mark(mark)
            for date, presence in student["meets"].items():
                self.__students[key].add_meet(date)
                self.__students[key].set_presence(date, presence)

