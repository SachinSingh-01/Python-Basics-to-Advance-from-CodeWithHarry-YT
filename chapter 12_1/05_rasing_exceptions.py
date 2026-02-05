a=int(input("Enter a numer:"))
b=int(input("Enter second numer:"))

if(b==0):
    raise ZeroDivisionError("Hey our program is not meant  to divide numbers by zero")

else:
    print(f"The division a/b is {a/b}")