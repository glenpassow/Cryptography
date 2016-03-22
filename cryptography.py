"""
cryptography.py
Author: Glen Passow
Credit: Tess Snyder, stack overflow, david wilson

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
stop = 1
y = 87
while stop == 1:

    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

    action = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))

    if action == "e":
        encryptionText = str(input("Message: "))
        key = str(input("Key: "))
        
        l = [associations.find(x)for x in encryptionText]
        k = [associations.find(x)for x in key] 
        
        cyclesMajor = len(l) // len(k)
        b = cyclesMajor
        
        while b > 0:
            k.extend(k)
            b = b - 1
        
        encrypted = [x + y for x, y in zip(k, l)]
        
        for x in encrypted:
            print(associations[x],end="")
        print("")
        
    
    elif action == "d":
        encryptionText = str(input("Message: "))
        key = str(input("Key: "))
        
        l = [associations.find(x)for x in encryptionText]
        k = [associations.find(x)for x in key] 
        
        cyclesMajor = len(l) // len(k)
        b = cyclesMajor
        
        while b > 0:
            k.extend(k)
            b = b - 1
        
        encrypted = [x - y for x, y in zip(l, k)]
        
        for x in encrypted:
            print(associations[x],end="")
        print("")
        
    
    elif action == "q":
        print("Goodbye!")
        stop = 2
        
        
    else:
        print("Did not understand command, try again.")