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

def display_user(user):
    '''
    function that displays user
    '''
    return User.display_user()

def login_user(username,password):
    '''
    a function that checks if the users already exist 
    '''
    checked_user = Credential.verify_user(username,password)
    return checked_user

def delete_user(self):

        """"
        function to check if the user is deleted
        """
        User.user_list.remove(self)
       
def create_credential(account_name,username,password):
        """
        function to create credentials
        """
        new_credential=Credential(account_name,username,password)
        return new_credential

def save_credential(self):
           """"
           function to check if the credential is saved
           """   
           Credential.credential_list.append(self)
 
def delete_credentials(self):
        '''
        delete saved credentials in the credentials list
        '''
        Credential.credential_list.remove(self)

def find_credential(cls, account_name):
        """
        function used to find credentials using username
         """
        for credential in cls.credential_list:
            if (credential.account_name == account_name):
                return  credential

def verify_credential(cls,account_name):
         """
           function used to verify credentials
         """
         for credential in Credential.Credential_list:
             if(credential.account_name==account_name):
                 return True
                 return False

# def generate_password(self):
#         '''
#         generate random password consisting of letters
#         '''
#         password = string.ascii_uppercase + string.ascii_lowercase
#         return ''.join(random.choice(password) for i in range(1,9))


def generate_password(self):
    ''' 
    function tht generates password randomly
    '''
    auto_password = Credential.generate_password(self)
    return auto_password