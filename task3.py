#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]


username = input("Enter your username: ")
pwd = input("Enter your password: ")

for i in range(len(users)): 
    if username == users[i] and pwd == passwords[i]: 
        print("Login Successful!")
        break
else: print("Access denied.Try Again.")