def word_counter(file_path: str):
  """
  Counts the occurrences of each word in a given file.

  Parameters:
    file_path (str): The path to the file to be read.
  """
  word_count = {}
  with open(file_path, 'r') as file:
    for line in file:
      words = line.strip().split()
      for word in set(words):
        if word in word_count:
          word_count[word] += words.count(word)
        else:
          word_count[word] = words.count(word)
  
  for word, count in word_count.items():
    print(f"{word}: {count}")
