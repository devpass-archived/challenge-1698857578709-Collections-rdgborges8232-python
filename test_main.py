import unittest
from main import count_duplicates

class TestMain(unittest.TestCase):
    def test_count_duplicates(self):
        numbers = [1, 3, 4, 2, 5, 3, 4, 1, 1]
        self.assertEqual(count_duplicates(numbers), 4)

if __name__ == '__main__':
    unittest.main()
