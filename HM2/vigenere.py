def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shifted_letter_code = (ord(key_repeated[i].lower()) + ord(plaintext[i].lower()) - 2 * ord('a')) % 26

            if plaintext[i].isupper():
                shifted_letter = chr(shifted_letter_code + ord('a')).upper()
            else:
                shifted_letter = chr(shifted_letter_code + ord('a'))
        else:
            shifted_letter = plaintext[i]

        ciphertext += shifted_letter

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shifted_letter_code = (ord(ciphertext[i].lower()) - ord(key_repeated[i].lower())) % 26

            if ciphertext[i].isupper():
                shifted_letter = chr(shifted_letter_code + ord('a')).upper()
            else:
                shifted_letter = chr(shifted_letter_code + ord('a'))
        else:
            shifted_letter = ciphertext[i]

        plaintext += shifted_letter
    return plaintext
