
import secrets
import string

class PasswordGenerator:
    def __init__(self, length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_digits = use_digits
        self.use_symbols = use_symbols
        self.charset = self._build_charset()

    def _build_charset(self):
        charset = ""
        if self.use_upper:
            charset += string.ascii_uppercase
        if self.use_lower:
            charset += string.ascii_lowercase
        if self.use_digits:
            charset += string.digits
        if self.use_symbols:
            charset += string.punctuation
        if not charset:
            raise ValueError("At least one character type must be selected.")
        return charset

    def generate(self):
        return ''.join(secrets.choice(self.charset) for _ in range(self.length))

def get_user_preferences():
    print("=== Advanced Password Generator ===\n")
    try:
        length = int(input("Password length: "))
        num_passwords = int(input("How many passwords to generate?: "))
    except ValueError:
        print("Invalid number. Exiting.")
        exit()

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("At least one character type must be selected. Exiting.")
        exit()

    save_option = input("Save passwords to file? (y/n): ").lower() == 'y'

    return length, num_passwords, use_upper, use_lower, use_digits, use_symbols, save_option

def save_to_file(passwords):
    file_name = "generated_passwords.txt"
    with open(file_name, 'w') as file:
        for pwd in passwords:
            file.write(pwd + '\n')
    print(f"\nPasswords saved to {file_name}")

def main():
    length, count, u, l, d, s, save = get_user_preferences()
    generator = PasswordGenerator(length, u, l, d, s)

    print("\nGenerated Passwords:")
    passwords = [generator.generate() for _ in range(count)]
    for idx, pwd in enumerate(passwords, 1):
        print(f"{idx}. {pwd}")

    if save:
        save_to_file(passwords)

if __name__ == "__main__":
    main()