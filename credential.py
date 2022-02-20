import random
import string
class Credential:

    '''
         class that generates an instance of credential
     '''

    credential_list=[]

    def __init__(self,account_name,username,account_password):
        self.account_name=account_name
        self.username=username
        self.account_password=account_password

        """"
           function that defines properties of a class
        """

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

    @classmethod
    def verify_credential(cls,account_name):
         """
           method used to verify credentials
         """
         for credential in Credential.Credential_list:
             if(credential.account_name==account_name):
                 return True
                 return False
    
    @classmethod
    def find_credential(cls, account_name):
        """
        method used to find credentials using username
         """
        for credential in cls.credential_list:
            if (credential.account_name == account_name):
                return  credential

    @classmethod
    def create_credential(account_name,username,password):
        """
        method to create credentials
        """
        new_credential=Credential(account_name,username,password)
        return new_credential
    
    @classmethod
    def credential_exists(cls, account_name):
        '''
        method to check credentials existing
        '''
        for credentials in cls.credential_list:
            if credentials.account_name== account_name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns credentials
        '''
        return cls.credential_list

    def generate_password(self):
        '''
        generate random password consisting of letters
        '''
        password = string.ascii_uppercase + string.ascii_lowercase
        return ''.join(random.choice(password) for i in range(1,9))
