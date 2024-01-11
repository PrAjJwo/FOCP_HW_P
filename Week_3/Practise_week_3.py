'''Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise it should print
a greeting with their name as before.'''

greeting = input("Hello! What is you name: ")

if greeting == "":
    print("Hello, Stranger!")

else:
    print(f"Hello! {greeting}. How are you?")



'''Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error.'''

new_password = input("Enter a new password: ")
confirm_password = input("Confirm your password: ")

if new_password == confirm_password:
    print("Password Set")

else:
    print("Error Password does not match")


'''Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.'''

new_password = input("Enter a new password: ")
confirm_password = input("Confirm your password: ")

if new_password == confirm_password and 8 < len(new_password) <= 12:
    print("Password Set")

elif len(new_password) < 8 or len(new_password) >= 12:
    print("Please use 8 to 12 characters for Password.")

elif new_password != confirm_password:
    print("Error Password does not match")



'''Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']'''

new_password = input("Enter a new password: ")
confirm_password = input("Confirm your password: ")

if new_password == 'password' or 'letmein' or 'sesame' or 'hello' or 'justinbieber':
        print("This is a bad Password")

elif new_password == confirm_password and 8 < len(new_password) <= 12:
    print("Password Set")

elif len(new_password) <= 8 or len(new_password) >= 12:
    print("Please use 8 to 12 characters for Password.")

elif new_password != confirm_password:
    print("Error Password does not match")


'''Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''

a = 1
while a == 1:
    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm your password: ")

    if new_password == 'password' or 'letmein' or 'sesame' or 'hello' or 'justinbieber':
            print("This is a bad Password")

    if new_password == confirm_password and 8 < len(new_password) <= 12:
        print("Password Set")
        break

    if len(new_password) <= 8 or len(new_password) >= 12:
        print("Please use 8 to 12 characters for Password.")

    if new_password != confirm_password:
        print("Error Password does not match")

    confirmation = input("Do you want to redo it (Y/N): ")
    confirmation.upper()

    if confirmation == "Y":
         continue
    else:
         print("Thank You for your time")
         break
    

'''Write a program that displays the "Seven Times Table". That is, the result of
multiplying 7 by every number from 0 to 12 inclusive. The output might start:
0 x 7 = 0
1 x 7 = 7
2 x 7 = 14
and so on.'''

for i in range (0,13):
    multiplication = 7 * i
    print(f"7 x {i} = {multiplication} ")


'''Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times".'''

number = int(input("Enter a number: "))

if number > 0:
    for i in range (0,13):
        multiplication = number * i
        print(f"{number} x {i} = {multiplication} ")

elif number < 0:
    for i in range (13, 0, -1):
        multiplication = number * i
        print(f"{number} x {i} = {multiplication} ")





