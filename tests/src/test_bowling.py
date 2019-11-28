import pytest
from src.bowling import bowling_score


@pytest.mark.parametrize(
    "rolls, score",
    [
        ([10 for x in range(12)], 300),
        ([9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 1], 182),
        ([9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0], 90),
        ([0 for x in range(20)], 0),
        ([10,9,1,5,3,2,8,10,7,1,2,7,5,5,1,3,10,8,1], 132),
        ([2 for x in range(20)], 40),

    ],
)
def test_bowling_score(rolls, score):
    assert bowling_score(rolls)==score

@pytest.mark.parametrize(
    "rolls",
    [
        [10 for x in range(11)],
        [10 for x in range(13)],
        # ostatni spare jeden rzut więcej VVVVV
        [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 0, 0, 1],
        # ostatni spare jeden rzut mniej VVVVV
        [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1],
        [11, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
        [9, 9, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],

    ],
)
def test_bowling_score_wrong(rolls):
    with pytest.raises(ValueError):
        bowling_score(rolls)