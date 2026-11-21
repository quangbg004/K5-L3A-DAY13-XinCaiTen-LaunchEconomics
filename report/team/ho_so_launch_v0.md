# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**XinCaiTen · L3A** · Hồ sơ trước duyệt chéo. Dữ liệu LogiX-VN là giả lập.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ (`simulated`) = tổng chi phí của mọi lần chạy, xem lại và làm lại ÷ 978 yêu cầu thành công. | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Chi phí mỗi việc thành công tăng 51,8% khi làm lại gấp đôi, 40,7% khi xem lại gấp đôi và 23,1% khi lương tăng 25% (`simulated`). | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Xem xét phạm vi `noi_dia` + `hang_nang`: 4.599 đ ở quy mô 45.000 yêu cầu/tháng và 5.784 đ ở nửa quy mô, đều đã gồm chi phí cố định (`simulated`), so với 12.000 đ. `quoc_te` riêng lẻ là 22.515 đ (`simulated`). | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chạy thử: 82,83% đóng trong 24 giờ và không mở lại trong 7 ngày (994/1.200), 27,12% gợi ý đã xem lại bị sửa hoặc bỏ (48/177), 4,25% mở lại trong 7 ngày (51/1.200). Đặc tả 6 event có `trace_id`. | Xong, có bằng chứng | Người phụ trách chỉ số |
| 5 · Bảng lỗi và cách khắc phục | Nhãn của Thắng trùng bộ tham khảo Codex ở 20/20 ca. Đã đề xuất 5 cách khắc phục. Bộ nhãn độc lập của người thứ hai còn thiếu. | Chưa | Người phụ trách bảng lỗi |
| 6 · Pilot plan | Chỉ `noi_dia` + `hang_nang` ở 6 depot. Phân ngẫu nhiên theo nhân viên, 20 người mỗi nhóm, 299 yêu cầu/người, 859 mẫu hiệu dụng/nhóm cho chênh lệch 6 điểm. Có 3 luật dừng. Với chênh lệch 5 điểm, lực thống kê khoảng 64%. | Xong, có bằng chứng | Người phụ trách kế hoạch pilot |
| 7 · Rủi ro kinh tế | Ở phạm vi dự kiến, xem lại 100% và làm lại khoảng 15,3 phút/ca cho chi phí biến đổi 12.415 đ/việc thành công (`simulated`), cao hơn mức 12.000 đ thủ công ngay cả trước khi cộng chi phí cố định. | Giả lập | Người phụ trách chỉ số |

Nguồn: [Chi phí](bang_chi_phi.md) · [Bảng lỗi](bang_loi.md) · [Pilot](pilot_plan.yaml) · [Chỉ số](chi_so.md).

**Điều kiện trước khi bật pilot:** Người phụ trách bảng lỗi bổ sung bộ nhãn độc lập còn thiếu. Giám đốc vận hành xác nhận đủ 20 nhân viên mỗi nhóm và chấp nhận đánh đổi khi chỉ đủ lực thống kê cho chênh lệch 6 điểm. Người phụ trách chỉ số xác nhận đo được thời gian xem lại và làm lại, đối soát hoàn tiền và báo cáo an toàn mỗi bước. Áp dụng luật dừng chi phí 8.000 đ/việc thành công theo kế hoạch. Ngày quyết định dự kiến 05/01/2027.

**Đề xuất của nhóm: Go có điều kiện** cho pilot trong phạm vi trên, sau khi kiểm tra các điều kiện trước khi bật.
