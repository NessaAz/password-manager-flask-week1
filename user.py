class User:
    '''
    class that generates new instance of a user
    '''
    
    user_list = []  #empty user's list
    
    def __init__(self,user_name,user_name,password,email):
        self.account_name = user_name
        self.user_name = user_name
        self.password = password
        self.email = email
        
    def save_user(self):
    
        '''
        save_user is the method to save user objects into the user list
        '''

        User.user_list.append(self)
    
    