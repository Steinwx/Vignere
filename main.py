def vigenere_encrypt(plaintext, keyword):
    """
    Encrypts plaintext using the Vigenere cipher with the provided keyword.

    Args:
        plaintext (str): The plaintext to be encrypted (all uppercase letters, no spaces).
        keyword (str): The keyword to be used for encryption (all uppercase letters).

    Returns:
        str: The encrypted ciphertext.
    """
    ciphertext = []
    keyword = keyword.upper()

    for i, char in enumerate(plaintext):
        # Calculate the shift value based on the corresponding letter in the keyword
        shift = ord(keyword[i % len(keyword)]) - ord('A')

        # Encrypt the current character using the Vigenere cipher algorithm
        encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        ciphertext.append(encrypted_char)

    return ''.join(ciphertext)


def main():
    """
    Main function to take user input and perform Vigenere encryption.
    """
    try:
        plaintext = input("Enter the plaintext (all uppercase letters, no spaces): ").upper()
        if not plaintext.isalpha():
            raise ValueError("Invalid input. The plaintext must contain only uppercase letters with no spaces.")

        keyword = input("Enter the keyword (all uppercase letters): ").upper()
        if not keyword.isalpha():
            raise ValueError("Invalid input. The keyword must contain only uppercase letters.")

        ciphertext = vigenere_encrypt(plaintext, keyword)
        print("Ciphertext:", ciphertext)

    except ValueError as e:
        print("Error:", e)
        # If there's an error, terminate gracefully and provide instructions
        print("Please restart the program and provide valid input.")


if __name__ == "__main__":
    main()
