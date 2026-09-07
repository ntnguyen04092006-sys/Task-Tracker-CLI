import json
from main import load_data

def test_load_data_khi_file_khong_ton_tai(tmp_path):
    # tmp_path tự động tạo ra một thư mục tạm thời, và sẽ tự xóa sạch sau khi test xong.
    
    # 1. Trỏ đường dẫn tới một file KHÔNG CÓ THẬT trong thư mục tạm
    fake_file = tmp_path / "khong_co_file_nay.json"
    
    # 2. Chạy hàm load_data với file giả đó
    result = load_data(fake_file)
    
    # 3. KIỂM ĐỊNH: Chắc chắn nó phải trả về một mảng rỗng []
    assert result == []

def test_load_data_khi_file_hop_le(tmp_path):
    # 1. Tạo ra một file giả trong thư mục tạm
    fake_file = tmp_path / "du_lieu_gia.json"
    
    # 2. Ghi một công việc mẫu vào file giả đó
    danh_sach_mau = [{"id": 1, "description": "Học viết Unit Test", "status": "todo"}]
    with open(fake_file, "w", encoding="utf-8") as f:
        json.dump(danh_sach_mau, f)
        
    # 3. Yêu cầu hàm load_data đi đọc cái file giả vừa tạo
    result = load_data(fake_file)
    
    # 4. KIỂM ĐỊNH: Chắc chắn mảng đọc ra phải có 1 phần tử, và mô tả phải khớp
    assert len(result) == 1
    assert result[0]["description"] == "Học viết Unit Test"