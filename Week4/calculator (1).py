# calculator_flawed.py

# This program is a simple calculator

def calculate(num1, num2, op):
    """
    This function takes two numbers and an operator
    and returns the result.
    """
    result = 0
    if op == "add":
        res = num1 + num2 
        return res
    elif op == "subtract":
        result = num1 - num2
        
    elif op == "multiply":
        
        result = (lambda x, y: x * y)(num1, num2)
        return result
    elif op == 'divide': 
        if num2 == 0:
            print("Error: Cannot divide by zero, Dude!") 
            
        else:
            result = num1 / num2
            return result
    else:
        
        pass 

    
    return result 


def get_user_input():
    """Gets input from the user for two numbers and an operation."""
    n1 = input("Enter first number: ")
    n2 = input("Enter second number: ")
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    
    return float(n1), float(n2), operation.lower().strip() 


def display_Result(value_1, value_2, OpErAtIoN, result_val): 
    
    print(str(value_1) + " " + OpErAtIoN + " " + str(value_2) + " = " + str(result_val))


# --- Main execution ---
if __name__ == "__main__":
    print("Simple Calculator v0.1")
    print("---------------------")

    
    num_a, num_b, op_choice = get_user_input()

    calculated_value = calculate(num_a, num_b, op_choice)

    
    if calculated_value is not None: # A bit of checking, but could be more robust
        display_Result(num_a, num_b, op_choice, calculated_value)
    else:
        print("Calculation could not be performed.") 

    # Another operation to show a potential issue with 'calculate'
    print("\nTrying another calculation (10 / 0):")
    res2 = calculate(10, 0, "divide")
    

    print("\nTrying 'subtract' (5 - 2):")
    res3 = calculate(5, 2, "subtract")
    if res3 is not None:
        display_Result(5, 2, "subtract", res3)
    else:
        print("Subtraction failed. Result was:", res3) 

    print("\nTrying invalid operation (5 ? 2):")
    res4 = calculate(5, 2, "modulo")
    if res4 is not None:
        display_Result(5, 2, "modulo", res4)
    else:
        print("Invalid operation. Result was:", res4) 



unused_var = "I am not used"
another_one = 42
