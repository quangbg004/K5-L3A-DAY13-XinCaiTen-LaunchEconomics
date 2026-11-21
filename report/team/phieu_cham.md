# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): XinCaiTen (L3A)
- Nhóm được chấm: [3changngulam (L3A)](https://github.com/minhiuss/K5-L3A-DAY13-3changngulam-LaunchEconomics)
- Bản được chấm: nhánh `main`, commit [`d1b2e6f`](https://github.com/minhiuss/K5-L3A-DAY13-3changngulam-LaunchEconomics/commit/d1b2e6ffca9d7d4e21e59890f84e7b22a831920f).
- Trạng thái: đã ghi điểm và phản hồi của đội trình.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Nhận xét từ hồ sơ |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | [Hồ sơ launch v0](https://github.com/minhiuss/K5-L3A-DAY13-3changngulam-LaunchEconomics/blob/d1b2e6ffca9d7d4e21e59890f84e7b22a831920f/report/team/ho_so_launch_v0.md) chọn Go có điều kiện và đặt mục tiêu thời gian xem lại trung bình ≤ 4,8 phút/ca. [Bảng chi phí](https://github.com/minhiuss/K5-L3A-DAY13-3changngulam-LaunchEconomics/blob/d1b2e6ffca9d7d4e21e59890f84e7b22a831920f/report/team/bang_chi_phi.md) nêu lý do của điều kiện này: xem lại 100% có thể đẩy CPS lên 12.415 đ (`simulated`), vượt mức 12.000 đ của nhân viên. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Bảng chi phí ghi nhãn `simulated` cho CPS. Pilot giới hạn ở `noi_dia` và `hang_nang`, lần lượt 2.696 đ và 8.221 đ/việc (`simulated`). Loại `quoc_te` vì 22.515 đ/việc (`simulated`), bằng 1,88 lần mốc 12.000 đ. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | [Kế hoạch pilot](https://github.com/minhiuss/K5-L3A-DAY13-3changngulam-LaunchEconomics/blob/d1b2e6ffca9d7d4e21e59890f84e7b22a831920f/report/team/pilot_plan.yaml) có đối chứng đồng thời, 20 nhân viên/nhóm và 299 yêu cầu/người, đủ theo giả định chênh lệch 6 điểm. Mục loại người đối chứng sau phân nhóm nếu họ mở trợ lý có thể gây thiên lệch. Cần giữ nhóm theo phân bổ ban đầu trong phân tích chính và cập nhật YAML theo phản hồi của đội trình về việc dừng trong vòng 30 phút kể từ khi phát hiện ca hoàn trùng đầu tiên. |
| **Tổng** | | | | **30 / 30** | Điểm do nhóm chấm chọn. |

**Quyết định đề xuất:** Go có điều kiện.

**Điều kiện trước khi bật pilot:** Kiểm tra có thể giữ thời gian xem lại trung bình ở mức ≤ 4,8 phút/ca. Giữ người tham gia theo nhóm phân bổ ban đầu trong phân tích chính và cập nhật luật dừng khi phát hiện ca hoàn tiền trùng đầu tiên theo phản hồi dưới đây.

**Câu hỏi cho đội trình:** Khi phát hiện ca hoàn tiền trùng đầu tiên, Giám đốc vận hành sẽ tắt trợ lý trong 30 phút kể từ lúc phát hiện hay chờ hết cửa sổ 3 ngày?

**Câu trả lời của đội trình:** Tắt ngay trong vòng 30 phút kể từ khi đối soát mỗi giờ phát hiện ca hoàn trùng đầu tiên (ngưỡng = 0 ca, không chờ hết 3 ngày). Trong report/team/pilot_plan.yaml, cửa sổ "3 ngày liên tiếp" áp dụng cho biến động tỉ lệ thống kê (mở lại 7 ngày cao hơn đối chứng ≥ 2 điểm hoặc vượt 6%) để tránh nhiễu mẫu nhỏ theo ngày, còn ≥ 1 ca hoàn tiền trùng là sự cố thất thoát tài chính trực tiếp (lỗi hệ thống ca 20) được đối soát mỗi giờ qua event refund_ledger_write (report/team/bang_loi.md). Để không còn bất kỳ cách hiểu nước đôi nào do gộp chung câu lệnh NẾU ... TRONG 3 ngày liên tiếp, nhóm cam kết tách vế hoàn trùng thành điều kiện kích hoạt tức thời: NẾU có ≥ 1 ca hoàn tiền trùng TRONG bất kỳ kỳ đối soát 1 giờ nào THÌ Giám đốc vận hành tắt trợ lý trong 30 phút.
