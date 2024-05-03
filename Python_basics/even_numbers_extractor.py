def extract_even_numbers(numbers: list) -> list:
  """
  Extracts even numbers from a list of numbers.

  Parameters:
      numbers (list): A list of numbers to extract even numbers from.

  Returns:
      list: A new list containing only the even numbers from the input list.
  """
  for num in numbers:
    if num % 2 != 0:
      numbers.remove(num)
  return numbers
