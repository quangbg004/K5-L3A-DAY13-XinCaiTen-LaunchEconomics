# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**XinCaiTen · L3A** · Bản nháp trước duyệt chéo. Dữ liệu LogiX-VN là giả lập.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ (`simulated`) = tổng chi phí của mọi lần chạy, xem lại và làm lại ÷ 978 yêu cầu thành công. | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Chi phí mỗi việc thành công tăng 51,8% khi làm lại gấp đôi, 40,7% khi xem lại gấp đôi và 23,1% khi lương tăng 25% (`simulated`). | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Xem xét phạm vi `noi_dia` + `hang_nang`: 4.599 đ ở quy mô 45.000 yêu cầu/tháng và 5.784 đ ở nửa quy mô, đều đã gồm chi phí cố định (`simulated`), so với 12.000 đ. `quoc_te` riêng lẻ là 22.515 đ (`simulated`). | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trên mẫu chạy thử: 994/1.200 = 82,83% đóng trong 24 giờ và không mở lại trong 7 ngày, 48/177 = 27,12% gợi ý bị sửa hoặc bỏ trong số đã xem lại, 51/1.200 = 4,25% mở lại trong 7 ngày. Đặc tả event chờ hoàn thiện. | Chưa | Người phụ trách chỉ số |
| 5 · Bảng lỗi và cách khắc phục | Cần 2 bộ nhãn độc lập trên 20 ca, mục tiêu đồng thuận ít nhất 16/20 và 5 dòng khắc phục. | Chưa | Người phụ trách bảng lỗi |
| 6 · Pilot plan | D1 ước tính 1.251 yêu cầu mỗi nhóm nếu chia theo yêu cầu để phát hiện chênh lệch 5 điểm phần trăm. Chờ chốt cách chia, nhóm đối chứng và 3 luật dừng. | Chưa | Người phụ trách kế hoạch pilot |
| 7 · Rủi ro kinh tế | Ở phạm vi dự kiến, xem lại 100% và làm lại khoảng 15,3 phút/ca cho chi phí biến đổi 12.415 đ/việc thành công (`simulated`), cao hơn mức 12.000 đ thủ công ngay cả trước khi cộng chi phí cố định. | Giả lập | Người phụ trách chỉ số |

Nguồn kiểm tra: [A2–A4, B1–B4 và D1 từ script nhóm](../../src/lab13.py), [các phép chia trên dữ liệu chạy thử trong báo cáo nhóm](group_report.md#4-kết-quả).

**Đề xuất bản nháp: No-go ở lần duyệt này.** Quay lại Gate 2a khi người phụ trách bảng lỗi hoàn tất CP3, người phụ trách pilot chốt đối chứng, cỡ mẫu và luật dừng, và người phụ trách chỉ số có cách đo phút xem lại/làm lại để kiểm tra rủi ro vượt 12.000 đ/việc thành công.
