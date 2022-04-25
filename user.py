class User:
    '''
    class that generates new instance of a user
    '''
    
    user_list = []  #empty user's list
    
    def __init__(self,account_name,user_name,password,email):
        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email
    