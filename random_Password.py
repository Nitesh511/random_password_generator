import random 
import string
import time
import datetime

print("Welcome to my random Password Generator :)")

def password_generator(): #making a function
    times=datetime.datetime.now() #generating current time
    start=time.time() #calculate time taken to execute the code
    length=int(input("Enter the length of your password:")) #Asking user for the length of the password 
    lower_case=string.ascii_lowercase
    upper_case=string.ascii_uppercase
    digit=string.digits
    symbol=string.punctuation

    combine=lower_case+upper_case+digit+symbol #joining all characters
    x=random.sample(combine, length) #generating random numbers
    password="".join(x) #joinging all the characters
    print(password)
    print(f"This password was created on {times}")
    print(f"This code took {time.time()-start} seconds to execute")
    password_generator() #calling the fnction 

password_generator() #calling the fnction
