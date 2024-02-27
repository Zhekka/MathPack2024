import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            letter_code = ord(letter)
            shifted_letter_code = letter_code + shift


            if letter.isupper():
                if shifted_letter_code > ord('Z'):
                    shifted_letter_code -= 26
            else:
                if shifted_letter_code > ord('z'):
                    shifted_letter_code -= 26

            shifted_letter = chr(shifted_letter_code)
        else:
            shifted_letter = letter

        ciphertext += shifted_letter

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            letter_code = ord(letter)
            shifted_letter_code = letter_code - shift


            if letter.isupper():
                if shifted_letter_code < ord('A'):
                    shifted_letter_code += 26
            else:
                if shifted_letter_code < ord('a'):
                    shifted_letter_code += 26

            shifted_letter = chr(shifted_letter_code)
        else:
            shifted_letter = letter

        plaintext += shifted_letter

    return plaintext



def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    max_matches = 0
    for shift in range(26):
        plaintext = ""
        for letter in ciphertext:
            if letter.isalpha():
                letter_code = ord(letter)
                shifted_letter_code = letter_code - shift

                if letter.isupper():
                    if shifted_letter_code < ord('A'):
                        shifted_letter_code += 26
                else:
                    if shifted_letter_code < ord('a'):
                        shifted_letter_code += 26

                shifted_letter = chr(shifted_letter_code)
            else:
                shifted_letter = letter

            plaintext += shifted_letter

        matches = 0
        for word in plaintext.split():
            if word in dictionary:
                matches += 1

        if matches > max_matches:
            max_matches = matches
            best_shift = shift

    return best_shift
