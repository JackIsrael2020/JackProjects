# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:31:02 2020

@author: JackRhys
"""
import string

print(string.ascii_lowercase)

print(string.ascii_uppercase)

print(string.digits)


pw = input( "Please give a passsword, 8 characters including 1 uc, 1 lc, 1 number:")
print(pw)

l = False
u = False
d = False
count = 0
while count == 0:
    pw = input( "Please give a passsword, 8 characters including 1 uc, 1 lc, 1 number:")
    if len(pw) >= 8:
       for letter in pw:
            if letter in string.ascii_lowercase:
                l=True
            elif letter in string.ascii_uppercase:
                u=True
            elif letter in string.digits:
                d=True
        
       if l == True:
            if u == True: 
                if d == True:
                    print("Your password has been logged.")
                    count = 1
                else:
                    print("That is not a valid password. You are missing a digit.")
            else:
                if d == True:
                    print("That is not a valid password. You are missing an uppercase.")
                else:
                    print("That is not a valid password. You are missing a digit and an uppercase.")
       else:    
            if u == True: 
                if d == True:
                    print("That is not a valid password. You are missing a lowercase.")
                else:
                    print("That is not a valid password. You are missing a digit and a lowercase.")
            else:
                if d == True:
                    print("That is not a valid password. Its all digits.")
                else:
                    print("That is not a valid password. Please try again, reading the requirements carefully.")
                     
    else:
        print("That password is too short. Please try again.")
    
    
            
        