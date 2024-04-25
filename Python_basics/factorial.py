def factorial(n: int) -> int:
  """
  Calculates the factorial of a given number.

  Args:
      n (int): The number to calculate the factorial of.

  Returns:
      int: The factorial of the given number.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

# Test the function
number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is", result)
