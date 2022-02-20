class User:
    '''
    class that generates an instance of user
    '''
    user_list=[]
   
    def __init__(self,username,password):
        self.username=username
        self.password=password
    """"
    function that defines properties of a class
    """
    
    def save_user(self):
        User.user_list.append(self)
    """"
    function to check if the user is saved
    """
    def delete_user(self):
        User.user_list.remove(self)
    """"
    function to check if the user is deleted
    """
    @classmethod
    def find_user(cls, username):
        for user in cls.user_list:
            if user.username == username:
                return  user

    @classmethod
    def display_user(cls):
        return cls.user_list
