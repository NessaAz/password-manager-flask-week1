#!/usr/bin/env python3.10

from user import User
from credentials import Credentials
import random  #importing random module for generating password

def create_user(account_name,user_name,password,email):
    '''
    Function to create a new account
    '''
    new_user = User(account_name,user_name,password,email)
    return new_user



