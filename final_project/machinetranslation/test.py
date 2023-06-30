import unittest
from translator import english_to_french , french_to_english

class UnitTests (unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Good Morning"),"bonne nuit")
    
class UnitTests2(unittest.TestCase):
  def test_f2e(self):
        self.assertNotEqual(french_to_english("Bonjour"),"Good morning")
        self.assertNotEqual(french_to_english("Bonjour"),"Hello")
        
        
        
unittest.main()