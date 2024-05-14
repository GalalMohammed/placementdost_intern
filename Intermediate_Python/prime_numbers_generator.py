def prime_generator():
  """
  Generates an infinite sequence of prime numbers.

  This function is an iterator that yields prime numbers one by one. It starts
  with the number 2 and checks for primality of all odd numbers starting from 3.

  Yields:
      int: The next prime number in the sequence.

  Example:
      >>> gen = prime_generator()
      >>> next(gen)
      2
      >>> next(gen)
      3
      >>> next(gen)
      5
      >>> next(gen)
      7
  """
  primes = [2, 3, 5, 7]  # List to store prime numbers
  for prime in primes:
    yield prime
  num = 9  # Start checking from 9

  while True:
    is_prime = True
    for prime in primes:
      if num % prime == 0:
        is_prime = False
        break

    if is_prime:
      yield num
      primes.append(num)

    num += 2  # Check only odd numbers

# Testing the prime_generator
primes = prime_generator()
for _ in range(10):
  print(next(primes))
