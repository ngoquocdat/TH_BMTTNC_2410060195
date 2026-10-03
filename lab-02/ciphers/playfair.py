"""Playfair cipher using a 5x5 matrix with I/J sharing one cell."""

import string

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is represented by I


def _letters_only(text: str) -> str:
    return "".join(char for char in text.upper() if char in string.ascii_uppercase).replace("J", "I")


def build_matrix(key: str) -> list[list[str]]:
    clean_key = _letters_only(key)
    sequence: list[str] = []

    for char in clean_key + ALPHABET:
        if char not in sequence:
            sequence.append(char)

    return [sequence[index:index + 5] for index in range(0, 25, 5)]


def _positions(matrix: list[list[str]]) -> dict[str, tuple[int, int]]:
    positions: dict[str, tuple[int, int]] = {}
    for row_index, row in enumerate(matrix):
        for col_index, char in enumerate(row):
            positions[char] = (row_index, col_index)
    return positions


def _prepare_plaintext(text: str) -> str:
    text = _letters_only(text)
    result: list[str] = []
    index = 0

    while index < len(text):
        first = text[index]
        second = text[index + 1] if index + 1 < len(text) else None

        if second is None:
            result.extend([first, "X"])
            index += 1
        elif first == second:
            result.extend([first, "X"])
            index += 1
        else:
            result.extend([first, second])
            index += 2

    return "".join(result)


def _prepare_ciphertext(text: str) -> str:
    text = _letters_only(text)
    if len(text) % 2 != 0:
        raise ValueError("Bản mã Playfair phải có số ký tự chẵn.")
    return text


def _transform_pair(
    first: str,
    second: str,
    matrix: list[list[str]],
    positions: dict[str, tuple[int, int]],
    direction: int,
) -> str:
    row1, col1 = positions[first]
    row2, col2 = positions[second]

    if row1 == row2:
        return matrix[row1][(col1 + direction) % 5] + matrix[row2][(col2 + direction) % 5]

    if col1 == col2:
        return matrix[(row1 + direction) % 5][col1] + matrix[(row2 + direction) % 5][col2]

    return matrix[row1][col2] + matrix[row2][col1]


def encrypt_playfair(text: str, key: str) -> str:
    if not _letters_only(key):
        raise ValueError("Khóa Playfair không được để trống.")

    matrix = build_matrix(key)
    positions = _positions(matrix)
    prepared = _prepare_plaintext(text)

    return "".join(
        _transform_pair(prepared[i], prepared[i + 1], matrix, positions, 1)
        for i in range(0, len(prepared), 2)
    )


def decrypt_playfair(text: str, key: str) -> str:
    if not _letters_only(key):
        raise ValueError("Khóa Playfair không được để trống.")

    matrix = build_matrix(key)
    positions = _positions(matrix)
    prepared = _prepare_ciphertext(text)

    return "".join(
        _transform_pair(prepared[i], prepared[i + 1], matrix, positions, -1)
        for i in range(0, len(prepared), 2)
    )
