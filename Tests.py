import unittest, time

from Questions import Question, TimeQuestion
from Answers import Answer

class TestQuestions (unittest.TestCase):

    def setUp (self):
        pass

    def testQA (self):
        self.assertEqual (Question ().computeAnswer ().__class__,
                          Answer)

    def testTime (self):
        time1 = time.time ()
        time2 = TimeQuestion ().computeAnswer ().time
        self.assertEqual (time1, time2)

    def tearDown (self):
        pass
    
if __name__ == '__main__':
    unittest.main (exit=False)
    
