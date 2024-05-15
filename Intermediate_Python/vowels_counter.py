def count_vowels(string: str) -> dict:
  """
  Counts the occurrences of each vowel (a, e, i, o, u) in the input string and returns a dictionary with the counts.
  
  Parameters:
    string (str): The input string to count the vowels from.

  Returns:
    dict: A dictionary containing the counts of each vowel 'a', 'e', 'i', 'o', 'u'.
  """
  vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

  for char in vowels.keys():
    vowels[char] = string.lower().count(char)

  return vowels

# Example usage
input_string = input("Enter a string: ")
result = count_vowels(input_string)
print(result)
