import unittest #importing the unittest module
from credentials import Credentials #importing the credentials class


class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("Vanessa Aze","Vanessa Azen","CoL99$","vanessamwikali@gmail.com") # create Credentials object
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credentials_name,"Vanessa Aze")
        self.assertEqual(self.new_credentials.credaccount_name,"Vanessa Azen")
        self.assertEqual(self.new_credentials.password,"CoL99$")
        self.assertEqual(self.new_credentials.email,"vanessamwikali@gmail.com")
    
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)  
        
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []    
            
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple user credentials
            objects to our account_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test1","user1","66778899","test1@user.com") # new user
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)  
            
    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove credentials from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test1","user1","66778899","test1@user.com") 
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting an account object
            self.assertEqual(len(Credentials.credentials_list),1)              
    
    def test_find_credentials_by_credentials_name(self):
        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test1","user1","66778899","test1@user.com") 
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_name("Test")

        #self.assertEqual(found_credentials.email,test_credentials.email)
        
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test1","user1","66778899","test1@user.com") 
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("66778899")
        self.assertTrue(credentials_exists)  
    

if __name__ == '__main__':
    unittest.main()    