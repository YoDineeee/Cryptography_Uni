import sys

# Romanian alphabet of 31 letters
ALPHABET = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'Ă', 'Â', 'Î', 'Ș', 'Ț'
]
ALPHABET_MAP = {ch: idx for idx, ch in enumerate(ALPHABET)}

def clean_message(msg):
    msg = msg.replace(' ', '').upper()
    for ch in msg:
        if ch not in ALPHABET_MAP:
            print("The message must contain only Romanian letters (A-Z, Ă, Â, Î, Ș, Ț).")
            sys.exit(1)
    return msg

def clean_key(key):
    key = key.replace(' ', '').upper()
    if len(key) < 7:
        print("The key must contain at least 7 characters.")
        sys.exit(1)
    for ch in key:
        if ch not in ALPHABET_MAP:
            print("The key must contain only Romanian letters (A-Z, Ă, Â, Î, Ș, Ț).")
            sys.exit(1)
    return key

def vigenere_encrypt(msg, key):
    encrypted = []
    key_len = len(key)
    for i, ch in enumerate(msg):
        m_idx = ALPHABET_MAP[ch]
        k_idx = ALPHABET_MAP[key[i % key_len]]
        c_idx = (m_idx + k_idx) % 31
        encrypted.append(ALPHABET[c_idx])
    return ''.join(encrypted)

def vigenere_decrypt(cipher, key):
    decrypted = []
    key_len = len(key)
    for i, ch in enumerate(cipher):
        c_idx = ALPHABET_MAP[ch]
        k_idx = ALPHABET_MAP[key[i % key_len]]
        m_idx = (c_idx - k_idx + 31) % 31
        decrypted.append(ALPHABET[m_idx])
    return ''.join(decrypted)

def main():
    op = input("Choose operation (c for encrypt, d for decrypt): ").strip().lower()
    key = clean_key(input("Enter the key: "))
    if op == 'c':
        msg = clean_message(input("Enter the message: "))
        print("Ciphertext:", vigenere_encrypt(msg, key))
    elif op == 'd':
        cipher = clean_message(input("Enter the ciphertext: "))
        print("Decrypted message:", vigenere_decrypt(cipher, key))
    else:
        print("Invalid operation. Choose 'c' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
