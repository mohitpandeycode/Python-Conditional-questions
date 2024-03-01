import random
print("welcome to password gemrator...")

char = "abcdefghijklmnopqrstuvwxwzABCDEFGHIJK@#$&:;LMNOPQRSTUVWXYZ0123456789" #we need define the charecters first
amount = input("enter the amout of passwords you want? : ") #ask the paswords amount form the user
amount = int(amount) # type caste all the givin amounts in int

length = input("enter your paswords lenght : ")  # ask password length from the use
length = int(length)

for pwd in range(amount): # make passwords from the given amount by user
    passwords = ''
    for i in range(length): #then make the passwords by given length
        passwords += random.choice(char)
    print (passwords)

# use that if you like ----->
# the password hacker....

# user = input("type your password")
# char = "0123456789"
# for pwd in range(362880):
#     passwords = ''
#     for i in range(1,7):
#         passwords += random.choice(char)
#     if user == passwords:
#         print (passwords)