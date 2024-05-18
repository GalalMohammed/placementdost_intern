while True:
  try:
    print("Result:", int(input("Enter the numerator: ")) / int(input("Enter the denominator: ")))
    break
  except ValueError:
    print("Invalid input. Please enter a valid integer.")
  except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero denominator.")
  except:
    print("An error occurred. Please try again.")
