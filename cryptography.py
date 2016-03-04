"""
cryptography.py
Author: Glen Passow
Credit: Tess Snyder

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

action = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))

if action == e:
    encryptionText = str(input("Message: "))
    key = str(input("Key: "))
elif action == d:
    
elif action == q:
    print("Goodbye!")
else:
    print("Did not understand command, try again.")