def is_palindrome(word: str) -> bool:
    """
    Check if a given word is a palindrome.

    Parameters:
        word (str): The word to check for palindrome.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    # Remove any spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Get user input
user_input = input("Enter a word: ")
# Check if the input is a palindrome
if is_palindrome(user_input):
  print("The word is a palindrome.")
else:
  print("The word is not a palindrome.")
