def find_common_elements(list1: list, list2: list) -> list:
  """
  Finds the common elements between two lists.

  Parameters:
      list1 (list): The first list.
      list2 (list): The second list.

  Returns:
      list: A list containing the common elements between list1 and list2.
  """
  common_elements = []
  for element in list1:
    if element in list2:
      common_elements.append(element)
  return common_elements

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print(common_elements)
