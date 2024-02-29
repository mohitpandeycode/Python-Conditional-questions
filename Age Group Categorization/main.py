try:
    user_input = int(input("enter your age: "))
    if user_input <= 13 :
        print("you are a child coz your are under 13")
    elif user_input > 13 and user_input <=19 :
        print("you are a teenager coz your are under 19")
    elif user_input >= 20 and user_input <=59 :
        print("you are a adult coz your are under 60")
    else:
        print("you are a Senior")
except:
    print("Please enter a valid input!!")
