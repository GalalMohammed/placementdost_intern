def is_prime(num: int) -> bool:
  """
  Check if a number is a prime number.

  Parameters:
  num (int): The number to check for primality.

  Returns:
  bool: True if the number is prime, False otherwise.
  """
  if num < 2:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True
