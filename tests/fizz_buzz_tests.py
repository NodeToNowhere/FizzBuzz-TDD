import unittest
from src.fizz_buzz import *


class TestFizzBuzz(unittest.TestCase):

    # divisible by 3 "fizz"
    def test_is_divisible_by_3(self):
        expected = "Fizz"
        actual = fizz(3)
        self.assertEqual(expected, actual)

    # # is divisible by 5 "buzz"

    def test_is_divisible_by_5(self):
        expected = "Buzz"
        actual = fizz(5)
        self.assertEqual(expected, actual)

    # # is divisible by 3 and 5 "fizzbuzz"

    def test_is_divisible_by_3_and_5(self):
        expected = "FizzBuzz"
        actual = fizz(15)
        self.assertEqual(expected, actual)

    # # else return as string eg: "7"
    def test_not_divisible_by_anything(self):
        expected = "11"
        actual = fizz(11)
        self.assertEqual(expected, actual)
