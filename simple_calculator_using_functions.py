def arithmetic_operations(first_number, second_number, operator):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        if second_number == 0:
            return "Error: Division by zero"
        return first_number / second_number
    elif operator == "%":
        if second_number == 0:
            return "Error: Division by zero"
        return first_number % second_number
    else:
        return "Error: Invalid operator"


while True:
    try:
        user_input_1 = float(input("Enter first number: "))
        user_input_2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        continue

    user_input_operator = input("Enter operator (+, -, *, /, %): ").strip()

    result = arithmetic_operations(user_input_1, user_input_2, user_input_operator)
    print(f"Result = {result}")

    user_input_for_repeat = input("Press Enter to continue or type 'q' to quit: ").strip().lower()

    if user_input_for_repeat == "q":
        print("Calculator closed.")
        break