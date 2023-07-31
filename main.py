def vigenere_encrypt(plaintext, keyword):
    ciphertext = []
    keyword = keyword.upper()

    for i, char in enumerate(plaintext):
        shift = ord(keyword[i % len(keyword)]) - ord('A')
        encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        ciphertext.append(encrypted_char)

    return ''.join(ciphertext)


def main():
    plaintext = input("Enter the plaintext (all uppercase letters, no spaces): ")
    keyword = input("Enter the keyword (all uppercase letters): ")

    ciphertext = vigenere_encrypt(plaintext, keyword)
    print("Ciphertext:", ciphertext)


if __name__ == "__main__":
    main()
