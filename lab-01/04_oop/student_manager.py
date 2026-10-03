"""Chương trình quản lý sinh viên bằng OOP.

Thuộc tính theo slide:
- Mã sinh viên tự tăng
- Tên
- Giới tính
- Chuyên ngành
- Điểm trung bình hệ 10
"""

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    gender: str
    major: str
    gpa: float
    id: int = field(init=False)

    _next_id = 1

    def __post_init__(self) -> None:
        self.id = Student._next_id
        Student._next_id += 1

    def update(self, name: str, gender: str, major: str, gpa: float) -> None:
        self.name = name
        self.gender = gender
        self.major = major
        self.gpa = gpa

    def __str__(self) -> str:
        return (
            f"ID={self.id} | Tên={self.name} | Giới tính={self.gender} | "
            f"Chuyên ngành={self.major} | GPA={self.gpa:.2f}"
        )


class StudentManager:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def add_student(self, name: str, gender: str, major: str, gpa: float) -> Student:
        student = Student(name=name, gender=gender, major=major, gpa=gpa)
        self.students.append(student)
        return student

    def find_by_id(self, student_id: int) -> Student | None:
        return next((s for s in self.students if s.id == student_id), None)

    def delete_by_id(self, student_id: int) -> bool:
        student = self.find_by_id(student_id)
        if student is None:
            return False
        self.students.remove(student)
        return True

    def list_students(self) -> list[Student]:
        return self.students.copy()


def read_gpa() -> float:
    while True:
        try:
            gpa = float(input("Điểm trung bình (0-10): "))
            if 0 <= gpa <= 10:
                return gpa
            print("Điểm phải nằm trong khoảng 0 đến 10.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")


def read_student_info() -> tuple[str, str, str, float]:
    name = input("Tên: ").strip()
    gender = input("Giới tính: ").strip()
    major = input("Chuyên ngành: ").strip()
    gpa = read_gpa()
    return name, gender, major, gpa


def print_menu() -> None:
    print("\n=== QUẢN LÝ SINH VIÊN ===")
    print("1. Thêm sinh viên")
    print("2. Xem danh sách")
    print("3. Tìm theo mã sinh viên")
    print("4. Cập nhật sinh viên")
    print("5. Xóa sinh viên")
    print("0. Thoát")


def main() -> None:
    manager = StudentManager()

    while True:
        print_menu()
        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            student = manager.add_student(*read_student_info())
            print(f"Đã thêm sinh viên, mã: {student.id}")
        elif choice == "2":
            students = manager.list_students()
            if not students:
                print("Danh sách trống.")
            for student in students:
                print(student)
        elif choice == "3":
            student_id = int(input("Nhập mã sinh viên: "))
            student = manager.find_by_id(student_id)
            print(student if student else "Không tìm thấy sinh viên.")
        elif choice == "4":
            student_id = int(input("Nhập mã sinh viên cần cập nhật: "))
            student = manager.find_by_id(student_id)
            if student is None:
                print("Không tìm thấy sinh viên.")
                continue
            student.update(*read_student_info())
            print("Đã cập nhật.")
        elif choice == "5":
            student_id = int(input("Nhập mã sinh viên cần xóa: "))
            print("Đã xóa." if manager.delete_by_id(student_id) else "Không tìm thấy sinh viên.")
        elif choice == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
