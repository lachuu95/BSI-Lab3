from datetime import datetime
from typing import List, Dict


class Student:
    def __init__(self, name: str, surname: str, id: str):
        self.__name = self.__validate_str(name)
        self.__surname = self.__validate_str(surname)
        self.__id = self.__validate_num(id)
        self.__marks = []
        self.__meets = {}

    def __validate_str(self, content: str) -> str:
        if not content.isalpha():
            raise ValueError("no xd ja tu chce literki a nie coś innego")
        elif not content[0].isupper():
            raise ValueError("nazwy powinny zaczynać Wielką Literą")
        else:
            return content

    def __validate_num(self, content: str) -> str:
        if not content.isdigit():
            raise ValueError("no gdzie mnie tu z literkami chcę cyferki jako stringi")
        else:
            return content

    def __validate_mark(self, mark: float) -> float:
        if mark in [2, 3, 3.5, 4, 4.5, 5]:
            return mark
        else:
            raise ValueError("przyjmuję tylko studenckie oceny")

    def __validate_mark_id(self, mark_id: int) -> int:
        if len(self.__marks) != 0 and mark_id >= 0 and mark_id < len(self.__marks):
            return mark_id
        else:
            raise ValueError("bardzo doby pomysł wybierać oceny któwych niema")

    def __validate_date(self, date: str) -> str:
        try:
            datetime.strptime(date, "%d.%m.%Y")
            return date
        except ValueError:
            raise ValueError("chce date w formacie DD.MM.YYYY")

    def __validate_meet(self, date: str) -> str:
        if date in self.__meets:
            return self.__validate_date(date)
        else:
            raise ValueError("brak daty w spotkaniach")

    def __validate_presence(self, char: str) -> str:
        if char in ["O", "S", "N", "U"]:
            return char
        else:
            raise ValueError("przyjmuję tylko literki O,S,N,U")

    @property
    def number_absent(self) -> int:
        return sum(x == "N" for x in self.__meets.values())

    @property
    def mean(self) -> float:
        return round(sum(self.__marks) / len(self.__marks), 2)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def surname(self) -> str:
        return self.__surname

    @property
    def id(self) -> str:
        return self.__id

    @property
    def marks(self) -> List[float]:
        return self.__marks

    @property
    def meets(self) -> Dict[str, str]:
        return self.__meets

    @name.setter
    def name(self, value: str) -> None:
        self.__name = self.__validate_str(value)

    @surname.setter
    def surname(self, value: str) -> None:
        self.__surname = self.__validate_str(value)

    @id.setter
    def id(self, value: str) -> None:
        self.__id = self.__validate_num(value)

    def add_mark(self, mark: float) -> None:
        self.__marks.append(self.__validate_mark(mark))

    def edit_mark(self, mark_id: int, mark: float) -> None:
        self.__marks[self.__validate_mark_id(mark_id)] = self.__validate_mark(mark)

    def delete_mark(self, mark_id: int) -> None:
        del self.__marks[self.__validate_mark_id(mark_id)]

    def add_meet(self, date: str) -> None:
        self.__meets[self.__validate_date(date)] = None

    def set_presence(self, date: str, char: str) -> None:
        self.__meets[self.__validate_meet(date)] = self.__validate_presence(char)

    def make_json(self) -> Dict[str, str]:
        stud_dict = {}
        stud_dict["name"] = self.__name
        stud_dict["surname"] = self.__surname
        stud_dict["id"] = self.__id
        stud_dict["marks"] = self.__marks
        stud_dict["meets"] = self.__meets
        return stud_dict
