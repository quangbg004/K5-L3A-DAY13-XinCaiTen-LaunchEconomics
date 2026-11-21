# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là **27,12%** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** |
| Dùng | Nhóm tự đề xuất: Tỉ lệ chấp nhận nguyên bản | Số yêu cầu có `quyet_dinh_xem_lai == 'giu'` chia tổng số yêu cầu được xem lại | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ hoàn tiền sai mức/trùng lệnh | Số yêu cầu phát sinh `refund_audit_mismatch` chia tổng số yêu cầu đã đóng | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_created` | Hệ thống CSKH | `request_id`, `created_at`, `staff_id`, `depot`, `loai`, `so_tien_vnd`, `pilot_arm`, `eligible_for_pilot`, `assistant_enabled`, `trace_id` | Khi tạo yêu cầu và đã định tuyến, trước khi trợ lý chạy |
| `agent_run_finished` | Trợ lý hoàn phí | `run_id`, `request_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls`, `trace_id` | Khi kết thúc mỗi lần chạy của agent |
| `review_decision_logged` | Giao diện nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `review_seconds`, `trace_id` | Khi nhân viên xem lại và chọn giữ/sửa/bỏ |
| `refund_rework_completed` | Giao diện nhân viên CSKH | `rework_id`, `request_id`, `staff_id`, `rework_seconds`, `trace_id` | Khi hoàn tất một lượt làm lại. Ghi thời gian thao tác, bỏ thời gian chờ |
| `request_closed` | Hệ thống CSKH | `request_id`, `dong_trong_24h`, `ket_qua`, `trace_id` | Khi yêu cầu được đóng và phản hồi khách |
| `request_reopened_7d` | Hệ thống CSKH | `request_id`, `days_since_close`, `reopen_reason`, `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |
| `refund_audit_mismatch` | Hệ thống đối soát/Sổ cái | `request_id`, `expected_vnd`, `actual_vnd`, `mismatch_type`, `trace_id` | Khi job đối soát phát hiện hoàn sai tiền hoặc trùng lệnh |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h & không mở lại 7 ngày):** tính từ `request_created`, `request_closed` (`dong_trong_24h == 1`) và loại trừ các `request_id` có `request_reopened_7d`.
- **Chỉ số dùng — Tỉ lệ bỏ qua gợi ý:** tính từ `review_decision_logged` (đếm `quyet_dinh_xem_lai` là `sua` hoặc `bo` chia tổng số event `review_decision_logged`).
- **Chỉ số an toàn — Tỉ lệ lỗi lọt đến khách:** tính từ `request_reopened_7d` chia tổng `request_created`.
- **Chỉ số dùng đề xuất — Tỉ lệ chấp nhận nguyên bản:** tính từ `review_decision_logged` (đếm `quyet_dinh_xem_lai == 'giu'` chia tổng `review_decision_logged`).
- **Chỉ số an toàn đề xuất — Tỉ lệ hoàn tiền sai mức/trùng lệnh:** tính từ `refund_audit_mismatch` chia tổng `request_closed`.

### Đo các ngưỡng dừng của pilot

- **Mức sử dụng 60%.** Trong cùng cửa sổ 7 ngày, lấy các yêu cầu có `pilot_arm = treatment`, `eligible_for_pilot = true` và `assistant_enabled = true` lúc định tuyến. Chia số yêu cầu có ít nhất một `agent_run_finished` cho tổng số yêu cầu đã lấy. Đếm mỗi `request_id` một lần. Xác định đủ điều kiện theo loại yêu cầu và depot trong kế hoạch.
- **CPS 8.000 đ.** Nối theo `request_id` trên nhóm yêu cầu đã đủ thời gian theo dõi của từng tuần. Cộng token và tool của mọi lần chạy, tiền thời gian từ `review_seconds` và `rework_seconds`, rồi chia số yêu cầu có `ket_qua = thanh_cong`. Đếm mỗi lượt làm lại một lần theo `rework_id` và dùng thời gian đo thực tế.
- **Mở lại trong 7 ngày.** So sánh trên các nhóm yêu cầu đã đủ thời gian theo dõi ở cả hai nhánh, đếm một lần theo `request_id`. Cảnh báo ca hoàn trùng ngay khi `refund_audit_mismatch` ghi nhận giao dịch trùng.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (chất lượng trả lời giảm sau khi đổi chính sách/bảng giá) | Chi phí mỗi việc thành công tăng từ 4.472 đ lên **6.787 đ** (+2.315 đ, tức **+51,8%**) [`simulated`] | Tỉ lệ `request_reopened_7d` hoặc ca `lam_lai` tăng vượt ngưỡng tuần trong 3 ngày liên tiếp | Tạm dừng định tuyến tự động cho loại yêu cầu lỗi, cập nhật bảng giá/prompt và kiểm thử lại trước khi mở lại | AI Engineer |
| Tỉ lệ xem lại tăng gấp đôi (nhân viên mất tin tưởng, kiểm tra nhiều hơn hoặc xem lại 100%) | Chi phí mỗi việc thành công tăng từ 4.472 đ lên **6.292 đ** (+1.820 đ, tức **+40,7%**) [`simulated`]; nếu xem lại 100% ở phạm vi `noi_dia` + `hang_nang`, CPS lên **11.743–12.415 đ** (0,98–1,03× mức 12.000 đ) [`simulated`] | Tỉ lệ `review_decision_logged` (đặc biệt `sua`/`bo`) vượt ngưỡng kế hoạch trong 3 ngày liên tiếp | Rà soát nhóm yêu cầu bị sửa/bỏ nhiều nhất, siết phạm vi pilot hoặc kích hoạt luật dừng pilot | Operations Manager |
| Lương nhân viên tăng 25% (từ 2.000 đ lên 2.500 đ/phút) | Chi phí mỗi việc thành công tăng từ 4.472 đ lên **5.506 đ** (+1.034 đ, tức **+23,1%**) [`simulated`] | Báo cáo chi phí nhân sự theo giờ từ bộ phận Vận hành/Tài chính hằng tháng | Ưu tiên giảm thời gian xem lại và số ca làm lại thay vì tối ưu giá token (vì giờ nhân viên chiếm 92,5% tổng chi phí [`simulated`]) | Finance / Ops Lead |
