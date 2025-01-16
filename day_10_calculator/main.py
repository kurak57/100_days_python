# # My Solution
# import art
# def calculator (n1, operator, n2):
#     def add(n1, n2):
#         return n1 + n2
#     def subtract(n1, n2):
#         return n1-n2
#     def divide(n1,n2):
#         return  n1/n2
#     def multiply(n1,n2):
#         return n1*n2
#     if operator == "+":
#         return add(n1,n2)
#     elif operator == "-":
#         return subtract(n1,n2)
#     elif operator == "*":
#         return multiply(n1,n2)
#     elif operator == "/":
#         return divide(n1,n2)

# while True:
#     print(art.logo)
#     first_number = float(input("What's the first number?: "))
#     operation = input("+\n-\n*\n/\n"
#                       "Pick an operation: ")
#     second_number = float(input("What's the next number?: "))
#     result = calculator(first_number, operation, second_number)
#     print(f"{first_number} {operation} {second_number} = {result}")
#     should_continue = input("Type 'y' to continue calculating with 0.0, "
#                             "or type 'n' to start a new calculation: ").lower()
#     while should_continue == "y":
#         first_number = result
#         operation = input("+\n-\n*\n/\n"
#                       "Pick an operation: ")
#         second_number = float(input("What's the next number?: "))
#         result = calculator(first_number, operation, second_number)
#         print(f"{first_number} {operation} {second_number} = {result}")
#         should_continue = input("Type 'y' to continue calculating with 0.0, "
#                                 "or type 'n' to start a new calculation: ").lower()

#Boorcamp solution
import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
