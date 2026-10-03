"""Caesar cipher over A-Z (Z26)."""


def _shift_char(char: str, shift: int) -> str:
    if "A" <= char <= "Z":
        return chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
    if "a" <= char <= "z":
        return chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
    return char


def encrypt_caesar(text: str, key: int) -> str:
    key %= 26
    return "".join(_shift_char(char, key) for char in text)


def decrypt_caesar(text: str, key: int) -> str:
    key %= 26
    return "".join(_shift_char(char, -key) for char in text)
