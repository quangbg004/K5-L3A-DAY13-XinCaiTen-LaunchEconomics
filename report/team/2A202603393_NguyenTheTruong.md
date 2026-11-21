# Báo cáo cá nhân — Nguyễn Thế Trường (2A202603393)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thế Trường
- MSSV: 2A202603393
- Email: truongnt20112004@gmail.com
- Vai trong nhóm: Người viết code (CP1–CP2 · Mô hình chi phí và độ nhạy)

## 2. Phần việc phụ trách

- **Nhiệm vụ A (CP1):** Viết và kiểm thử các hàm toán học nền tảng A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`). Viết hàm `mo_hinh` tính toán toàn diện chi phí từ trace dữ liệu thực tế kết hợp giả lập (token, tool, làm lại, xem lại) cho 1.200 yêu cầu. Phân rã theo 4 nhóm đơn và tính chi phí cố định cho phạm vi pilot.
- **Nhiệm vụ B (CP2):** Viết kịch bản tính toán bảng độ nhạy B1 (9 kịch bản), kịch bản đổi cặp B2, phân tích chi phí toàn hệ thống theo số lần chạy tối đa B3 và kịch bản xem lại 100% B4.
- **Bàn giao code:** Chạy xác thực số liệu, xuất kết quả để bàn giao cho Người kiểm số (Bảo) điền bảng chi phí, sau đó bàn giao file code để Bảo tiếp quản phần tính cỡ mẫu D1.

## 3. Đóng góp cụ thể

- Hoàn thành đầy đủ code trong `src/lab13.py` đảm bảo chạy thông suốt từ đầu đến cuối, vượt qua 3 test kiểm tra với sai số tuyệt đối < 1e-9.
- Tính toán chính xác chi phí mỗi việc thành công (4.472 đ [simulated], gấp 16,3 lần hóa đơn token/yêu cầu).
- Chứng minh bằng số liệu việc chạy lại tới lần thứ 3 không giúp ích cho nhóm `quoc_te` (tỉ lệ thành công giảm từ 30% ở lần 1 xuống 11,4% ở lần 2 và 2,2% ở lần 3).
- Phân tích và chỉ ra phương án giới hạn 2 lần chạy là tối ưu nhất cho toàn hệ thống công ty (6.901.220 đ), dù giới hạn 1 lần cho CPS trợ lý thấp nhất.

## 4. Bằng chứng

- File code: `src/lab13.py`.
- Các bảng số liệu xuất ra: Bảng A2, A3, A4, B1, B2, B3, B4 trong `report/team/bang_chi_phi.md`.
- Các commit trên Git liên quan đến việc triển khai code `lab13.py`.

## 5. Công cụ AI đã dùng

- **Antigravity (Gemini):** Hỗ trợ tra cứu nhanh công thức từ tài liệu hướng dẫn, cấu trúc code theo hàm chuẩn, soát lỗi chia nhầm tổng số yêu cầu thay vì số việc thành công.
- **Tự kiểm tra:** Tự chạy kiểm thử nội bộ 3 phép thử đáp án biết trước (1,20 · 1,25 · 1,25); kiểm tra tính tuyến tính của bảng độ nhạy (kịch bản giảm một nửa phải bằng một nửa mức tăng của kịch bản gấp đôi); đối chiếu số liệu xuất ra với kết quả của Người kiểm số (Bảo) đảm bảo sai số < 2%.

## 6. Tự đánh giá

- Hoàn thành xuất sắc nhiệm vụ viết code đúng tiến độ (trước 15:20), bàn giao đầy đủ số liệu chính xác và code sạch, dễ mở rộng cho đồng đội.
