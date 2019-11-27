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
    student.name = name + "a"
    student.surname = surname + "b"
    student.id = student_id + "1"
    assert student.name == (name + "a")
    assert student.surname == (surname + "b")
    assert student.id == (student_id + "1")


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


@pytest.mark.parametrize("marks", [[2, 3], [3, 3.5, 4, 4.5, 5]])
def test_student_add_mark(marks):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    # when
    for mark in marks:
        student.add_mark(mark)
    # then
    for mark in marks:
        assert mark in student.marks


@pytest.mark.parametrize("mark", [-2, 1, 1.5, 2.25, 3.01, 5.5, 6])
def test_student_add_mark_wrong(mark):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    student.add_mark(3)
    student.add_mark(4)
    # then
    with pytest.raises(ValueError):
        # when
        student.add_mark(mark)


@pytest.mark.parametrize(
    "mark_id, mark", [(0, 2), (1, 3), (2, 3), (1, 3.5), (0, 4), (1, 4.5), (2, 5)]
)
def test_student_edit_mark(mark_id, mark):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    student.add_mark(3)
    student.add_mark(2)
    student.add_mark(2)
    # when
    student.edit_mark(mark_id, mark)
    # then
    assert mark == student.marks[mark_id]


@pytest.mark.parametrize(
    "mark_id, mark",
    [(-1, 2), (3, 3), (4, 3), (-2, 3.5), (0, 4.25), (1, 2.75), (2, 5.5)],
)
def test_student_edit_mark_wrong(mark_id, mark):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    student.add_mark(3)
    student.add_mark(2)
    student.add_mark(2)
    # then
    with pytest.raises(ValueError):
        # when
        student.edit_mark(mark_id, mark)


@pytest.mark.parametrize("mark_id", [0, 1, 2])
def test_student_delete_mark(mark_id):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    student.add_mark(2)
    student.add_mark(3)
    student.add_mark(4)
    tmp_marks = student.marks.copy()
    # when
    student.delete_mark(mark_id)
    # then
    assert tmp_marks[mark_id] not in student.marks
    assert len(student.marks) == 2


@pytest.mark.parametrize("mark_id", [-1, 3, 4])
def test_student_delete_mark_wrong(mark_id):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    student.add_mark(2)
    student.add_mark(3)
    student.add_mark(4)
    # then
    with pytest.raises(ValueError):
        # when
        student.delete_mark(mark_id)


@pytest.mark.parametrize(
    "marks, mean",
    [([2, 3, 4], 3), ([3, 3, 3], 3), ([2, 3.5, 3.5], 3), ([5, 4.5, 5], 4.83), ([2], 2)],
)
def test_student_mean(marks, mean):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    for mark in marks:
        student.add_mark(mark)
    # when
    stud_mean = student.mean
    # then
    assert stud_mean == mean

@pytest.mark.parametrize("dates", [["27.11.2019", "28.11.2019"], ["03.01.2020"]])
def test_student_add_meet(dates):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    for date in dates:
        # when
        student.add_meet(date)
    # then
    assert dates is len(student.meets)

@pytest.mark.parametrize("date", ["32.11.2019", "28.13.2019", "03-01-2020"])
def test_student_add_meet_wrong(date):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    # then
    with pytest.raises(ValueError):
        # when
        student.add_meet(date)

@pytest.mark.parametrize("presence", ["O", "S", "N", "U"])
def test_student_set_presence(presence):
    # given
    date = "28.11.2019"
    student = Student("Qwerty", "Azerty", "000001")
    student.add_meet(date)
    # when
    student.set_presence(date, presence)
    # then
    assert presence == student.meets(date)

@pytest.mark.parametrize("presence", ["X", "o", "/", "s"])
def test_student_set_presence_wrong(presence):
    # given
    date = "28.11.2019"
    student = Student("Qwerty", "Azerty", "000001")
    student.add_meet(date)
    # then
    with pytest.raises(ValueError):
        # when
        student.set_presence(date, presence)


@pytest.mark.parametrize("presence", ["O", "S", "N", "U"])
def test_student_edit_presence(presence):
    # given
    date = "28.11.2019"
    student = Student("Qwerty", "Azerty", "000001")
    student.add_meet(date)
    student.set_presence(date, "O")
    # when
    student.set_presence(date, presence)
    # then
    assert presence == student.meets(date)

@pytest.mark.parametrize("presence", ["X", "o", "/", "s"])
def test_student_edit_presence_wrong(presence):
    # given
    date = "28.11.2019"
    student = Student("Qwerty", "Azerty", "000001")
    student.add_meet(date)
    student.set_presence(date, "O")
    # then
    with pytest.raises(ValueError):
        # when
        student.set_presence(date, presence)

@pytest.mark.parametrize("date,presence,no_a", [("28.11.2019","O",0), ("27.11.2019","N",1)])
def test_student_number_absent(date, presence, no_a):
    # given
    student = Student("Qwerty", "Azerty", "000001")
    student.add_meet(date)
    student.set_presence(date, presence)
    # when
    tmp_num=student.number_absent
    # then
    assert tmp_num==no_a

def test_student_get_json():
    student = Student("Qwerty", "Azerty", "000001")
    student.add_meet(date)
    student.set_presence(date, presence)


def test_student_set_json():
    pass

