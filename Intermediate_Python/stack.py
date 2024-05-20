class Stack:
  def __init__(self):
    """
    Initializes a new instance of the Stack class.

    This constructor creates an empty stack by initializing the `stack` attribute as an empty list.
    """
    self.stack = []

  def push(self, item):
    """
    Adds an item to the top of the stack.

    Args:
        item: The item to be added to the stack.
    """
    self.stack.append(item)

  def pop(self):
    """
    Removes and returns the top element from the stack.

    This method removes and returns the top element from the stack. If the stack is empty, 
    it raises an IndexError with the message "Stack is empty".

    Returns:
        The top element of the stack.

    Raises:
        IndexError: If the stack is empty.
    """
    if not self.is_empty():
      return self.stack.pop()
    else:
      raise IndexError("Stack is empty")

  def is_empty(self):
    """
    Check if the stack is empty.

    Returns:
        bool: True if the stack is empty, False otherwise.
    """
    return len(self.stack) == 0

  def peek(self):
    """
    Returns the top element of the stack without removing it.

    This method returns the top element of the stack without removing it. If the stack is empty,
    it raises an IndexError with the message "Stack is empty".

    Returns:
        The top element of the stack.

    Raises:
        IndexError: If the stack is empty.
    """
    if not self.is_empty():
      return self.stack[-1]
    else:
      raise IndexError("Stack is empty")
    
  def size(self):
    """
    Returns the number of elements in the stack.

    Returns:
        int: The number of elements in the stack.
    """
    return len(self.stack)

  def clear(self):
    """
    Removes all elements from the stack.
    """
    self.stack = []

  def __str__(self):
    """
    Returns a string representation of the stack.

    Returns:
        str: A string representation of the stack.
    """
    return str(self.stack)

  def __repr__(self):
    """
    Returns a string representation of the stack.

    Returns:
        str: A string representation of the stack.
    """
    return str(self.stack)
