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

    
   def test_save_credentials(self):
        '''
         test_save_credentials test case to test if the credential object is saved into
         the  list
        '''
        self.new_user.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
