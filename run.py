#!/usr/bin/env python3.8
from ast import While
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
      return User.user_list.append(self)

def display_user(user):
    '''
    function that displays user
    '''
    return User.display_user()

def login_users(username,password):
    '''
    a function that checks if the users already exist 
    '''
    checked_users = Credential.login_users(username,password)
    return checked_users

def delete_user(self):

        """"
        function to check if the user is deleted
        """
        return User.user_list.remove(self)
       
def create_credentials(account_name,username,password):
        """
        function to create credentials
        """
        new_credentials=Credential(account_name,username,password)
        return new_credentials

def save_credential(self):
           """"
           function to check if the credential is saved
           """   
           return   Credential.credential_list.append(self)
 
def delete_credentials(self):
        '''
        delete saved credentials in the credentials list
        '''
        return Credential.credential_list.remove(self)

def find_credential(cls, account_name):
        """
        function used to find credentials using username
         """
    
        return Credential.find_by_username(account_name)
def verify_credential(cls,account_name):
         """
           function used to verify credentials
         """
    

         return Credential.verify_credential

def generate_password(self):
    ''' 
    function that generates password randomly
    '''
    auto_password = Credential.generate_password(self)
    return auto_password

def display_credential():
    '''
    test case that returns all saved accounts
    '''
    return Credential.display_credential()

def main():
    print('*' *30)
    print("Hello Welcome to PasswordLocker...\n To procced enter any of the following...\n cu---  To signup... \n dc-display credential..\n cc-create account...\fa-find account...\n dl-delete account...\n ex-exit account")
    print('*' *30)
    short_code = input("").lower().strip()
    if short_code == 'cu':
        print("signup")
        print('*' * 20)
        print("Username")
        username = input()
        print("password")
        password = ""
        while True:
            print("*" * 30)
            print(" TP - Type your own pasword?..\n GP - Generate from our random Password..\n")
            print("*" * 30)
            password_choice = input().strip()
            if password_choice == 'TP':
                password = input("Enter Password\n")
            elif password_choice == 'GP':
                    password = input(generate_password(password))
                    break  
          
            else:
                    print("Invalid password please try again")    

        save_user(create_user(username,password))
        print('\n')
        print(f"Hello {username}, Your account  has been created succesfully created! Your password is: {password}")
        print("-"*90)  
        while True:
            print("*" * 30)
            print("use these short codes to proceed:cu-signup...\n cc-create account..\n dc-dispaly credential..\n fc-find credential..\n dl-delete account...\n ex-exit account")
            print("*" * 30)
    elif short_code=="dc":
          print(f"Here are your credentials for account:")
          print("*" * 3)
          for credential in display_credential():
                    
                    print(f"{credential.username}{credential.password}")
                    print('\n')
                    break           
          else:
                print("You dont seem to have any accounts saved yet")
              
          while True:
            
            print("*" * 30)
            print("use these short codes to proceed:cu-signup...\n cc-create account..\n dc-dispaly credential..\n fc-find credential..\n dl-delete account...\n ex-exit account")
            print("*" * 30)
    if short_code == "cc":
            print("Create new Account")
            print("Enter account details")
            print("Account Name(example:Instagram):")
            account=input()
            print("."*5)
            print("Username ....")
            username = input()
           
            while True:
             print("*" * 30)
             print(" TP - Type your own pasword?..\n GP - Generate from our random Password..\n")
             print("*" * 30)
             password_choice = input().strip()
             if password_choice == 'TP':
                password = input("Enter Password\n")
                break
              
          
                    
            else:
                    print("Invalid password please try again")
                
            save_credential(create_credentials(account,username,password))
            print('\n')
            print(f"Account Credential for: Account{account}:Username: {username} - Password:{password} created succesfully")
            print('\n')

     
    elif short_code == "a":
            print("please enter the account you are searching example tiktok: " )
            search_credential= input()
            if find_credential(search_credential):
                search_credential = find_credential(search_credential)
                print(f"{search_credential.account_name} {search_credential.username} { search_credential.password}")
                print('-'*20)

                print(f"Account name: {search_credential.account_name}")
                print(f"Account username: {search_credential.username}")
                print(f"Account password: {search_credential.password}")
            
            else: print("This account does not exist")
    elif short_code == "dl":
            print("Enter account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*40)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("The Credential you want to delete does not exist")

    elif short_code == 'ex':
        print('Thank you for considering our service. Goodbye for now see you later!')
                # break
    else:
                print('I really didnt get that. Please use the short codes')
          
if __name__ == '__main__':
     main()