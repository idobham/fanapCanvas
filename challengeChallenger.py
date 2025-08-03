import unittest

from main import reverseString, mostRepeatedNum, primeChecker, mainDiameterSumCalculator, wordsSorter

class TestChallenges(unittest.TestCase):
    def testReverseString(self):
        self.assertEqual(reverseString("hello"), "olleh")
        self.assertEqual(reverseString("hello world"), "dlrow olleh")
        self.assertEqual(reverseString("challenge"), "egnellahc")

    def testMostRepeatedNum(self):
        self.assertEqual(mostRepeatedNum([1, 2, 2, 3, 3, 3, 4]),3)
        self.assertEqual(mostRepeatedNum([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]),4)

    def testPrimeChecker(self):
        self.assertFalse(primeChecker(0))
        self.assertFalse(primeChecker(1))
        self.assertTrue(primeChecker(2))
        self.assertFalse(primeChecker(4))
        self.assertTrue(primeChecker(7))
        self.assertFalse(primeChecker(15))

    def testMainDiameterSumCalculator(self):
        self.assertEqual(mainDiameterSumCalculator([[9, 8, 7], [6, 5, 4], [3, 2, 1]]),15)
        self.assertEqual(mainDiameterSumCalculator([[1, 1, 1], [2, 2, 2], [3, 3, 3]]), 6)
        self.assertEqual(mainDiameterSumCalculator([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 15)

    def testWordsSorter(self):
        self.assertEqual(wordsSorter("machine learning is fun"), "fun is learning machine")
        self.assertEqual(wordsSorter("fanap canvas"), "canvas fanap")
        self.assertEqual(wordsSorter("lubba lubba dub dub"), "dub dub lubba lubba")