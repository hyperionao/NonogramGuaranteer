import unittest
from nonogram_guarantee import calculate_blanks, process_input, nonogram_logic

class TestNonogramLogic(unittest.TestCase):
    def test_calculate_blanks(self):
        self.assertEqual(calculate_blanks(10, [3, 2]), 4)

    def test_process_input_valid(self):
        self.assertEqual(process_input("10", "3 2"), (10, [3, 2]))

    def test_nonogram_logic(self):
        result = nonogram_logic(10, [3, 2])
        self.assertIn("guaranteed slots found", result)

if __name__ == "__main__":
    unittest.main()
