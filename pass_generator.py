import random
# import string

def password_generator():
    uppercase = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    lowercase = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    symbols = [i for i in '!#$%&*+/<=>?@\^_~']
    number = [str(n) for n in range(10)]
    caracteres = uppercase + lowercase + symbols + number

    # caracteres = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
    passwords = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        passwords.append(caracter_random)
    passwords = ''.join(passwords)    
    return passwords


def run():
    password = password_generator()
    print('You new password is: ' + password)


if __name__ == "__main__":
    run()