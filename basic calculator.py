# basic calculator


def add(num_1 , num_2):
    return num_1 + num_2

def sub(num_1 , num_2):
    return num_1 - num_2

def div(num_1 , num_2):
    if num_2 == 0:
        return "Sorry, cannot divide by zero"
    else:
        return num_1 / num_2

def multiply(num_1 , num_2):
    return num_1 * num_2

def mod(num_1 , num_2):
    return num_1 % num_2

print("Please select the operation you want to perform:\n")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")
print("5. Module")


choice = input("Enter your choice (1/2/3/4/5):\n")
num_1 = float(input("Enter the first number:\n"))
num_2 = float(input("Enter the second number:\n"))

if choice == '1':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == '2':
    print(num_1, "-", num_2, "=", sub(num_1, num_2))
elif choice == '3':
    print(num_1, "/", num_2, "=", div(num_1, num_2))
elif choice == '4':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == '5': 
    print(num_1, "%", num_2, "=", mod(num_1, num_2))
else:
    print("Invalid choice.")