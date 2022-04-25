import imp


import unittest #importing the unittest module
from credentials import Credentials #importing the credentials class


class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("Vanessa","Azenwa","CooL99$","vanessa.azenwa@gmail.com") # create Cresentials object
        

