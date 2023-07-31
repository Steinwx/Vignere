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


def get_valid_input(prompt, validator_func):
    """
    Get user input and validate it using the provided validator function.

    Args:
        prompt (str): The prompt message to display to the user.
        validator_func (function): The function used to validate the user input.

    Returns:
        str: The user input that passed the validation.
    """
    while True:
        user_input = input(prompt).strip().upper()
        if validator_func(user_input):
            return user_input
        print("Invalid input. Please try again.")


def is_valid_uppercase(text):
    """
    Check if the input text contains only uppercase letters.

    Args:
        text (str): The input text to be validated.

    Returns:
        bool: True if the input text contains only uppercase letters, False otherwise.
    """
    return text.isalpha() and text.isupper()


def main():
    """
    Main function to take user input and perform Vigenere encryption.
    """
    print("=== Vigenere Cipher Encryption Program ===")
    
    plaintext_prompt = "Enter the plaintext (all uppercase letters, no spaces): "
    keyword_prompt = "Enter the keyword (all uppercase letters): "

    plaintext = get_valid_input(plaintext_prompt, is_valid_uppercase)
    keyword = get_valid_input(keyword_prompt, is_valid_uppercase)

    ciphertext = vigenere_encrypt(plaintext, keyword)
    print("Ciphertext:", ciphertext)


if __name__ == "__main__":
    main()
