import random

def generate_password(required_length: int = 8,
                      n_lowercase: int = 2,
                      n_uppercase: int = 2,
                      n_numbers: int = 1,
                      n_special: int = 1) -> str:

    LOWERCASE_CHARACTERS = 'abcdefghijkmnopqrstuvwxyz' # removed l
    UPPERCASE_CHARACTERS = 'ABCDEFGHJKLMNPQRSTUVWXYZ' # removed I and O
    NUMBER_CHARACTERS = '0123456789'
    SPECIAL_CHARACTERS = '@#$%&*+?!'

    lower = random.choices(LOWERCASE_CHARACTERS, k = n_lowercase)
    upper = random.choices(UPPERCASE_CHARACTERS, k = n_uppercase)
    numbers = random.choices(NUMBER_CHARACTERS, k = n_numbers)
    special = random.choices(SPECIAL_CHARACTERS, k = n_special)
    extra = random.choices(LOWERCASE_CHARACTERS +
                           UPPERCASE_CHARACTERS +
                           NUMBER_CHARACTERS +
                           SPECIAL_CHARACTERS,
                           k = required_length - n_lowercase - n_uppercase - n_numbers - n_special)

    all_characters = lower + upper + numbers + special + extra

    random.shuffle(all_characters)

    password = ''.join(all_characters)

    return password


# ---------------------------------------------------------

if __name__ == '__main__':

    new_password = generate_password(required_length = 10)

    print('New password: ', new_password)

