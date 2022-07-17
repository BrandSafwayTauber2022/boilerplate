from __future__ import annotations

from basic_math import add_two_numbers


class TestSampleAddition:
    def test_add_two_different_numbers(self):
        # variable to test
        sum = add_two_numbers(2, 3)

        # defined answer
        answer = 5

        # assert statement to compare the two
        assert sum == answer

    def test_add_negative_numbers(self):
        sum = add_two_numbers(-2, -3)
        answer = -5
        assert sum == answer
