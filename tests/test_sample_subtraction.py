from basic_math import subtract_two_numbers

class TestSampleSubtraction:

    def test_subtract_two_postive_numbers(self):
        difference = subtract_two_numbers(6,2)

        answer = 4

        assert difference == answer