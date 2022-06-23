One = float(input("The first number: "))
Two = float(input("The second number: "))

Three = input("Your action(+ or -): ")

if Three == "+":
    print("Results: ", (float(One + Two)))
elif Three == "-":
    print("Results: ", (float(One - Two)))
else:
    while True:
        print("Again!")
        Three = input("Your action(+ or -): ")

        if Three == "+":
            print("Results: ", (float(One + Two)))
            break
        elif Three == "-":
            print("Results: ", (float(One - Two)))
            break  
