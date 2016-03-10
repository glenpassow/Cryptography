"""
cryptography.py
Author: Glen Passow
Credit: Tess Snyder

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
x = 1
y = 87
while x == 1:

    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

    action = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))

    if action == "e":
        encryptionText = str(input("Message: "))
        key = str(input("Key: "))
        
        l = [associations.find(x)for x in encryptionText]
        k = [associations.find(x)for x in key] 
        
        cyclesMajor = len(l) // len(k)+1
        
        encryptionAddition = [k]*cyclesMajor
        encryptionAddition 
        print (encryptionAddition)
        print(cyclesMajor)
        
    
    elif action == "d":
        encryptionText = str(input("Message: "))
        key = str(input("Key: "))
        
    
    elif action == "q":
        print("Goodbye!")
        x = 2
        
        
    else:
        print("Did not understand command, try again.")