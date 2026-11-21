# Báo cáo nhóm

Bản tổng hợp kết quả Lab 13. Dữ liệu LogiX-VN là giả lập.

## 1. Thông tin nhóm

- Tên nhóm: XinCaiTen
- Lớp: L3A
- Thành viên và vai trò: [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Đánh giá liệu trợ lý hoàn phí có đáng để đưa vào pilot có đối chứng. Nhóm dùng 1.200 yêu cầu và 1.624 lần chạy để kiểm tra chi phí, phân tích độ nhạy và xác định bằng chứng cần có trước Gate 2a.

## 3. Giải pháp

- **A · Chi phí:** Cộng tiền token và tool của mọi lần chạy với chi phí xem lại và làm lại ở cấp yêu cầu, rồi chia cho số yêu cầu thành công. Tách theo loại yêu cầu và cộng chi phí cố định cho phạm vi dự kiến. [Bảng chi phí](bang_chi_phi.md)
- **B · Độ nhạy:** So sánh 9 kịch bản, giới hạn 1–3 lần chạy và kịch bản xem lại 100%. Code đã xuất kết quả A/B để người kiểm số đối chiếu và điền bảng. [Code A/B](../../src/lab13.py)
- **C · Bảng lỗi:** Hai cột đã đủ 20 ca. Nhãn của Thắng trùng bộ tham khảo Codex ở 20/20 ca và bảng có 5 cách khắc phục. Chờ xác nhận nguồn bộ nhãn tự chốt của Người 2 để báo cáo mức đồng thuận độc lập. [Bảng lỗi](bang_loi.md)
- **D · Pilot:** Phân ngẫu nhiên theo nhân viên, phân tầng theo depot và chạy đối chứng đồng thời. Với 20 người mỗi nhóm và 299 yêu cầu mỗi người, mục tiêu là 859 mẫu hiệu dụng mỗi nhóm cho chênh lệch 6 điểm. Kế hoạch có 3 luật dừng về an toàn, chi phí và sử dụng. [Kế hoạch pilot](pilot_plan.yaml)
- **E · Chỉ số và quyết định:** Đã tính ba chỉ số trên mẫu chạy thử và đặc tả 7 event có `trace_id`, gồm số đo thời gian xem lại và làm lại cùng dữ liệu để tính tỉ lệ sử dụng. [Bảng chỉ số](chi_so.md) · [Hồ sơ launch v0](ho_so_launch_v0.md)

## 4. Kết quả

- `python lab13.py` chạy hết và in cả ba phép thử A1 đạt. Chi phí mỗi việc thành công là **4.472 đ** trên toàn mẫu. Trong phạm vi `noi_dia` + `hang_nang`, chi phí là **4.599 đ** ở quy mô 45.000 yêu cầu/tháng, đã gồm chi phí cố định, và **12.415 đ** chưa gồm chi phí cố định nếu xem lại 100% với khoảng 15,3 phút làm lại mỗi ca. Cả ba số là `simulated`. [Code và cách tính](../../src/lab13.py)
- **Chỉ số trong đợt chạy thử.** Đếm từ [CSV yêu cầu](../../src/logix_requests.csv) rồi chia: `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` cho **994/1.200 = 82,83%**. Trong 177 yêu cầu có `duoc_xem_lai = 1`, `quyet_dinh_xem_lai` là `sua` hoặc `bo` ở **48/177 = 27,12%**. `mo_lai_trong_7_ngay = 1` ở **51/1.200 = 4,25%**.
- **Đề xuất:** Go có điều kiện cho pilot `noi_dia` + `hang_nang` tại 6 depot. Trước khi bật, xác nhận nguồn nhãn CP3, đủ 40 nhân viên và dữ liệu đo chi phí, mức sử dụng và an toàn. [Hồ sơ launch](ho_so_launch_v0.md)
- **Duyệt chéo Gate 2a:** XinCaiTen chấm 3changngulam **30/30** và đã ghi phản hồi của đội trình về việc dừng khi phát hiện hoàn trùng. Báo cáo chưa có điểm hoặc nhận xét của hội đồng dành cho XinCaiTen. [Phiếu chấm nhóm bạn](phieu_cham.md)

## 5. Khó khăn và cách xử lý

- Với 40 nhân viên, chia theo nhân viên chỉ đạt mục tiêu lực thống kê 80% ở mức chênh lệch 6 điểm theo phương án đã chọn. Nếu hiệu ứng thật là 5 điểm, lực thống kê ước khoảng 64%.
- Đã kiểm đủ 6 file hồ sơ và 4 báo cáo cá nhân. Cả ba phép thử A1 đạt trên máy một thành viên và máy Quang, lần lượt **1,20 · 1,25 · 1,25**. YAML đọc được. [Checklist nộp bài](../../SUBMISSION.md#checklist)

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Chi phí nhân sự dùng số phút giả lập. Pilot cần ghi thời gian xem lại và làm lại để kiểm tra chi phí so với mốc thủ công 12.000 đ.
- Đợt chạy thử thiếu đối chứng. Pilot cần đối chứng đồng thời và theo dõi khả năng ảnh hưởng giữa hai nhóm trước khi kết luận hiệu quả.

## 8. Tài liệu tham khảo

- [Dữ liệu, giả định và công thức Lab 13](../../docs/du_lieu_va_cong_thuc.md)
- [Yêu cầu từng checkpoint](../../CHECKPOINTS.md)
