import unittest  #importing the unittest module
from user import User  #importing the User class


class TestUser(unittest.TestCase):
    def setUp(self):
           
        self.new_user = User("Vanessa Az","Vanessa Azenwa","CooL99$","vanessa.azenwa@gmail.com") # create User object
        
    def test_init(self):
        '''
        test_init test case to test if the (user) object is initialized properly
        '''
        self.assertEqual(self.new_user.account_name,"Vanessa Az")
        self.assertEqual(self.new_user.user_name,"Vanessa Azenwa")
        self.assertEqual(self.new_user.password,"CooL99$")
        self.assertEqual(self.new_user.email,"vanessa.azenwa@gmail.com")    
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the (user) object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)    
        
    /    


