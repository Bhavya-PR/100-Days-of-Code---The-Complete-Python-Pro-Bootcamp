import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
continue_with_prev_value = "n"
while True:
    if continue_with_prev_value == "n":
        first_num = float(input("What's the first number?"))
    operation_type = input("What's the mathematical operation you need to perform '+', '-', '*', '/' : ")
    second_num = float(input("What's the second number? "))
    result = operations[operation_type](first_num, second_num)
    print(f'{first_num} {operation_type} {second_num} = {result}')
    continue_with_prev_value = input(f"Wants to continue working with the previous result: {result} .(Type 'y' for Yes and 'n' for No): ").lower()
    if continue_with_prev_value == "y":
        first_num = result
    else:
        print("\n"*20)
        print(art.logo)
