import ast

def evaluate_input():
    """
    This function allows the user to input Python expressions and evaluates them using ast.literal_eval.
    The function loops infinitely until the user inputs "exit". If the user inputs an invalid expression,
    the function prints "Invalid input" and continues to the next input.
    """
    commend = ""
    while True:
        commend = input(">>>")
        if commend.lower() == "exit":
            break
        try:
            result = ast.literal_eval(commend)
            print(result)
        except (SyntaxError, ValueError):
            print("Invalid input")