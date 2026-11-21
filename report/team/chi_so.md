# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... *(chỉ số trong đợt chạy thử là ...)* |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... *(chỉ số trong đợt chạy thử là ...)* |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... *(chỉ số trong đợt chạy thử là ...)* |
| Dùng | Nhóm tự đề xuất: Tỉ lệ chấp nhận nguyên bản | Số yêu cầu có `quyet_dinh_xem_lai == 'giu'` chia tổng số yêu cầu được xem lại | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ hoàn tiền sai mức/trùng lệnh | Số yêu cầu phát sinh `refund_audit_mismatch` chia tổng số yêu cầu đã đóng | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_created` | Hệ thống CSKH | `request_id`, `depot`, `loai`, `so_tien_vnd`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_finished` | Trợ lý hoàn phí | `run_id`, `request_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls`, `trace_id` | Khi kết thúc mỗi lần chạy của agent |
| `review_decision_logged` | Giao diện nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `review_seconds`, `trace_id` | Khi nhân viên xem lại và chọn giữ/sửa/bỏ |
| `request_closed` | Hệ thống CSKH | `request_id`, `dong_trong_24h`, `ket_qua`, `trace_id` | Khi yêu cầu được đóng và phản hồi khách |
| `request_reopened_7d` | Hệ thống CSKH | `request_id`, `days_since_close`, `reopen_reason`, `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |
| `refund_audit_mismatch` | Hệ thống đối soát/Sổ cái | `request_id`, `expected_vnd`, `actual_vnd`, `mismatch_type`, `trace_id` | Khi job đối soát phát hiện hoàn sai tiền hoặc trùng lệnh |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h & không mở lại 7 ngày):** tính từ `request_created`, `request_closed` (`dong_trong_24h == 1`) và loại trừ các `request_id` có `request_reopened_7d`.
- **Chỉ số dùng — Tỉ lệ bỏ qua gợi ý:** tính từ `review_decision_logged` (đếm `quyet_dinh_xem_lai` là `sua` hoặc `bo` chia tổng số event `review_decision_logged`).
- **Chỉ số an toàn — Tỉ lệ lỗi lọt đến khách:** tính từ `request_reopened_7d` chia tổng `request_created`.
- **Chỉ số dùng đề xuất — Tỉ lệ chấp nhận nguyên bản:** tính từ `review_decision_logged` (đếm `quyet_dinh_xem_lai == 'giu'` chia tổng `review_decision_logged`).
- **Chỉ số an toàn đề xuất — Tỉ lệ hoàn tiền sai mức/trùng lệnh:** tính từ `refund_audit_mismatch` chia tổng `request_closed`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Tỉ lệ xem lại tăng gấp đôi (nhân viên mất tin tưởng hoặc phải kiểm tra nhiều hơn) | Chi phí mỗi việc thành công tăng ... đ (+...%) [simulated, lấy từ B1] | Tỉ lệ `review_decision_logged` vượt ngưỡng kế hoạch trong 3 ngày liên tiếp | Rà soát nhóm yêu cầu bị sửa/bỏ nhiều nhất, thu hẹp phạm vi hoặc kích hoạt luật dừng pilot | Operations Manager |
| Số ca làm lại tăng gấp đôi (chất lượng trả lời giảm sau khi đổi chính sách/bảng giá) | Chi phí mỗi việc thành công tăng ... đ (+...%) [simulated, lấy từ B1] | Tỉ lệ `request_reopened_7d` hoặc ca `lam_lai` tăng vượt ngưỡng tuần | Tạm dừng định tuyến tự động cho loại yêu cầu lỗi, cập nhật prompt/bảng giá và kiểm thử lại | AI Engineer |