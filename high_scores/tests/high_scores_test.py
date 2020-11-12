import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp (self):
        self.test_list = [1,2,5,10,20,8]
    # Test latest score (the last thing in the list)
    def test_latest(self):        
        self.assertEqual(8,latest(self.test_list))
        self.assertNotEqual(7,latest(self.test_list))
    # Test personal best (the highest score in the list)
    def test_personal_best(self):        
        self.assertEqual(20,personal_best(self.test_list))
        self.assertNotEqual(7,personal_best(self.test_list))

    # Test top three from list of scores
    def test_top_three(self):        
        self.assertEqual([20,10,8],personal_top_three(self.test_list))
        self.assertNotEqual([20,10,7],personal_top_three(self.test_list))
    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
