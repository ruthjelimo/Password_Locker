#!usr/bin/env python3.8
import unittest
from users import User

class TestUser(unittest.TestCase):
   def setUp(self):
     self.new_user = User("jelimo","12345") 

   
   def test_init(self):

        self.assertEqual(self.new_user.username,"jelimo")
        self.assertEqual(self.new_user.password,"12345")

   def test_save_user(self):
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

   def tearDown(self):
       User.user_list =[]

   def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("ruth","45678")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
   
   def  test_delete_user(self):
         self.new_user.save_user()
         test_user = User("ruth","45678")
         test_user.save_user()
         self.new_user.delete_user()
         self.assertEqual(len(User.user_list),1)



   def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("ruth", "45678")
        test_user.save_user()
        found_user = User.find_user("jelimo")
        self.assertEqual(found_user.username, self.new_user.username)


if __name__ == '__main__':
    unittest.main()