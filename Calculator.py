def calculate():
    print("Welcome to My Calculator!!!")
    number1 = int(input("Enter the First Number:"))
    number2 = int(input("Enter the Second Number:"))
    print('''Select the operation to be performed:
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division''')
    sel = int(input("Enter the operation:"))

    if sel == 1:
        print("{}+{}={}".format(number1,number2,number1+number2))

    elif sel == 2:
        print("{}-{}={}".format(number1,number2,number1-number2))

    elif sel == 3:
        print("{}*{}={}".format(number1,number2,number1*number2))
    
    elif sel == 4:
        print("{}/{}={}".format(number1,number2,number1/number2))
        
    else:   
        print("You have entered a wrong option!")
    again()

def again():
    option = input("Do you want to continue? Press 1 for YES and 2 for NO :")
    if option == 1:
        calculate()
    elif option == 2:
        print("Exiting the calculator!!")
    else:
        print("Exiting the calculator!!")

calculate()