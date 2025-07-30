numberOne = float(input("Enter the first number"))

numberTwo = float(input("Enter the second number"))

operation = str(input("Enter the operation (+,-,*,/)"))

if (operation == "*"):
    print(f"Multiplication {numberOne} * {numberTwo} {numberOne*numberTwo}")
elif (operation == "+"):
    print(f"Addition {numberOne} + {numberTwo}={numberOne+numberTwo}")
elif (operation == "-"):
    print(f"Subtraction {numberOne} - {numberTwo}={numberOne-numberTwo}")
elif (operation == "/"):
    print(f"Quotient {numberOne} / {numberTwo}={numberOne/numberTwo}")
