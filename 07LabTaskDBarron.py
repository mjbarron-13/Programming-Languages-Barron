# Task D - Login Attempt Limiter
correct_password = "admin123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect password")

if attempts == max_attempts:
    print("Access denied")
