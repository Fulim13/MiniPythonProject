import random
import string


def generate_password(input, length):
    return "".join(random.choices(input, k=length))


def generate_valid_password(length, is_num=True, is_special=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    combined = letters
    if is_num:
        combined += digits
    if is_special:
        combined += special

    pwd = ""
    is_meet_criteria = False
    has_char = False
    has_numbers = False
    has_special = False

    while not is_meet_criteria:
        pwd = generate_password(combined, length)

        # Check pwd contain character https://codefather.tech/blog/check-if-python-string-contains-number/
        if True in [char.isalpha() for char in pwd]:
            has_char = True

        # Check pwd contain digit
        if True in [char.isdigit() for char in pwd]:
            has_numbers = True

        # Check pwd contain special character
        for char in pwd:
            if char in special:
                has_special = True
                break

        is_meet_criteria = True
        if is_num:
            is_meet_criteria = has_numbers and has_char
        if is_special:
            is_meet_criteria = is_meet_criteria and has_special
        # print(f"Generator password {pwd}")

    return pwd


while True:
    length = input("Enter you length (enter is 8): ")
    if length == '':
        length = 8
        break
    try:
        length = int(length)
    except ValueError:
        print("You key in wrong value, Try Again!!!")
    else:
        break

want_num = input("Do you wanto have numbers (y/n)> ").lower() == 'y'
want_special = input(
    "Do you wanto have special character (y/n)> ").lower() == 'y'

print(generate_valid_password(length, want_num, want_special))
