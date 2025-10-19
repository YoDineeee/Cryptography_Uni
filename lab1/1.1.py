def letter_to_number(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in alphabet:
        return alphabet.index(letter)
    else:
        return None

def number_to_letter(number):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if 0 <= number < 26:
        return alphabet[number]
    else:
        return None
    
def validate_text(text):
    for c in text:
        if c.upper() not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    return True

def caesar_cipher(text, key, encrypt=True):
    text = text.replace(' ', '').upper()
    if not validate_text(text):
        raise ValueError("The text must contain only English alphabet letters (A-Z, a-z).")
    if not (1 <= key <= 25):
        raise ValueError("The key must be between 1 and 25.")
    result = ''
    for c in text:
        num = letter_to_number(c)
        if encrypt:
            shifted = (num + key) % 26
        else:
            shifted = (num - key) % 26
        result += number_to_letter(shifted)
    return result

def main():
    print("Choose operation: 1 - Encrypt, 2 - Decrypt")
    op = input("Enter option (1/2): ")
    if op not in ['1', '2']:
        print("Invalid option.")
        return
    key = input("Enter the key (1-25): ")
    try:
        key = int(key)
    except ValueError:
        print("Key must be a number between 1 and 25.")
        return
    if not (1 <= key <= 25):
        print("Key must be between 1 and 25.")
        return
    text = input("Enter the text: ")
    try:
        if op == '1':
            result = caesar_cipher(text, key, encrypt=True)
            print("Ciphertext:", result)
        else:
            result = caesar_cipher(text, key, encrypt=False)
            print("Decrypted message:", result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
