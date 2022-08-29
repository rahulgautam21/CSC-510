#Calculator -- performs four basic operations - Addition, Subtraction, Multiplication and Division
  
  # ADD function
  def add(num1, num2):
    return num1 + num2
  
  # SUBTRACT function
  def subtract(num1, num2):
    return num1 - num2
  
  # MULTIPLY function
  def multiply(num1, num2):
    return num1 * num2
  
  # DIVIDE function
  def divide(num1, num2):
    # Check if num2 is 0 or not
    if num2 == 0:
      return "Denominator can't be zero"
    return num1 / num2
