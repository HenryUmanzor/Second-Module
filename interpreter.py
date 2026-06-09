X,Z,Y = input("Problem: ").split(" ")
def interpreter():
    match Z:
        case "+":
            Result  = (float(X) + float(Y))
            print(Result)
        case "-":
            Result  = (float(X) - float(Y))
            print(Result)
        case "*":
            Result  = (float(X) * float(Y))
            print(Result)
        case "/":
            Result = (float(X) / float(Y))
            print(Result)
interpreter()
