import unittest #importing the unittest module
from credentials import Credentials #importing the credentials class


class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("Vanessa","Azenwa","CooL99$","vanessa.azenwa@gmail.com") # create Cresentials object
        
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
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test1","user1","66778899","test1@user.com") # new user
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)        
    
    

