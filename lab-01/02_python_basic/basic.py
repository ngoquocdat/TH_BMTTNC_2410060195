"""Ví dụ tổng hợp các nội dung Python cơ bản trong Bài 1."""


def arithmetic_demo(a: float, b: float) -> None:
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    if b != 0:
        print(f"a / b = {a / b}")
        print(f"a // b = {a // b}")
        print(f"a % b = {a % b}")
    else:
        print("Không thể chia cho 0")
    print(f"a ** 2 = {a ** 2}")


def classify_number(number: float) -> str:
    if number > 0:
        return "Số dương"
    if number < 0:
        return "Số âm"
    return "Số 0"


def string_demo(text: str) -> None:
    print(f"Chuỗi gốc: {text}")
    print(f"Chữ hoa: {text.upper()}")
    print(f"Chữ thường: {text.lower()}")
    print(f"Độ dài: {len(text)}")
    print(f"Các từ: {text.strip().split()}")


def loop_demo(limit: int) -> None:
    print("for:", end=" ")
    for number in range(1, limit + 1):
        print(number, end=" ")
    print()

    print("while:", end=" ")
    number = 1
    while number <= limit:
        print(number, end=" ")
        number += 1
    print()


def main() -> None:
    print("=== PYTHON CƠ BẢN ===")
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    arithmetic_demo(a, b)

    print(f"a: {classify_number(a)}")
    print(f"b: {classify_number(b)}")

    text = input("Nhập một chuỗi: ")
    string_demo(text)

    limit = int(input("Nhập số nguyên dương để chạy vòng lặp: "))
    loop_demo(max(0, limit))


if __name__ == "__main__":
    main()
