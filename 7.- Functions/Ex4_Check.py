# Write a function calculates the total check after applying taxes
# The function should receive the total without taxes, and the
# tax is going to apply. If there's no tax, the tax will be 21%
# default

def check(amount,tax = 21):
    """
        CALCULATES TOTAL TAXES

        If there's no tax to apply, the default
        tax will be 21%
    """
    if tax <= 0 :
        total = amount + (amount * 0.21)
        print("The total is $" + 
              str(amount) + 
              ", default tax is 21.0%, check is: $" + 
              str(total))
        return
    if tax > 0:
        total = amount + (amount * (tax/100))
        print("The total is $" + 
              str(amount) + 
              ", the tax is " +
              str(tax) + 
              "%, check is: $" + 
              str(total))
        return


amount = float(input("\nWhat is the total?: $"))
tax = float(input("What is the tax?: "))

print("")
check(amount,tax)