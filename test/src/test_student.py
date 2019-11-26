import pytest
from src.student import Student


@pytest.mark.parametrize(
    "name, surname, student_id",
    [
        ("Qwerty", "Azerty", "000001"),
        ("Asdfgh", "Zxcvbn", "000002"),
        ("Qazwsx", "Edcrfv", "000003"),
    ],
)
def test_student_init(name, surname, student_id):
    student = Student(name, surname, student_id)
    assert student.name is name
    assert student.surname is surname
    assert student.id is student_id


@pytest.mark.parametrize(
    "name, surname, student_id",
    [
        ("awerty", "azerty", "000001"),
        ("213546", ",./;l=", "000002"),
        ("Qazwsx", "Edcrfv", "/';.][]"),
    ],
)
def test_student_init_wrong(name, surname, student_id):
    with pytest.raises(ValueError):
        Student(name, surname, student_id)

@pytest.mark.parametrize(
    "name, surname, student_id",
    [
        ("Qwerty", "Azerty", "000001"),
        ("Asdfgh", "Zxcvbn", "000002"),
        ("Qazwsx", "Edcrfv", "000003"),
    ],
)
def test_student_edit(name, surname, student_id):
    student = Student(name, surname, student_id)
    student.name = name+"a"
    student.surname = surname+"b"
    student.id = student_id+"1"
    assert student.name == (name+"a")
    assert student.surname == (surname+"b")
    assert student.id == (student_id+"1")

@pytest.mark.parametrize(
    "name, surname, student_id",
    [
        ("awerty", "azerty", "000001"),
        ("213546", ",./;l=", "000002"),
        ("Qazwsx", "Edcrfv", "/';.][]"),
    ],
)
def test_student_edit_wrong(name, surname, student_id):
    student = Student("Qwerty", "Azerty", "000001")
    with pytest.raises(ValueError):
        student.name = name
        student.surname = surname
        student.id = student_id

def test_student_add_mark():

def test_student_edit_mark():

def test_student_mean():

def test_student_add_meet():

def test_student_set_presence():

def test_student_edit_presence():







