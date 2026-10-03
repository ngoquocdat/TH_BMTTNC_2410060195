# COS339 - Bài thực hành 01 và 02

Source được chuẩn bị để mở trực tiếp bằng Visual Studio Code và bám theo phạm vi được yêu cầu:

- Bài 01: cài đặt môi trường, Python cơ bản, List/Tuple/Dictionary, OOP.
- Bài 02: Caesar, Playfair, Flask web UI và API để kiểm thử bằng Postman.

## 1. Công cụ

Các công cụ xuất hiện trong bộ cài được cung cấp:

- Python 3.12.x
- Visual Studio Code
- Git for Windows
- Postman
- Qt Designer
- Win64 OpenSSL
- Npcap

Trong Bài 01 và Bài 02, source này trực tiếp sử dụng Python, VS Code, Git và Postman. Qt Designer, OpenSSL và Npcap thuộc các nội dung/bài thực hành sau nên chưa được gọi trong code của hai bài này.

## 2. Cài đặt và kiểm tra môi trường

Mở PowerShell hoặc terminal trong VS Code:

```powershell
python --version
git --version
code --version
```

Tạo virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Nếu PowerShell chặn activate script, có thể dùng Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

## 3. Bài 01

### 3.1. Cài đặt môi trường và Hello World

```powershell
python lab-01/01_environment/hello.py
```

### 3.2. Python cơ bản

File `lab-01/02_python_basic/basic.py` minh họa:

- biến và kiểu dữ liệu;
- input/print;
- toán tử số học, logic và so sánh;
- if/elif/else;
- for/while;
- xử lý chuỗi;
- function.

Chạy:

```powershell
python lab-01/02_python_basic/basic.py
```

### 3.3. List, Tuple, Dictionary

```powershell
python lab-01/03_collections/collections_demo.py
```

### 3.4. OOP - Quản lý sinh viên

Theo yêu cầu trong slide, sinh viên có:

- mã sinh viên tự tăng;
- tên;
- giới tính;
- chuyên ngành;
- điểm trung bình hệ 10.

Chương trình có thêm menu thêm, xem, tìm, cập nhật và xóa để dễ kiểm tra OOP.

```powershell
python lab-01/04_oop/student_manager.py
```

## 4. Bài 02

### 4.1. Caesar

Công thức dùng Z26:

- Mã hóa: `y = x + k (mod 26)`
- Giải mã: `x = y - k (mod 26)`

Ví dụ trong slide:

- Plaintext: `CHIENTRANH`
- Key: `17`
- Ciphertext: `TYZVEKIREY`

### 4.2. Playfair

Source sử dụng ma trận 5x5, I/J dùng chung ô. Với khóa `MONARCHY`, ma trận là:

```text
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z
```

Ví dụ trong slide:

```text
HELLOUXME -> CFSUPMVZCL
```

### 4.3. Chạy Flask

Từ thư mục gốc project:

```powershell
python lab-02/app.py
```

Mở trình duyệt:

```text
http://127.0.0.1:5000
```

Web có hai phần:

- Caesar Encrypt/Decrypt
- Playfair Encrypt/Decrypt

### 4.4. API cho Postman

Import file:

```text
lab-02/postman_collection.json
```

Endpoints:

```text
POST /api/caesar/encrypt
POST /api/caesar/decrypt
POST /api/playfair/encrypt
POST /api/playfair/decrypt
```

Ví dụ request Caesar:

```json
{
  "text": "CHIENTRANH",
  "key": 17
}
```

Ví dụ request Playfair:

```json
{
  "text": "HELLOUXME",
  "key": "MONARCHY"
}
```

## 5. Chạy test

```powershell
python -m pytest lab-02/tests -v
```

Các test xác minh trực tiếp hai ví dụ Caesar và Playfair trong slide.

## 6. Git workflow theo bài thực hành

Sau khi tạo repository trên GitHub và clone về máy:

```powershell
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"
```

### Nhánh lab-01

```powershell
git checkout -b lab-01
git add .
git commit -m "Complete lab 01"
git push -u origin lab-01
```

Sau đó tạo Pull Request `lab-01 -> main` trên GitHub.

### Nhánh lab-02

Sau khi `lab-01` đã merge vào `main`:

```powershell
git checkout main
git pull origin main
git checkout -b lab-02
git add .
git commit -m "Complete lab 02"
git push -u origin lab-02
```

Sau đó tạo Pull Request `lab-02 -> main`.

## 7. Lưu ý về đề bài trong tài liệu

Các slide chỉ ghi rằng phần Python cơ bản phải làm Câu 1-10 và phần List/Tuple/Dictionary phải làm một nhóm câu trong “Tài liệu học tập”, nhưng nội dung cụ thể của từng câu không xuất hiện trong các PDF đã cung cấp. Vì vậy source hiện tại triển khai đầy đủ các chủ đề được slide mô tả, thay vì tự đoán nội dung các câu chưa có đề.

Nếu có thêm file chứa nguyên văn Câu 1-10 và các câu List/Tuple/Dictionary, có thể thay các file demo bằng lời giải đúng từng câu mà không cần đổi cấu trúc project.
