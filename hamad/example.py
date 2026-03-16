print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
operation = int(input("Choose an operation: "))

if(operation in [1, 2, 3, 4]):
  n1 = float(input("Enter first number: "))
  n2 = float(input("Enter second number: "))
  if(operation == 1):
    result = n1 + n2
  elif(operation == 2):
    result = n1 - n2
  elif(operation == 3):
    result = n1 * n2
  else: 
    if(n2 == 0):
        print("Divide by zero error")
        exit()
    else:
        result = n1/n2
else:
  print("INVALID ENTRY!")
  exit()

print(f"Result: {result}")
