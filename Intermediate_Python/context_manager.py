import time

class Timer:
  def __enter__(self):
    """
    Initializes the context manager by setting the start time to the current time.
    """
    self.start_time = time.time()

  def __exit__(self, exc_type, exc_val, exc_tb):
    """
    Exit the context manager and print the execution time.

    Parameters:
        exc_type (Type[BaseException]): The type of the exception that caused the context manager to exit, if any.
        exc_val (BaseException): The exception that caused the context manager to exit, if any.
        exc_tb (TracebackType): The traceback of the exception that caused the context manager to exit, if any.
    """
    self.end_time = time.time()
    execution_time = self.end_time - self.start_time
    print(f"Execution time: {execution_time} seconds")

# Usage example
with Timer():
  # Code block to measure execution time
  # ...
  time.sleep(1)  # Simulate a long-running operation
  # ...
