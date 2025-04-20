
def calculator_tool(expression):
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"