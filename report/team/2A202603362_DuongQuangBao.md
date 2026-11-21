# Báo cáo cá nhân — Dương Quang Bảo (2A202603362)

## 1. Thông tin thành viên

- Họ tên: Dương Quang Bảo
- MSSV: 2A202603362
- Vai trong nhóm: Người kiểm số CP1–CP2 và phụ trách kế hoạch pilot CP4.

## 2. Phần việc phụ trách

- Kiểm tra độc lập mô hình chi phí A2–A4 và bảng độ nhạy B1–B4.
- Điền `report/team/bang_chi_phi.md`.
- Nhận bàn giao logic tính cỡ mẫu từ `src/lab13.py`, đối chiếu D1 và hoàn thiện `report/team/pilot_plan.yaml`.
- Gửi phạm vi pilot, cỡ mẫu, phương pháp phân nhóm và ngưỡng dừng cho người giữ hồ sơ.

## 3. Đóng góp cụ thể

- Đối chiếu CPS A2 bằng phép tính độc lập: (245.585,132 + 84.000 + 1.780.000 + 2.264.000) / 978 = 4.471,97 đ, làm tròn 4.472 đ.
- Hoàn thiện A3: xác định `quoc_te` không phù hợp với pilot vì CPS 22.515 đ, bằng 1,88 lần baseline 12.000 đ; tỉ lệ `status=ok` giảm theo attempt.
- Hoàn thiện A4 và B1–B4; xác định ba yếu tố nhạy nhất là số ca làm lại, tỉ lệ xem lại và lương nhân viên.
- Tính D1 và ghi rõ đánh đổi MDE 6 điểm vì giới hạn 40 nhân viên; nếu hiệu ứng thật chỉ 5 điểm, power khoảng 0,64.
- Đề xuất pilot theo nhân viên: 20 can thiệp, 20 đối chứng; phân tầng theo depot; ba luật dừng có ngưỡng, thời hạn, hành động và người có quyền dừng.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`
- `report/team/pilot_plan.yaml`
- `TEAM.md`
- Các số liệu được tính lại từ `src/logix_runs.csv`, `src/logix_requests.csv` và công thức trong `src/lab13.py`.

## 5. Công cụ AI đã dùng

- ChatGPT hỗ trợ đọc yêu cầu, rà soát phép tính, soạn bảng và kiểm tra tính nhất quán của kế hoạch.
- Tự đối chiếu công thức, kiểm tra số liệu theo CSV và so sánh với logic trong `src/lab13.py`; không xem nội dung do AI tạo là kết quả kiểm chứng thay cho dữ liệu.

## 6. Tự đánh giá

Đã hoàn thiện nội dung CP1–CP2 và CP4 ở mức tài liệu. Cần chạy `python lab13.py`, kiểm tra YAML bằng `yaml.safe_load`, xem diff trên nhánh cá nhân và nhờ một thành viên rà soát trước khi merge.

