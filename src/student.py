class Student:
    def __init__(self, name: str, surname: str, id: str):
        self.__name = self.__validate_str(name)
        self.__surname = self.__validate_str(surname)
        self.__id = self.__validate_num(id)
        self.__marks = []

    def __validate_str(self, content: str) -> str:
        if not content.isalpha():
            raise ValueError("no xd ja tu chce literki a nie coś innego")
        if not content[0].isupper():
            raise ValueError("nazwy powinny zaczynać Wielką literą")
        return content

    def __validate_num(self, content: str) -> str:
        if not content.isdigit():
            raise ValueError("no gdzie mnie tu z literkami chcę cyferki")
        return content

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def surname(self) -> str:
        return self.__surname

    @property
    def id(self) -> str:
        return self.__id

    @name.setter
    def name(self, value:str) -> None:
        self.__name = self.__validate_str(value)

    @surname.setter
    def surname(self, value:str) -> None:
        self.__surname = self.__validate_str(value)

    @id.setter
    def id(self, value:str) -> None:
        self.__id = self.__validate_num(value)   


