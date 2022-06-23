One = float(input("The first number: "))
Two = float(input("The second number: "))

Three = input("Your action(+ or -): ")
while True:
  if Three == "+":
    print("Results: ", (float(One + Two)))
    break
  elif Three == "-":
    print("Results: ", (float(One - Two)))
    break  
  else:
    print("Again!")
