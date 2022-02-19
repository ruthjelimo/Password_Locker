class Credentials:
     '''
    class that generates an instance of credentials
    '''

     credentials_list=[]

def __init__(self,username,password):
      """"
    function that defines properties of a class
    """
      self.username = username
      self.password = password

def save_credentials(self):
      """"
    function to check if the user is saved
    """
      Credentials.credentials_list.append(self)

def delete_credentials(self):
      """"
        function to check if the credentials is deleted
      """     

      Credentials.credentials_list.remove(self)
      
@classmethod
def find_username(cls, credentials):
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return  credentials
