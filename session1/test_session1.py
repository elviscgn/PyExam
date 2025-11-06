import unittest
from io import StringIO
import sys

from question_1 import fizzbuzz
from question_2 import pattern
from question_3 import word_frequency
from question_4 import analyze

class TestSession1(unittest.TestCase):

    # --------------------------
    # Q1 – FizzBuzz Tests
    # --------------------------
    def test_fizzbuzz_basic(self):
        self.assertEqual(fizzbuzz(6), ["1", "2", "Fizz", "4", "Buzz", "Fizz"])
        self.assertEqual(fizzbuzz(15), ["1","2","Fizz","4","Buzz","Fizz",
                                        "7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])

    # --------------------------
    # Q2 – Pattern Printing Tests
    # --------------------------
    def test_pattern_right(self):
        captured = StringIO()
        sys.stdout = captured
        pattern(3, "right")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue().strip(), "*\n**\n***")

    def test_pattern_inverted(self):
        captured = StringIO()
        sys.stdout = captured
        pattern(3, "inverted")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue().strip(), "***\n**\n*")

    def test_pattern_pyramid(self):
        captured = StringIO()
        sys.stdout = captured
        pattern(3, "pyramid")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue().strip(), "  *\n ***\n*****")

    # --------------------------
    # Q3 – Word Frequency Tests
    # --------------------------
    def test_word_frequency(self):
        self.assertEqual(word_frequency("Hello hello world!"), {"hello": 2, "world": 1})
        self.assertEqual(word_frequency("Python is fun. Python is easy."),
                         {"python": 2, "is": 2, "fun": 1, "easy": 1})

    # --------------------------
    # Q4 – List Analyzer Tests
    # --------------------------
    def test_analyze(self):
        result = analyze([5, 3, 2, 5, 1, 3])
        self.assertEqual(result["unique_sorted"], [1, 2, 3, 5])
        self.assertEqual(result["sum"], 19)
        self.assertAlmostEqual(result["average"], 3.1666666666666665)
        self.assertEqual(result["max"], 5)
        self.assertEqual(result["min"], 1)

if __name__ == "__main__":
    unittest.main()
