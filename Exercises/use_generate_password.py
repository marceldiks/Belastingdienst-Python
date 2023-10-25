from generate_password_function import generate_password

password = generate_password(required_length=10, n_lowercase=4)
print('Uw nieuwe wachtwoord is', password)