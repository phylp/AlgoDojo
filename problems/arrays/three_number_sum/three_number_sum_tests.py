import sys
import solution
import unittest

class TestProgram(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(solution.three_number_sum([1, 2, 3], 6), [[1, 2, 3]])
    def testcase2(self):
        self.assertEqual(solution.three_number_sum([1, 2, 3], 7), [])
    def testcase3(self):
            self.assertEqual(solution.three_number_sum([8, 10, -2, 49, 14], 57), [[-2, 10, 49]])
    def testcase4(self):
            self.assertEqual(solution.three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]] )
    def testcase5(self):
            self.assertEqual(solution.three_number_sum([12, 3, 1, 2, -6, 5, 0, -8, -1], 0), [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]] )
    def testcase6(self):
            self.assertEqual(solution.three_number_sum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-1, 0, 1]] )
    def testcase7(self):
            self.assertEqual(solution.three_number_sum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0),
            [
                [-8, 2, 6],
                [-8, 3, 5],
                [-6, 0, 6],
                [-6, 1, 5],
                [-5, -1, 6],
                [-5, 0, 5],
                [-5, 2, 3],
                [-1, 0, 1],
            ]
        )
    def testcase8(self):
            self.assertEqual(solution.three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32), [[8, 9, 15]])
    def testcase9(self):
            self.assertEqual(solution.three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33), [])
    def testcase10(self):
            self.assertEqual(solution.three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 5), [])



if __name__ == "__main__":
	unittest.main()
