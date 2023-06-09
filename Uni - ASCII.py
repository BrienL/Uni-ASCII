#Responsible for Uni to ASCII
def ConvertUni2ASCII():
    UserInputCon = input('What Unicode value would you like to convert into ASCII? \n')
    if len(UserInputCon) > 1:
        strArray = []
        for i in UserInputCon:
            strArray.append(ord(i))
        print(strArray)
        main()
    elif len(UserInputCon) < 0:
        print("Invalid Input, please input at least one integer")
        main()
    print('Your Unicode converts to')
    print(ord(UserInputCon))
    main()

#Responsible for ASCII to Uni
def ConvertASCII2Uni():
    #Made sure the integer is within the set values
    UserInputCon = input('What ASCII (integer) would you like to convert into Unicode? \n')
    if not UserInputCon.isdigit():
        print("Invalid input")
        main()
    if int(UserInputCon) <= 127 and int(UserInputCon) >= 0:
        print('Your ASCII converts to')
        print(chr(int(UserInputCon)))
        main()
    else: 
        print('Your integer doenst fall into ASCII, please select a integer >0 and <128')
        main()

#Asks user about what they want to do
def main():
    print('\n')
    print('1) - Unicode to ASCII')
    print('2) - ASCII to Unicode')
    print('3) - Exit')
    UserInput = input('1, 2 or 3\n')
    if UserInput == '1':
        ConvertUni2ASCII()
    if UserInput == '2':
        ConvertASCII2Uni()
    if UserInput == '3':
        print('Closed \n')
        exit()
    else:
        print('Invalid input')
        main()

main()