import unittest
from logger import Logger

class target(object):
    def set_text(self, text):
        self.string = text
    
    def get_text(self):
        return self.string

  
text = "Some Text"
class LoggerTest(unittest.TestCase):
    '''unit tests for the logger functions'''
    
    def test_logger_info(self):
        t = target()
        log = Logger(t.set_text(text))
        
        log.info(text)
        
        self.assertEqual(t.get_text(), "[INFO] Some Text")
        
    def test_logger_error(self):
        t = target()
        log = Logger(t.set_text(text))
        
        log.error(text)
        
        self.assertEqual(t.get_text(), "[INFO] Some Text")


if __name__ == '__main__':
    unittest.main()
    
