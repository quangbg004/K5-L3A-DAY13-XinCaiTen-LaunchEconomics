# Bảng chi phí · Nhiệm vụ A và B

Số được tính lại từ `src/logix_runs.csv` và `src/logix_requests.csv` theo mô hình trong `src/lab13.py`. Các khoản tính từ cột `_simulated` đều được ghi nhãn **simulated**. Đơn vị tiền: VND.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | **1,20** |
| Số lần chạy trung bình, chạy đến khi đúng | **1,25** |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | **1,25** |

## A2 · Mô hình chi phí từ trace (1.200 yêu cầu, 1.624 lần chạy)

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | **245.585** | `logix_runs.csv`, mọi lần chạy | đo từ trace |
| Tool | **84.000** | `logix_runs.csv`, mọi lần chạy | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | **93.804** | `attempt > 1`, gồm token + tool | đo từ trace |
| Xem lại | **1.780.000** | 890 phút × 2.000 đ/phút | simulated |
| Làm lại | **2.264.000** | 1.132 phút × 2.000 đ/phút | simulated |
| **Tổng chi phí** | **4.373.585** | token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | **978** | `ket_qua == 'thanh_cong'` | đo từ trace |
| **Chi phí mỗi việc thành công (CPS)** | **4.472** | 4.373.585 / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | **274,65** | (245.585 + 84.000) / 1.200 | đo từ trace |

- CPS **4.472 đ**, gấp **16,28 lần** hoá đơn token + tool chia cho số yêu cầu (**274,65 đ**). Chênh lệch chủ yếu do thời gian nhân viên, không phải token.
- Khoản lớn nhất là **làm lại: 2.264.000 đ (51,8%)**; tiếp theo xem lại **1.780.000 đ (40,7%)**. Hai khoản nhân công chiếm khoảng **92,5%** tổng CPS.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | CPS (đ) | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | **95,0%** | 1,11 | **2.696** | **0,22×** |
| hang_nang | 158 | **74,1%** | 1,47 | **8.221** | **0,69×** |
| quoc_te | 150 | **27,3%** | 2,32 | **22.515** | **1,88×** |
| doi_tac | 68 | **54,4%** | 1,88 | **10.215** | **0,85×** |

- **quoc_te** không nên đưa vào pilot: CPS **22.515 đ**, bằng **1,88×** chi phí nhân viên tự làm. Tỉ lệ `status=ok` giảm từ **30,0%** ở lần 1 xuống **11,4%** ở lần 2 và **2,2%** ở lần 3 (2/93 lần chạy); chạy lại đến 3 lần không giải quyết được vấn đề.
- Đề xuất phạm vi pilot ban đầu: `noi_dia` + `hang_nang`; theo dõi riêng `hang_nang` vì tỉ lệ thành công thấp hơn nội địa (**74,1%** so với **95,0%**).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Trong mẫu có **982** yêu cầu thuộc phạm vi, **900** việc thành công. Quy đổi theo giả định 45.000 yêu cầu/tháng: 45.000 × 900 / 1.200 = **33.750 việc thành công/tháng**.

| Khối lượng | Việc thành công/tháng | Chi phí cố định/việc | CPS biến đổi + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | **1.185 đ** | **4.599 đ** | **0,38×** |
| Một nửa khối lượng | 16.875 | **2.370 đ** | **5.784 đ** | **0,48×** |

- Chi phí cố định **không đổi kết luận** ở hai mức khối lượng đã xét: CPS lần lượt **4.599 đ** và **5.784 đ**, đều thấp hơn baseline **12.000 đ**. Tuy nhiên, đây là ước tính **simulated**, phụ thuộc giả định sản lượng và tỷ lệ thành công giữ nguyên.

## B1 · Đổi từng yếu tố

CPS gốc dùng làm mốc: **4.472 đ**. Các giá trị dưới đây được làm tròn đến đồng; toàn bộ CPS chứa phút nhân viên `_simulated`.

| Kịch bản | Cách tính | CPS (đ) | Thay đổi |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ/1.000 token; tool giữ nguyên | **4.723** | **+5,6%** |
| Giá token giảm một nửa | 13 đ và 65 đ/1.000 token | **4.346** | **−2,8%** |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | **6.292** | **+40,7%** |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | **3.562** | **−20,3%** |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | **6.787** | **+51,8%** |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | **3.315** | **−25,9%** |
| Lương nhân viên tăng 25% | 2.500 đ/phút | **5.506** | **+23,1%** |
| Chỉ cho chạy tối đa 2 lần | Bỏ attempt > 2; ca vượt giới hạn chuyển nhân viên | **4.237** | **−5,2%** |
| Chỉ cho chạy 1 lần | Bỏ attempt > 1; ca vượt giới hạn chuyển nhân viên | **4.111** | **−8,1%** |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: CPS **6.543 đ**, tăng **46,3%**. Mức tăng bằng tổng tác động riêng: **5,6% + 40,7% = 46,3%**, do mô hình cộng tuyến tính theo từng khoản chi phí.
- Ba yếu tố nhạy nhất: **1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%)**. Giá token chỉ làm CPS tăng **5,6%** khi tăng gấp đôi.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (đ) | Số yêu cầu không thành công | Chi phí cả hệ thống (đ) | CPS trợ lý (đ) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | **3.621.781** | **319** | **7.449.781** | **4.111** |
| 2 lần | **4.093.220** | **234** | **6.901.220** | **4.237** |
| 3 lần | **4.373.585** | **222** | **7.037.585** | **4.472** |

- Giới hạn **2 lần** rẻ nhất cho công ty: **6.901.220 đ**. Không trùng với CPS thấp nhất: giới hạn **1 lần** có CPS **4.111 đ**, nhưng để lại **319** yêu cầu cho nhân viên; giới hạn 2 lần giảm số yêu cầu không thành công xuống **234** và giảm tổng chi phí hệ thống.

## B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang)

- Có **948** yêu cầu trong phạm vi có ít nhất một lần `status=ok`; xem lại 100% × 5 phút × 2.000 đ = **9.480.000 đ**. Token + tool **224.513 đ**. Có **48** ca làm lại; trung bình toàn bộ **74** ca làm lại trong dữ liệu là **15,297 phút/ca (simulated)**, nên chi phí làm lại trong pilot là **1.468.541 đ (simulated)**.
- Tổng **11.173.054 đ / 900 việc thành công = 12.415 đ/việc (simulated)**, xấp xỉ **1,03×** baseline 12.000 đ. Xem lại 100% làm mất lợi thế chi phí; pilot phải đo cách giảm tỷ lệ xem lại an toàn, không chỉ đo token.

## Phép tính đối chiếu độc lập của Bảo

- A2: CPS = (245.585,132 + 84.000 + 1.780.000 + 2.264.000) / 978 = **4.471,97 đ**, làm tròn **4.472 đ**.
- D1-e: với 20 nhân viên mỗi nhóm và ICC = 0,02, giải `20m / (1 + (m − 1) × 0,02) ≥ 859`; suy ra `2,82m ≥ 841,82`, nên **m ≥ 299 yêu cầu/nhân viên**. Design effect = **6,96**, cỡ mẫu hiệu dụng xấp xỉ **859/nhóm**.
