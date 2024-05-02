def generate_fibonacci(n: int) -> list:
  """
  Generates a list of Fibonacci numbers up to the specified length.

  Parameters:
      n (int): The desired length of the Fibonacci list.

  Returns:
      list: A list of Fibonacci numbers up to the specified length.
  """
  fibonacci_list = [0, 1]
  while len(fibonacci_list) < n:
    next_number = fibonacci_list[-1] + fibonacci_list[-2]
    fibonacci_list.append(next_number)
  return fibonacci_list

fibonacci_numbers = generate_fibonacci(20)
print(fibonacci_numbers)
