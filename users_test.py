#!usr/bin/env python3.8
import unittest
import pyperclip
from users import User

class TestUser(unittest.TestCase):
   def setUp(self):
       """
         Test class that defines test cases for the user class behaviours.
        """
   
   
       self.new_user = User("jelimo","12345") 
   
   def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"jelimo")
        self.assertEqual(self.new_user.password,"12345")
    
   def test_save_user(self):
        '''
         test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

   def tearDown(self):
          '''
            tearDown method that does clean up after each test case has run.
            '''
          User.user_list =[]

   def test_save_multiple_users(self):
         '''
            test_save_multiple_users to check if we can save multiple users
            objects to our user_list
            '''
         self.new_user.save_user()
         test_user = User("ruth","45678")
         test_user.save_user()
         self.assertEqual(len(User.user_list),2)
   
   def  test_delete_user(self):
          '''
            test_delete_user to test if we can remove a user from our user list
            '''
          self.new_user.save_user()
          test_user = User("ruth","45678")
          test_user.save_user()
          self.new_user.delete_user()
          self.assertEqual(len(User.user_list),1)

   def test_find_user(self):
        '''
        find a user using username and display information
        '''
        self.new_user.save_user()
        test_user = User("ruth", "45678")
        test_user.save_user()
        found_user = User.find_user("jelimo")
        self.assertEqual(found_user.username, self.new_user.username)


if __name__ == '__main__':
    unittest.main()