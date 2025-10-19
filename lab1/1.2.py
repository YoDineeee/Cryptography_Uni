def build_substitution_alphabet(key2):
    key2 = key2.upper()
    seen = set()
    result = ''
    for c in key2:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and c not in seen:
            result += c
            seen.add(c)
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if c not in seen:
            result += c
    return result

def validate_key2(key2):
    key2 = key2.upper()
    if len(key2) < 7:
        return False
    seen = set()
    for c in key2:
        if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
        if c in seen:
            return False
        seen.add(c)
    return True

def letter_to_number(letter, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    if letter in alphabet:
        return alphabet.index(letter)
    else:
        return None

def number_to_letter(number, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    if 0 <= number < 26:
        return alphabet[number]
    else:
        return None

def validate_text(text):
    for c in text:
        if c.upper() not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    return True

def caesar_cipher_2keys(text, key1, key2, encrypt=True):
    text = text.replace(' ', '').upper()
    if not validate_text(text):
        raise ValueError("The text must contain only English alphabet letters (A-Z, a-z).")
    if not (1 <= key1 <= 25):
        raise ValueError("Key 1 must be between 1 and 25.")
    if not validate_key2(key2):
        raise ValueError("Key 2 must contain only unique letters, at least 7 characters, from the Latin alphabet (A-Z, a-z).")
    subst_alphabet = build_substitution_alphabet(key2)
    result = ''
    for c in text:
        num = letter_to_number(c)
        if encrypt:
            shifted = (num + key1) % 26
            result += subst_alphabet[shifted]
        else:
            idx_in_subst = subst_alphabet.index(c)
            shifted = (idx_in_subst - key1) % 26
            result += number_to_letter(shifted)
    return result

def main():
    print("Choose operation: 1 - Encrypt, 2 - Decrypt")
    op = input("Enter option (1/2): ")
    if op not in ['1', '2']:
        print("Invalid option.")
        return
    key1 = input("Enter key 1 (1-25): ")
    try:
        key1 = int(key1)
    except ValueError:
        print("Key 1 must be a number between 1 and 25.")
        return
    key2 = input("Enter key 2 (min 7 unique letters, only A-Z): ")
    if not validate_key2(key2):
        print("Key 2 must contain only unique letters, at least 7 characters, from the Latin alphabet (A-Z, a-z).")
        return
    text = input("Enter the text: ")
    try:
        if op == '1':
            result = caesar_cipher_2keys(text, key1, key2, encrypt=True)
            print("Ciphertext:", result)
        else:
            result = caesar_cipher_2keys(text, key1, key2, encrypt=False)
            print("Decrypted message:", result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


