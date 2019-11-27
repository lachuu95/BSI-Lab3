from typing import List


class Student:
    def __init__(self, name: str, surname: str, id: str):
        self.__name = self.__validate_str(name)
        self.__surname = self.__validate_str(surname)
        self.__id = self.__validate_num(id)
        self.__marks = []

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

    def add_mark(self, mark: float) -> None:
        self.__marks.append(self.__validate_mark(mark))

    def edit_mark(self, mark_id: int, mark: float) -> None:
        self.__marks[self.__validate_mark_id(mark_id)] = self.__validate_mark(mark)

    def delete_mark(self, mark_id: int) -> None:
        del self.__marks[self.__validate_mark_id(mark_id)]

    @property
    def mean(self) -> float:
        return round(sum(self.__marks)/len(self.__marks), 2)

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

    @name.setter
    def name(self, value: str) -> None:
        self.__name = self.__validate_str(value)

    @surname.setter
    def surname(self, value: str) -> None:
        self.__surname = self.__validate_str(value)

    @id.setter
    def id(self, value: str) -> None:
        self.__id = self.__validate_num(value)
