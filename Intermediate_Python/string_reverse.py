def reverse_string(string: str) -> str:
  """
  Reverses a given string.

  Parameters:
    string (str): The string to be reversed.

  Returns:
    str: The reversed string.
  """
  reversed_string = ""
  for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]
  return reversed_string
