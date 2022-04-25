import unittest #importing the unittest module
from credentials import Credentials #importing the credentials class


class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("Vanessa","Azenwa","CooL99$","vanessa.azenwa@gmail.com") # create Cresentials object
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credentials_name,"Vanessa Az")
        self.assertEqual(self.new_credentials.account_name,"Vanessa Azenwa")
        self.assertEqual(self.new_credentials.password,"CooL99$")
        self.assertEqual(self.new_credentials.email,"vanessa.azenwa@gmail.com")
    
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the account object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)  
    

