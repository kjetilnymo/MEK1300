username = input("Enter your username: ")
password = input("Enter your password: ")

length = len(password)

hidden_password = "*" * length

print(f"Hi {username}. Your password {hidden_password} is {length} characters long.")
