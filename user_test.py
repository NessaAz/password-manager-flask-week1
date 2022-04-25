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
        
    def tearDown(self):
            '''
            tearDown method does clean up after each test case has run.
            '''
            User.user_list = []    
            
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","55667788","test@user.com") # a new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","55667788","test@user.com") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)
        
    def test_find_user_by_user_name(self):
        '''
        test to check if we can find a user by a user_name and display user information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","55667788","test@user.com") 
        test_user.save_user()

        found_user = User.find_by_account_name("Test")

        self.assertEqual(found_user.email,test_user.email)      
        
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","55667788","test@user.com")
        test_user.save_user()

        user_exists = User.user_exist("55667788")

        self.assertTrue(user_exists)      

    def test_display_all_users(self):
        '''
        method that returns a list of all user-accounts saved
        '''
        displayed = User.display_users()
        self.assertEqual(displayed,User.user_list)

