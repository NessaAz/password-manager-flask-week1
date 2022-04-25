class Credentials:
    '''
    class that generates new instance of user credentials
    '''
    
    credentials_list = [] #empty credentials list
    
    def __init__(self,credentials_name,account_name,password,email):
        self.credentials_name = credentials_name
        self.account_name = account_name
        self.password = password
        self.email = email
        
        