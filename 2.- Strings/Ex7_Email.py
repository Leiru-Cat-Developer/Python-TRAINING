# Ask for an email and replace the domain with 'ceu.es'
email = input("Please enter your email: ")
print("Your email with the new domain is:", email[:email.find('@')] + '@ceu.es')