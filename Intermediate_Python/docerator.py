import functools
import logging

def log_arguments_and_return(func):
  """
  Wraps a function to log its arguments and return value.
  
  Parameters:
      func (function): The function to be wrapped.
  
  Returns:
      function: The wrapped function.
  """
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    """
    A decorator function that logs information before and after calling the input function.
    
    Parameters:
    - args: positional arguments passed to the input function.
    - kwargs: keyword arguments passed to the input function.
    
    Returns:
    - The result of the input function.
    """
    logging.info(f"Calling function {func.__name__} with arguments: {args}, {kwargs}")
    result = func(*args, **kwargs)
    logging.info(f"Function {func.__name__} returned: {result}")
    return result
  return wrapper
