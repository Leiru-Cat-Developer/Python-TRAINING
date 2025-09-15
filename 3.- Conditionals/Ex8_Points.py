# Each employee has a punctuation which is as follows:
# 0.0
# 0.4
# 0.6 or over
# there's no values between, the multiplied quantity is 2,400 by the punctuation

print("")
punctuation = float(input("Digit your punctuation: "))
print("")

if punctuation == 0.0:
    print(f"$2,400 times 0.0 = {(2400 * punctuation):0.2f}")
elif punctuation == 0.4:
    print(f"$2,400 times 0.4 = {(2400 * punctuation):0.2f}")
elif punctuation >= 0.6:
    print(f"$2,400 times {punctuation} = {(2400 * punctuation):0.2f}")
else:
    print("Punctuation invalid, try again . . .")