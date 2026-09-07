# 📝 Task Manager CLI

Một ứng dụng giao diện dòng lệnh (CLI) đơn giản và nhẹ nhàng được viết bằng Python giúp bạn quản lý các công việc hàng ngày. Dữ liệu được lưu trữ an toàn trong file JSON và danh sách công việc được hiển thị dưới dạng bảng trực quan.

## 🚀 Tính năng nổi bật

- **Thêm, sửa, xóa** công việc dễ dàng.
- Cập nhật trạng thái linh hoạt: `to-do` (cần làm), `in-progress` (đang làm), `done` (hoàn thành).
- Theo dõi thời gian tạo (`createdAt`) và thời gian cập nhật lần cuối (`updatedAt`).
- Hiển thị danh sách công việc dưới dạng bảng đẹp mắt (sử dụng thư viện `tabulate`).
- Lưu trữ dữ liệu độc lập vào file `data.json`.

## 🛠️ Yêu cầu hệ thống

- Đã cài đặt [Python 3.x](https://www.python.org/downloads/) trên máy tính.

## 📦 Hướng dẫn cài đặt

Tải mã nguồn về máy (hoặc clone repository này):
    pip install -r requirements.txt

## 📋 Danh sách các lệnh (Commands)

* `python main.py add "Tên công việc"` — Thêm một công việc mới vào danh sách (mặc định trạng thái là `to-do`).
* `python main.py list` — Hiển thị toàn bộ công việc đang có.
* `python main.py update <id> "Nội dung mới"` — Cập nhật lại tên/mô tả của công việc dựa vào ID.
* `python main.py delete <id>` — Xóa vĩnh viễn công việc ra khỏi hệ thống.
* `python main.py mark-in-progress <id>` — Đánh dấu công việc đang được thực hiện (`in-progress`).
* `python main.py mark-done <id>` — Đánh dấu công việc đã hoàn thành (`done`).
* `python main.py list-to-do` — Liệt kê các công việc chưa bắt đầu (`to-do`).
* `python main.py list-in-progress` — Liệt kê các công việc đang thực hiện (`in-progress`).
* `python main.py list-done` — Liệt kê các công việc đã hoàn thành (`done`).

Project URL: https://roadmap.sh/projects/task-tracker