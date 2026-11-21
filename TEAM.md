# Team

## Thông tin nhóm

- Tên nhóm: XinCaiTen
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-XinCaiTen-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/quangbg004/K5-L3A-DAY13-XinCaiTen-LaunchEconomics.git, main, 2e89a7f

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Thế Trường | 2A202603393 | truongnt20112004@gmail.com |  | Người viết code (CP1–CP2) |
|   2 | Dương Quang Bảo | 2A202603362 | dumabao69@gmail.com | wadiobao | Người kiểm số (CP1–CP2) & Coder CP4 |
|   3 | Kiều Văn Thắng | 2A202603424 | 26ai.thangkv@vinuni.edu.vn | katsu1154 | Người gắn nhãn 1 (CP3) & Chỉ số (CP5) |
|   4 |        |      |       |        | Người gắn nhãn 2, giữ hồ sơ & duyệt Gate 2a |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenTheTruong-2A202603393

### Phần việc phụ trách

- Người viết code CP1–CP2: Viết và kiểm thử các hàm tính toán kinh tế trong `src/lab13.py` (A1–A4, B1–B4) và tích hợp sẵn logic tính cỡ mẫu D1.

### Đóng góp cụ thể

- Hoàn thành đầy đủ code trong `src/lab13.py`, qua 3 test kiểm tra với sai số tuyệt đối < 1e-9.
- Tính chính xác CPS (4.472 đ [simulated], gấp 16,3 lần hóa đơn token/YC).
- Phân tích 4 loại yêu cầu, chứng minh đơn quốc tế không nên chạy agent và chạy lại tới 3 lần chỉ tốn tiền.
- Chạy 9 kịch bản độ nhạy, xếp hạng 3 yếu tố nhạy nhất và chỉ ra giới hạn 2 lần chạy rẻ nhất cả hệ thống (6.901.220 đ).
- Bàn giao số liệu và code hoàn chỉnh cho Người kiểm số (Bảo).

### Bằng chứng

- File code `src/lab13.py`.
- Báo cáo cá nhân `report/team/2A202603393_NguyenTheTruong.md`.
- Commit Git `2e89a7f`.


## Dương Quang Bảo - 2A202503362

### Phần việc phụ trách

- Kiểm tra và đối chiếu độc lập các phép tính chi phí trong CP1–CP2.
- Hoàn thiện bảng chi phí `report/team/bang_chi_phi.md` từ A1 đến B4.
- Phụ trách CP4: tính toán cỡ mẫu D1, phân tích tính khả thi của pilot và hoàn thiện kế hoạch `report/team/pilot_plan.yaml`.
- Đề xuất phương pháp phân nhóm, kiểm soát rủi ro và xây dựng các điều kiện dừng pilot.

### Đóng góp cụ thể

- Tính toán độc lập CPS tại A2, xác nhận chi phí trung bình cho mỗi yêu cầu thành công là khoảng **4.472 VND**.
- Phân tích chi phí theo từng loại yêu cầu, xác định `quoc_te` có CPS khoảng **22.515 VND**, cao hơn baseline nhân viên tự xử lý.
- Hoàn thiện các kịch bản phân tích độ nhạy B1–B4, xác định ba yếu tố ảnh hưởng lớn nhất đến CPS là số ca làm lại, thời gian xem lại và chi phí nhân công.
- Tính toán cỡ mẫu D1, đánh giá giới hạn 40 nhân viên hiện có và đề xuất MDE 6 điểm phần trăm để phù hợp với nguồn lực pilot.
- Xây dựng phương án pilot gồm 20 nhân viên nhóm can thiệp và 20 nhân viên nhóm đối chứng, phân nhóm ngẫu nhiên có phân tầng theo depot.
- Hoàn thiện 3 luật dừng pilot nhằm kiểm soát rủi ro vận hành, chi phí và mức độ sử dụng hệ thống.

### Bằng chứng

- `report/team/bang_chi_phi.md` – Bảng tính chi phí và phân tích độ nhạy A1–B4.
- `report/team/pilot_plan.yaml` – Kế hoạch pilot, cỡ mẫu D1, thiết kế D2 và các điều kiện dừng.
- `src/logix_requests.csv` – Dữ liệu yêu cầu dùng để đối chiếu chi phí và tỷ lệ thành công.
- `src/logix_runs.csv` – Dữ liệu các lần chạy dùng để tính token, tool và tỷ lệ thành công.
- `src/lab13.py` – Mã nguồn và công thức tính toán được sử dụng để kiểm tra kết quả.


## HoVaTen-MSSV (Mẫu cho các thành viên khác)

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
