import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:              # Exception handler
    print("Error: Invalid Input.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:       # Exception handler
    print("Error: cannot divide by zero.")
    sys.exit(1)
    
print(f"{x} / {y} = {result}")