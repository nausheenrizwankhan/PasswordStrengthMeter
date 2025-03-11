# import re --> -->

<!-- # def check_password_strength Meter(password): -->
#     # Initialize strength value
#     strength = 0

#     # Check password length
#     if len(password) >= 8:
#         strength += 1

#     # Check for lowercase, uppercase, number, and special characters
#     if re.search("[a-z]", password):
#         strength += 1
#     if re.search("[A-Z]", password):
#         strength += 1
#     if re.search("[0-9]", password):
#         strength += 1
#     if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
#         strength += 1

#     # Determine the strength based on the number of checks passed
#     if strength == 1:
#         return "Weak", strength
#     elif strength == 2:
#         return "Medium", strength
#     elif strength >= 3:
#         return "Strong", strength
#     else:
#         return "Very Weak", strength

# def display_strength_meter(strength_value):
#     # Display a visual representation of the password strength
#     bar = ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]']
    
#     for i in range(strength_value):
#         bar[i] = '[#]'
    
#     print("Password strength: " + "".join(bar))

# # Main Program
# def main():
#     password = input("Enter a password: ")
#     strength, strength_value = check_password_strength(password)

#     print(f"Password is {strength}")
#     display_strength_meter(strength_value)

# # Run the main function
# if __name__ == "__main__":
#     main()
