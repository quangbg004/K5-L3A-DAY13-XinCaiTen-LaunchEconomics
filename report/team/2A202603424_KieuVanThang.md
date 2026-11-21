# Báo cáo cá nhân — KieuVanThang-2A202603424

## 1. Thông tin thành viên

- Họ tên: Kiều Văn Thắng
- MSSV: 2A202603424
- Email: 26ai.thangkv@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 1 (CP3), lập bảng chỉ số (CP5) và theo dõi điều kiện hoàn thành theo `CHECKPOINTS.md`

## 2. Phần việc phụ trách

- Theo dõi tiến độ và điều kiện "Xong khi" của cả nhóm qua 5 checkpoint trong `CHECKPOINTS.md`.
- **CP3 (Nhiệm vụ C):** Tự gắn nhãn độc lập lượt 1 cho 20 ca lỗi theo 5 loại của Google PAIR, lưu riêng trước khi so với người gắn nhãn 2; tổng hợp hai bộ nhãn vào `report/team/bang_loi.md`, tính tỉ lệ đồng thuận, viết quy tắc xử lý bất đồng và cùng người gắn nhãn 2 hoàn thiện bảng khắc phục 5 ca.
- **CP5 (Nhiệm vụ E1, E2):** Hoàn thiện `report/team/chi_so.md` gồm 3 chỉ số tính thử, 1 chỉ số sử dụng và 1 chỉ số an toàn đề xuất thêm, danh sách ít nhất 6 event có `trace_id` (kèm kiểm tra chéo), và ít nhất 2 dòng rủi ro kinh tế lấy số từ bảng độ nhạy CP2; gửi kết quả cho người giữ hồ sơ trước 17:00.

## 3. Đóng góp cụ thể

- Hoàn thành bộ nhãn độc lập lượt 1 cho 20 ca lỗi theo nguyên nhân gốc (không sửa lại bộ nhãn gốc sau khi so).
- Tổng hợp bảng so sánh hai bộ nhãn vào `report/team/bang_loi.md`, tính tỉ lệ đồng thuận đạt [20/20 = 100%], thống nhất nhãn và ghi quy tắc phân biệt cho các ca không trùng.
- Cùng người gắn nhãn 2 xây dựng bảng khắc phục 5 ca (đủ 5 loại: Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống, Ngầm), đảm bảo mỗi ca có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách cụ thể.
- Hoàn thiện `report/team/chi_so.md`: điền kết quả tính thử 3 chỉ số trên 1.200 yêu cầu, đề xuất thêm chỉ số sử dụng (*Tỉ lệ chấp nhận nguyên bản*) và chỉ số an toàn (*Tỉ lệ hoàn tiền sai mức/trùng lệnh*), thiết kế 6 event có `trace_id` kèm kiểm tra chéo công thức, và bổ sung 2 dòng rủi ro kinh tế dựa trên bảng độ nhạy CP2.
- Rà soát checklist nộp bài của nhóm (nhãn `simulated`, không dùng từ bị cấm, đủ file đúng tên).

## 4. Bằng chứng

- File `report/team/bang_loi.md`: cột `Nhãn người 1`, tỉ lệ đồng thuận, mục quy tắc phân biệt và bảng khắc phục 5 ca.
- File `report/team/chi_so.md`: bảng đặc tả chỉ số E1, bảng 6 event có `trace_id`, mục kiểm tra chéo và bảng rủi ro kinh tế E2.
- Commit chốt: `[điền mã commit sau khi push lên GitHub]`

## 5. Công cụ AI đã dùng

- **Công cụ:** Gemini.
- **Mục đích sử dụng:** Tóm tắt yêu cầu bài lab; gợi ý phân tích nguyên nhân gốc cho 20 ca lỗi theo khung Google PAIR; gợi ý cấu trúc bảng khắc phục, chỉ số đề xuất thêm và danh sách 6 event có `trace_id`; hỗ trợ rà soát định dạng file báo cáo.
- **Cách tự kiểm tra:**
  - Tự đọc và đối chiếu trực tiếp từng ca lỗi với đề bài gốc (`docs/Ngay13_Lab13_De_bai_hoc_vien.docx`) và 5 định nghĩa của Google PAIR trước khi chốt nhãn độc lập.
  - Kiểm tra chéo từng chỉ số trong bảng E1 với danh sách 6 event để đảm bảo mọi chỉ số đều đo được và có `trace_id`.
  - Mọi con số tính thử và rủi ro kinh tế đều lấy từ kết quả chạy `src/lab13.py` của nhóm, không dùng AI bịa số hay kết quả duyệt chéo.
  - Kiểm tra đúng quy tắc đặt nhãn `simulated` và không dùng từ cấm trong hồ sơ.

## 6. Tự đánh giá

- Hoàn thành đúng vai trò được phân công, giữ đúng nguyên tắc gắn nhãn độc lập ở CP3 và bàn giao bảng chỉ số/rủi ro kịp mốc cho người giữ hồ sơ.
- Đảm bảo tính nhất quán giữa bảng chỉ số, danh sách event và số liệu độ nhạy từ CP2.
- Điểm cần lưu ý thêm: chủ động đối chiếu sớm số liệu từ `src/lab13.py` với người viết code để giảm thời gian chờ ở bước ghép hồ sơ cuối buổi.