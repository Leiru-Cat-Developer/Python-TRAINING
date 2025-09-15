# Ask for 2 numbers, display the division
# If divisor is 0, the program display an error
divisor = float(input("Enter divisor value: "))
dividend = float(input("Enter dividend value: "))

if divisor == 0:
    print("\nError . . .\n")
else:
    print(f"\nResult: {dividend/divisor}\n")