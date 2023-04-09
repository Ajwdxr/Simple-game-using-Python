x = input("Enter an integer between 0 and 1024..")
x = int(x)
a = 0
b = 1024
test = True
if x == 0:
    print("Your number is 0, Thank you for playing.")
    test = False
else:
    if x == 1024:
        print("Your number is 1024, Thank you for playing.")
        test = False
    while test == True:
        n = int ((a+b)/2)
        if n == x:
            print("Your number is ", n," Thank you for playing.")
            break
        else:
            if n < x:
                a = n
            else:
                b = n
            
            
