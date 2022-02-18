class User:
    user_list=[]
   
    def __init__(self,username,password):
        self.username=username
        self.password=password
    
    #create account
    def save_account(self):
        User.user_list.append(self)
    def view_account(self):
        User.user_list.view(self)
