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

def save_users(user):
    '''
    Function to save users
    '''
    user.save_user()    

def del_user(user):
    '''
    Function to delete a user account
    '''
    user.delete_user()  
    
def find_user(name):
    '''
    Function that finds a user by name and returns the account
    '''
    return User.find_by_user(name)    

def check_existing_users(name):
    '''
    Function that check if a user account exists with that name and return a Boolean
    '''
    return User.user_exist(name)    

def display_users():
    '''
    Function that returns all the saved accounts
    '''
    return User.display_accounts()  

#CREDENTIALS

def create_credentials(credentials_name,credaccount_name,password,email):
    '''
    Function to create a new credentials account
    '''
    new_credentials = Credentials(credentials_name,credaccount_name,password,email)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials account
    '''
    credentials.save_credentials()    

def del_credentials(credentials):
    '''
    Function to delete a credentials account
    '''
    credentials.delete_credentials()    

def find_credentials(name):
        '''
    Function that finds a account by nane and returns the account
    '''
    #return Credentials.find_by_name(name)    

def check_existing_credentials(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(name)    
   
def display_credentials():  
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_credentials() 
  

def main():
    print("Welcome to the Password Manager. What is your name?")
    account_name = input()
    print(f"Hello {account_name}, sign up to Password Manager to create a user account.")
    print('\n')
    