from pathlib import Path
import sys

LAB02_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB02_DIR))

from ciphers.caesar import decrypt_caesar, encrypt_caesar
from ciphers.playfair import build_matrix, decrypt_playfair, encrypt_playfair


def test_caesar_example_from_slide():
    assert encrypt_caesar("CHIENTRANH", 17) == "TYZVEKIREY"
    assert decrypt_caesar("TYZVEKIREY", 17) == "CHIENTRANH"


def test_playfair_matrix_monarchy():
    assert build_matrix("MONARCHY") == [
        ["M", "O", "N", "A", "R"],
        ["C", "H", "Y", "B", "D"],
        ["E", "F", "G", "I", "K"],
        ["L", "P", "Q", "S", "T"],
        ["U", "V", "W", "X", "Z"],
    ]


def test_playfair_example_from_slide():
    assert encrypt_playfair("HELLOUXME", "MONARCHY") == "CFSUPMVZCL"
    assert decrypt_playfair("CFSUPMVZCL", "MONARCHY") == "HELXLOUXME"
