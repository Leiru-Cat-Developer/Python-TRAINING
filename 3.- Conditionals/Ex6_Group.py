# Group A = [A - M] Womans , [N - Z] Mens
# Group B
name = input("What is your name?: ")
sex = input("Are you male[M] or female[F]: ")

if sex == 'F':
    print("You're group is A") if name.lower() < 'm' else print("You're group is B")
else:
    print("You're group is A") if name.lower() > 'n' else print("You're group is B")