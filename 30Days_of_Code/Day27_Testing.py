# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 27

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

import random

class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        return list()

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        global Unique_Values
        length = random.randint(1, 10)
        Unique_Values = random.sample(range(1, 101), length)
        return Unique_Values

    @staticmethod
    def get_expected_result():
        global Unique_Values
        return Unique_Values.index(min(Unique_Values))

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        global Double_minimum
        length = random.randint(1, 10)
        Double_minimum = random.sample(range(1, 101), length)
        Double_minimum.append(min(Double_minimum))
        return Double_minimum

    @staticmethod
    def get_expected_result():
        global Double_minimum
        return Double_minimum.index(min(Double_minimum))


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
