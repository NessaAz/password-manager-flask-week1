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
        
    def save_user(self):
    
        '''
        save_user is the method to save user objects into the user list
        '''

        User.user_list.append(self)
    
    def delete_user(self):
    
        '''
        delete_user is the method to delete a saved user from the user_list
        '''

        User.user_list.remove(self)
        
        
    @classmethod
    def user_exist(cls,name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            name: User name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.password == name:   #why not highlighting password
                    return user

        return False
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the user account list
        '''
        return cls.user_list