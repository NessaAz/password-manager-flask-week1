import unittest  #importing the unittest module
from user import User  #importing the User class


class TestUser(unittest.TestCase):
    def setUp(self):
           
        self.new_user = User("Vanessa","Azenwa","CooL99$","vanessa.azenwa@gmail.com") # create User object



