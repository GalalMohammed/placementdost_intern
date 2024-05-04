def calculate_average(numbers: list) -> float:
  """
  Calculates the average of a list of numbers.

  Parameters:
      numbers (list): A list of numbers to calculate the average from.

  Returns:
      float: The average of the numbers in the input list. If the input list is empty, returns 0.
  """
  total = 0
  count = 0

  for num in numbers:
    total += num
    count += 1

  if count == 0:
    return 0

  return total / count

# Example usage
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("Average:", average)
