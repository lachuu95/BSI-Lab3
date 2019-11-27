import pytest
import os
from src.group import Group


def test_group():
    # when
    group = Group()
    # then
    assert len(group.students) == 0


@pytest.mark.parametrize(
    "name, surname, student_id",
    [
        ("Qwerty", "Azerty", "000001"),
        ("Asdfgh", "Zxcvbn", "000002"),
        ("Qazwsx", "Edcrfv", "000003"),
    ],
)
def test_add_student(name, surname, student_id):
    # given
    group = Group()
    # when
    group.add_student(name, surname, student_id)
    # then
    assert group.students[0].id == student_id

def test_add_student_wrong():
    # given
    group = Group()
    group.add_student("Qwerty", "Azerty", "000001")
    # then
    with pytest.raises(ValueError):
        # when
        group.add_student("Qwerty", "Azerty", "000001")

@pytest.mark.parametrize(
    "name, surname, student_id",
    [
        ("Qwerty", "Azerty", "000001"),
        ("Asdfgh", "Zxcvbn", "000002"),
        ("Qazwsx", "Edcrfv", "000003"),
    ],
)
def test_delete_student(name, surname, student_id):
    # given
    group = Group()
    group.add_student(name, surname, student_id)
    # when
    group.delete_student(student_id)
    # then
    assert len(group.students) == 0

def test_delete_student_wrong():
    # given
    group = Group()
    # then
    with pytest.raises(ValueError):
        # when
        group.delete_student("000001")


def test_add_meet():
    # given
    group = Group()
    stud = [
        ("Qwerty", "Azerty", "000001"),
        ("Asdfgh", "Zxcvbn", "000002"),
        ("Qazwsx", "Edcrfv", "000003"),
    ]
    for name, surname, student_id in stud:
        group.add_student(name, surname, student_id)
    # when
    group.add_meet("28.11.2019")
    # then
    for idx, _ in enumerate(stud):
        print(group.students)
        assert "28.11.2019" in group.students[idx].meets.keys()


def test_save(tmp_path):
    # given
    group = Group()
    stud = [
        ("Qwerty", "Azerty", "000001"),
        ("Asdfgh", "Zxcvbn", "000002"),
        ("Qazwsx", "Edcrfv", "000003"),
    ]
    for name, surname, student_id in stud:
        group.add_student(name, surname, student_id)
    # when
    group.save(os.path.join(tmp_path, "test"))
    # then
    os.path.isfile(os.path.join(tmp_path, "test.txt"))


def test_read(tmp_path):
    # given
    group = Group()
    stud = [
        ("Qwerty", "Azerty", "000001"),
        ("Asdfgh", "Zxcvbn", "000002"),
        ("Qazwsx", "Edcrfv", "000003"),
    ]
    for name, surname, student_id in stud:
        group.add_student(name, surname, student_id)
    group.save(os.path.join(tmp_path, "test"))
    group2 = Group()
    # when
    group2.read(os.path.join(tmp_path, "test"))
    # then
    assert len(group2.students) == 3
