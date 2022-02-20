#!/usr/bin/envi python3.8
import pyperclip
from users import User
from credential import Credential
def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user
def save_user(self):
      """"
      function to check if the user is saved
      """
      User.user_list.append(self)
    