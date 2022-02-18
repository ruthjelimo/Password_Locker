#!usr/bin/env python3.8
import unittest
from users import User

class TestUser(unittest.TestCase):
   def setUp(self):
     self.new_user = User("jelimo","12345") 

   
   def test_init(self):

        self.assertEqual(self.new_user.username,"jelimo")
        self.assertEqual(self.new_user.password,"12345")






if __name__ == '__main__':
    unittest.main()