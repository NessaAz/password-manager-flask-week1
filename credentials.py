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
        
    def save_credentials(self):
    
        '''
        save_credentials is the method that saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)    

    def delete_credentials(self):
    
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)   

    @classmethod
    def find_by_name(cls,name):
        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                return credentials