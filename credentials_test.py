#!usr/bin/env python3.8
import unittest
import pyperclip
from credentials import Credentials

class TestUser(unittest.TestCase):
   def setUp(self):
       """
         Test class that defines test cases for the credentials class behaviours.
        """
   
   
       self.new_credentials = Credentials("Talia","12345") 
      
   def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Talia")
        self.assertEqual(self.new_user.password,"12345")