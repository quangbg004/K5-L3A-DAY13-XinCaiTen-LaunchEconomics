# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Bảng ghi nhãn CP3

Người gắn nhãn 1: Thắng · Người gắn nhãn 2: Nguyễn Tuấn Quang.

Mỗi người đọc mục “Hai mươi ca lỗi” trong [đề bài](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), dành 8 phút để ghi đủ 20 nhãn vào bản riêng. Chỉ nhập hai bộ nhãn gốc vào bảng chung sau khi cả hai đã chốt. Ghi kết quả đối chiếu ở cột “Trùng?” và “Nhãn thống nhất”.

Cột “Nhãn người 2” hiện chứa 20 nhãn do Codex điền theo tài liệu hướng dẫn. Quang cần xác nhận và cung cấp bản tự chốt trước khi dùng cột này để báo cáo mức đồng thuận độc lập.


| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ trùng giữa nhãn của Thắng và bộ nhãn tham khảo:** 20/20 = 100%.

## Quy tắc phân biệt cho các ca không trùng

Hai bộ nhãn hiện trùng ở cả 20 ca.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Các tín hiệu, ngưỡng và biện pháp dưới đây là đề xuất cho pilot.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Kiểm tra định dạng và độ dài số tài khoản theo ngân hàng mỗi lần gửi. Ghi `refund_input_invalid` nếu không đạt. | Chặn tạo lệnh hoàn, chỉ rõ ô cần sửa và kiểm tra lại khi khách gửi lại. | Chủ luồng nhập yêu cầu hoàn phí |
| 7 | Hệ thống | Cảnh báo ngay nếu phản hồi báo hoàn thành công mà sổ cái chưa xác nhận ghi tiền. Nối hai sự kiện theo `trace_id` và mã lệnh hoàn. | Chỉ gửi thông báo thành công sau khi sổ cái xác nhận. Nếu vẫn gặp 503 sau 3 lần thử, ghi trạng thái chờ đối soát và chuyển nhân viên tiếp nhận. | Kỹ sư phụ trách tích hợp sổ cái |
| 18 | Ngữ cảnh | Hằng tuần, đếm `request_reopened_7d` có lý do “hoàn thiếu” trong số yêu cầu đã đối chiếu và xác nhận hoàn đúng tiền. | Hiển thị phí gốc, tỉ lệ hoàn và phép tính ngay trong tin nhắn, ví dụ 30.000 đ × 50% = 15.000 đ. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Với mỗi yêu cầu, kiểm tra ngày đơn trước khi tra cứu. Ghi `refund_lookup_out_of_range` nếu ngày đơn nằm ngoài cửa sổ dữ liệu 12 tháng. | Giải thích giới hạn tra cứu cho khách và chuyển nhân viên có quyền tra hồ sơ lưu trữ, kèm mã đơn, ngày đơn và lý do chuyển. | Trưởng ca xử lý hoàn phí |
| 17 | Ngầm | Hằng ngày, tính lại mức hoàn của các đơn dưới 2 kg theo phiên bản bảng giá có hiệu lực cho từng đơn. Ghi `refund_audit_mismatch` và cảnh báo khi có ít nhất 1 khoản chênh lệch. | Vô hiệu hóa bộ nhớ đệm khi bảng giá đổi, lưu phiên bản bảng giá cho từng lệnh hoàn và rà soát lại các đơn đã dùng bản cũ để xử lý chênh lệch. | Kỹ sư phụ trách dịch vụ bảng giá |
