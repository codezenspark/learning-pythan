# >>> in this program i use case statment to make calculter 
num1 = int(input(print("Enter num1 ")))
num2 = int(input(print("Enter num2 ")))
op = (input(print("enter any operter +,-,*,/")))

match op:
    case '+' :
        print("num1 + num2 =",num1+num2)
    case '-' :
        print("num1 - num2 =",num1-num2)
    case '*' :
        print("num1 * num2 =",num1*num2)
    case '/' :
        print("num1 / num2 =",num1/num2)
