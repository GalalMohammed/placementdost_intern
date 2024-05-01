class BasicCalculator:
  def add(self, num1: int | float, num2: int | float) -> int | float:
    """
    Adds two numbers together and returns the result.

    Parameters:
        num1 (int or float): The first number to be added.
        num2 (int or float): The second number to be added.

    Returns:
        int or float: The sum of num1 and num2.
    """
    return num1 + num2

  def subtract(self, num1: int | float, num2: int | float) -> int | float:
    """
    Subtracts two numbers and returns the result.

    Parameters:
        num1 (int or float): The first number to be subtracted.
        num2 (int or float): The second number to be subtracted.

    Returns:
        int or float: The difference between num1 and num2.
    """
    return num1 - num2

  def multiply(self, num1: int | float, num2: int | float) -> int | float:
    """
    Multiply two numbers and return the result.

    Parameters:
        num1 (int or float): The first number to be multiplied.
        num2 (int or float): The second number to be multiplied.

    Returns:
        int or float: The product of num1 and num2.
    """
    return num1 * num2

  def divide(self, num1: int | float, num2: int | float) -> int | float:
    """
    Divide two numbers and return the result.

    Parameters:
        num1 (int or float): The first number to be divided.
        num2 (int or float): The second number to divide by.

    Returns:
        int or float: The quotient of num1 divided by num2. If num2 is zero,
        returns the string "Error: Division by zero is not allowed".
    """
    if num2 != 0:
      return num1 / num2
    else:
      return "Error: Division by zero is not allowed"
