"""Minh hoạ List, Tuple và Dictionary theo nội dung Bài 1."""


def list_demo() -> None:
    numbers = [5, 2, 9, 2]
    print("List ban đầu:", numbers)
    numbers.append(7)
    numbers.insert(1, 10)
    numbers.remove(2)
    popped = numbers.pop()
    print("List sau thao tác:", numbers)
    print("Phần tử pop:", popped)
    print("Duyệt list:", end=" ")
    for item in numbers:
        print(item, end=" ")
    print()


def tuple_demo() -> None:
    subjects = ("Python", "Security", "Python", "Git")
    print("Tuple:", subjects)
    print("Số lần 'Python' xuất hiện:", subjects.count("Python"))
    print("Vị trí đầu tiên của 'Security':", subjects.index("Security"))


def dictionary_demo() -> None:
    student = {
        "id": "SV001",
        "name": "Nguyen Van A",
        "major": "An toan thong tin",
        "gpa": 8.2,
    }
    print("Dictionary ban đầu:", student)
    student["gpa"] = 8.5
    student["email"] = "sv001@example.com"
    print("Keys:", list(student.keys()))
    print("Values:", list(student.values()))
    print("Items:")
    for key, value in student.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    print("=== LIST ===")
    list_demo()
    print("\n=== TUPLE ===")
    tuple_demo()
    print("\n=== DICTIONARY ===")
    dictionary_demo()
