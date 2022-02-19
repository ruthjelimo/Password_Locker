#!usr/bin/env python3.8
import unittest
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):
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
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


   def tearDown(self):
          '''
            tearDown method that does clean up after each test case has run.
            '''
          Credentials.credentials_list =[]   
  
   def test_save_multiple_credentials(self):
         '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
         self.new_credentials.save_credentials()
         test_credentials = Credentials("mimo","twin")
         test_credentials.save_credentials()
         self.assertEqual(len(Credentials.credential_list),2)
   
   def  test_delete_credentials(self):
          '''
            test_delete_credentials to test if we can remove credentials from our credentials list
            '''
          self.new_credentials.save_credentials()
          test_credentials = Credentials("Talia","1234")
          test_credentials.save_credentials()
          self.new_credentials.delete_credentials()
          self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()