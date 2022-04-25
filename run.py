#!/usr/bin/env python3.10

import string
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
    Function that returns all                                                                               the saved accounts
    '''
    return Credentials.display_credentials() 
  

def main():
    print("Welcome to the Password Manager. What is your name?")
    account_name = input()
    print(f"Hello {account_name}, sign up to Password Manager to create a user account.")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n SU -> SIGN UP.\n DA -> Display your account.\n LN ->LOGIN.\n ex ->exit Pass Word Locker. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create a Password Manager Account")
            print("_"*100)
            account_name = input('Account name:')
            print ('\n')
            user_name = input('User name:')
            print ('\n')
            print("to generate password use 'gp' or use your own using 'op'")
            own_password = input("choice ")
            if own_password == "gp":
                def randomStringDigits(stringLength=6):
                    lettersAndDigits = string.ascii_letters + string.digits
                    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
                print ("Generating a Random String including letters and digits")
                print ("First Random String is  ", randomStringDigits(8))
            elif own_password == "op":
                print('/n')
            password = input('Password : ')
            print ('\n')
            email_address = input('Email address:')
            save_users(create_user(account_name,user_name,password,email_address)) 
            print ('\n')
            print(f"A New {account_name} Account with the user name  {user_name} has been created.")
            print(f"You can now login to your {account_name} account using your password.")
            print ('\n')    
        elif own_password == "op":
                print('/n')
                password = input('Password : ')
                print ('\n')
                email_address = input('Email address:')
                save_users(create_user(account_name,user_name,password,email_address)) 
                print ('\n')
                print(f"A New {account_name} Account with the user name  {user_name} has been created.")
                print(f"You can now login to your {account_name} account using your password.")
                print ('\n')    
        elif short_code == 'da':
             if display_users():
                 print("Here is your account and your details")
                 print('\n')
                 for account in display_users():
                     print(f"Account name:{account.account_name}  User name: {account.user_name} Password:{account.password}")
                     print('\n')
             else:
                 print('\n')
                 print("You dont seem to have created an account.Sign up to create a new user account.")
                 print('\n')    
        elif short_code == 'ln':
            print("Enter your password to login.")
            search_account = input()
            if check_existing_users(search_account):
                search_cred = find_user(search_account)
                print("\033[1;32;1m   \n")
                print(f"You are now logged in to your {account_name} account")
                print("\033[1;37;1m   \n")   
#CREDENTIALS
                while True:
                    print('''
                    Use these short codes:
                    CA -> Create new credential.
                    DC -> Display your credentials list
                    ex ->Log out your credentials account.''')
                    short_code = input().lower()                
                      
                 