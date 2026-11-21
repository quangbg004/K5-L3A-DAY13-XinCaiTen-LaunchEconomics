"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
Thành viên thực hiện CP1–CP2: Nguyễn Thế Trường (2A202603393).
"""
import math
import statistics
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000  # đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1.0 / p
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    cps = tong / thanh_cong if thanh_cong > 0 else 0.0
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs) if len(reqs) > 0 else 0.0

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=cps,
        hoa_don_moi_yc=hoa_don_moi_yc
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu (Sẵn sàng bàn giao cho Bảo CP4) ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Tính cỡ mẫu mỗi nhóm khi so hai tỉ lệ độc lập."""
    za = statistics.NormalDist().inv_cdf(1.0 - alpha / 2.0)
    zb = statistics.NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2.0
    tu = (za * math.sqrt(2.0 * pb * (1.0 - pb)) + zb * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))) ** 2
    mau = (p2 - p1) ** 2
    return math.ceil(tu / mau)


if __name__ == '__main__':
    # 1. Đọc dữ liệu (Bắt buộc keep_default_na=False)
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print('=' * 70)
    print('LAB 13: ĐỊNH GIÁ AGENT VÀ LẬP KẾ HOẠCH PILOT (GATE 2a)')
    print('Người thực hiện CP1–CP2: Nguyễn Thế Trường (2A202603393)')
    print('=' * 70)

    # -------------------------------------------------------------
    # CP1 · A1: Kiểm tra đáp án biết trước
    # -------------------------------------------------------------
    print('\n[CP1 · A1] KIỂM TRA ĐÁP ÁN BIẾT TRƯỚC:')
    kiem_tra_dap_an_biet_truoc()

    # -------------------------------------------------------------
    # CP1 · A2: Mô hình chi phí từ trace
    # -------------------------------------------------------------
    print('\n[CP1 · A2] BẢNG CHI PHÍ TỔNG THỂ (1.200 YÊU CẦU):')
    ket_qua = mo_hinh(runs, reqs)
    labels = {
        'token': 'Token (mọi lần chạy) [đo từ trace]',
        'tool': 'Tool (5.600 lần gọi) [đo từ trace]',
        'chay_lai': 'Trong đó, lần chạy 2 & 3 [đo từ trace]',
        'xem_lai': 'Xem lại (890 phút) [simulated]',
        'lam_lai': 'Làm lại (1.132 phút) [simulated]',
        'tong': 'Tổng chi phí [có phần simulated]',
        'thanh_cong': 'Số việc thành công',
        'cps': 'Chi phí mỗi việc thành công [simulated]',
        'hoa_don_moi_yc': 'Hoá đơn token+tool / yêu cầu [đo từ trace]'
    }
    for ten, gia_tri in ket_qua.items():
        ten_in = labels.get(ten, ten)
        if ten == 'thanh_cong':
            print(f'  - {ten_in:45s}: {gia_tri:>12,d}')
        elif ten in ['cps', 'hoa_don_moi_yc']:
            print(f'  - {ten_in:45s}: {gia_tri:>12,.1f} đ')
        else:
            print(f'  - {ten_in:45s}: {gia_tri:>12,.0f} đ')

    boi_so = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    pct_lam_lai = ket_qua['lam_lai'] / ket_qua['tong'] * 100
    pct_xem_lai = ket_qua['xem_lai'] / ket_qua['tong'] * 100
    pct_nhan_vien = (ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong'] * 100
    print(f"\n  => Đánh giá: CPS ({ket_qua['cps']:,.0f} đ) gấp {boi_so:.1f} lần hóa đơn token+tool ({ket_qua['hoa_don_moi_yc']:,.1f} đ).")
    print(f"  => Giờ nhân viên chiếm {pct_nhan_vien:.1f}% tổng chi phí (Làm lại: {pct_lam_lai:.1f}%, Xem lại: {pct_xem_lai:.1f}%).")

    # -------------------------------------------------------------
    # CP1 · A3: Tách theo từng loại yêu cầu
    # -------------------------------------------------------------
    print('\n[CP1 · A3] BẢNG THEO TỪNG LOẠI YÊU CẦU:')
    print(f"{'Loại':12s} | {'Số YC':>7s} | {'Tỉ lệ TC':>9s} | {'Lần/YC':>8s} | {'CPS [sim]':>11s} | {'So 12.000đ':>10s}")
    print('-' * 70)
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r_l = reqs[reqs['loai'] == loai]
        res_l = mo_hinh(runs, r_l)
        so_yc = len(r_l)
        ti_le_tc = res_l['thanh_cong'] / so_yc * 100
        runs_l = runs[runs['request_id'].isin(r_l['request_id'])]
        lan_yc = len(runs_l) / so_yc
        cps_l = res_l['cps']
        so_sanh = cps_l / BASELINE
        print(f"{loai:12s} | {so_yc:>7d} | {ti_le_tc:>8.1f}% | {lan_yc:>8.2f} | {cps_l:>9,.0f} đ | {so_sanh:>9.2f}×")

    # Tỉ lệ thành công theo từng lần thử
    df_merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    df_merged['is_ok'] = (df_merged['status'] == 'ok').astype(float)
    pivot_attempt = df_merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print('\n  * Tỉ lệ status == ok theo lần thử (attempt 1, 2, 3):')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        row = pivot_attempt.loc[loai]
        print(f"    - {loai:10s}: lần 1 = {row.get(1, 0):.1f}%, lần 2 = {row.get(2, 0):.1f}%, lần 3 = {row.get(3, 0):.1f}%")

    # -------------------------------------------------------------
    # CP1 · A4: Chi phí cố định
    # -------------------------------------------------------------
    print('\n[CP1 · A4] CHI PHÍ CỐ ĐỊNH (40 TRIỆU Đ/THÁNG) TRONG PHẠM VI PILOT (noi_dia + hang_nang):')
    scope_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    res_scope = mo_hinh(runs, scope_reqs)
    tc_scope = res_scope['thanh_cong']  # 900
    tc_thang_full = 45000 * (tc_scope / len(reqs))  # 33.750
    co_dinh_moi_viec_full = CO_DINH_THANG / tc_thang_full  # 1.185 đ
    cps_bien_doi_scope = res_scope['cps']  # 3.414 đ
    cps_tong_full = cps_bien_doi_scope + co_dinh_moi_viec_full  # 4.599 đ

    # Kịch bản khối lượng giảm một nửa
    tc_thang_half = tc_thang_full / 2.0  # 16.875
    co_dinh_moi_viec_half = CO_DINH_THANG / tc_thang_half  # 2.370 đ
    cps_tong_half = cps_bien_doi_scope + co_dinh_moi_viec_half  # 5.784 đ

    print(f"  - Số việc thành công trong mẫu: {tc_scope}/{len(reqs)} -> Quy mô đầy đủ: {tc_thang_full:,.0f} việc/tháng")
    print(f"  - Chi phí biến đổi trong phạm vi: {cps_bien_doi_scope:,.0f} đ [simulated]")
    print(f"  - Ở quy mô 45.000 yc/tháng: Cố định = {co_dinh_moi_viec_full:,.0f} đ -> Tổng CPS = {cps_tong_full:,.0f} đ ({cps_tong_full / BASELINE:.2f}× baseline) [simulated]")
    print(f"  - Ở quy mô giảm 50% (pilot): Cố định = {co_dinh_moi_viec_half:,.0f} đ -> Tổng CPS = {cps_tong_half:,.0f} đ ({cps_tong_half / BASELINE:.2f}× baseline) [simulated]")

    # -------------------------------------------------------------
    # CP2 · B1: Bảng độ nhạy (9 kịch bản)
    # -------------------------------------------------------------
    print('\n' + '=' * 70)
    print('[CP2 · B1] BẢNG ĐỘ NHẠY (9 KỊCH BẢN):')
    goc_cps = ket_qua['cps']
    kich_ban = {
        'Gốc (A2)':                 dict(),
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2.0),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2.0),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }

    print(f"{'Kịch bản':30s} | {'CPS [sim]':>11s} | {'Thay đổi':>9s}")
    print('-' * 56)
    for ten, kw in kich_ban.items():
        cps_kb = mo_hinh(runs, reqs, **kw)['cps']
        diff_pct = (cps_kb / goc_cps - 1.0) * 100.0
        if ten == 'Gốc (A2)':
            print(f"{ten:30s} | {cps_kb:>9,.0f} đ | {'':>9s}")
        else:
            print(f"{ten:30s} | {cps_kb:>9,.0f} đ | {diff_pct:>+8.1f}%")

    # -------------------------------------------------------------
    # CP2 · B2: Đổi một cặp và xếp hạng
    # -------------------------------------------------------------
    print('\n[CP2 · B2] ĐỔI MỘT CẶP YẾU TỐ VÀ XẾP HẠNG:')
    res_pair = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    cps_pair = res_pair['cps']
    diff_pair = (cps_pair / goc_cps - 1.0) * 100.0
    print(f"  - Giá token x2 + Xem lại x2: {cps_pair:,.0f} đ ({diff_pair:+0.1f}%) [simulated]")
    print("  - Tổng hai tác động riêng rẽ: +5.6% (token x2) + 40.7% (xem lại x2) = +46.3% -> Khớp hoàn toàn (tuyến tính).")
    print("  - Xếp hạng 3 yếu tố nhạy nhất: 1. Số ca làm lại (+51.8%) | 2. Tỉ lệ xem lại (+40.7%) | 3. Lương nhân viên (+23.1%).")

    # -------------------------------------------------------------
    # CP2 · B3: Giới hạn số lần chạy và chi phí cả hệ thống
    # -------------------------------------------------------------
    print('\n[CP2 · B3] GIỚI HẠN SỐ LẦN CHẠY VÀ CHI PHÍ CẢ HỆ THỐNG:')
    print(f"{'Giới hạn':10s} | {'Tổng trợ lý [sim]':>18s} | {'Không TC':>9s} | {'Cả hệ thống [sim]':>18s} | {'CPS [sim]':>11s}")
    print('-' * 75)
    for k in [1, 2, 3]:
        res_k = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - res_k['thanh_cong']
        chi_phi_nv = khong_tc * BASELINE
        ca_he_thong = res_k['tong'] + chi_phi_nv
        ghi_chu = ""
        if k == 1:
            ghi_chu = " (CPS thấp nhất)"
        elif k == 2:
            ghi_chu = " (Hệ thống RẺ NHẤT)"
        print(f"Tối đa {k} lần | {res_k['tong']:>16,.0f} đ | {khong_tc:>9d} | {ca_he_thong:>16,.0f} đ | {res_k['cps']:>9,.0f} đ{ghi_chu}")

    # -------------------------------------------------------------
    # CP2 · B4: Nếu phải xem lại 100% (noi_dia + hang_nang)
    # -------------------------------------------------------------
    print('\n[CP2 · B4] KỊCH BẢN XEM LẠI 100% (noi_dia + hang_nang):')
    reqs_p = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    runs_p = runs[runs['request_id'].isin(reqs_p['request_id'])].copy()

    # 1. Đếm yêu cầu có ít nhất một lần chạy status == 'ok'
    ok_req_ids = runs_p[runs_p['status'] == 'ok']['request_id'].unique()
    so_yc_ok = len(ok_req_ids)  # 948
    tien_xem_lai_100 = so_yc_ok * 5 * LUONG_PHUT  # 5 phút/lần

    # 2. Đếm ca lam_lai trong phạm vi
    ca_lam_lai = (reqs_p['ket_qua'] == 'lam_lai').sum()  # 48 ca
    tien_lam_lai_9m = ca_lam_lai * 9 * LUONG_PHUT  # 9 phút/ca (đề bài cho)
    # Trung bình phút làm lại thực tế trên toàn bộ ca lam_lai (tài liệu ghi 15,3 phút)
    tb_phut_lam_lai_that = reqs[reqs['ket_qua'] == 'lam_lai']['phut_lam_lai_simulated'].mean()
    tien_lam_lai_real = ca_lam_lai * tb_phut_lam_lai_that * LUONG_PHUT

    # 3. Token + tool
    tien_token_tool_p = (runs_p['tokens_in'] / 1000.0 * GIA_VAO +
                         runs_p['tokens_out'] / 1000.0 * GIA_RA +
                         runs_p['tool_calls'] * GIA_TOOL).sum()

    # 4. Thành công & CPS
    tc_p = (reqs_p['ket_qua'] == 'thanh_cong').sum()  # 900
    tong_9m = tien_token_tool_p + tien_xem_lai_100 + tien_lam_lai_9m
    cps_9m = tong_9m / tc_p

    tong_real = tien_token_tool_p + tien_xem_lai_100 + tien_lam_lai_real
    cps_real = tong_real / tc_p

    print(f"  - Yêu cầu có status=ok: {so_yc_ok} đơn × 5 phút = {tien_xem_lai_100:,.0f} đ")
    print(f"  - Token + Tool: {tien_token_tool_p:,.0f} đ")
    print(f"  - Trường hợp làm lại 9 phút ({ca_lam_lai} ca): Tổng = {tong_9m:,.0f} đ -> CPS = {cps_9m:,.0f} đ ({cps_9m / BASELINE:.2f}× baseline) [simulated]")
    print(f"  - Trường hợp làm lại 15,3 phút (theo dữ liệu thực): Tổng = {tong_real:,.0f} đ -> CPS = {cps_real:,.0f} đ ({cps_real / BASELINE:.2f}× baseline) [simulated]")

    # -------------------------------------------------------------
    # CP4 · D1: Cỡ mẫu (Sẵn sàng bàn giao cho Bảo)
    # -------------------------------------------------------------
    print('\n' + '=' * 70)
    print('[CP4 · D1] TÍNH TOÁN CỠ MẪU (SẴN SÀNG BÀN GIAO CHO BẢO):')
    n_a = co_mau(0.70, 0.75)
    de_b = 1.0 + (75 - 1) * 0.02
    n_b = math.ceil(n_a * de_b)
    nguoi_b = math.ceil(n_b / 75)
    gioi_han_c = math.floor(20 / 0.02)
    gioi_han_d = math.floor(6 / 0.02)
    n_e = co_mau(0.70, 0.76)  # 859
    # Giải m cho câu e: 20m / (1 + (m-1)*0.02) >= 859 -> 20m >= 859 * (0.98 + 0.02m) -> (20 - 17.18)m >= 841.82 -> 2.82m >= 841.82 -> m >= 298.5 -> 299
    m_e = math.ceil((859 * 0.98) / (20 - 859 * 0.02))

    print(f"  - Câu a (Chia theo yêu cầu, delta=5%): {n_a} yêu cầu mỗi nhóm")
    print(f"  - Câu b (Theo nhân viên m=75, DE={de_b:.2f}): {n_b} yêu cầu/nhóm -> {nguoi_b} người/nhóm (tổng {nguoi_b * 2} > 40: KHÔNG ĐỦ)")
    print(f"  - Câu c (20 nhân viên mỗi nhóm, giới hạn c/ICC): tối đa {gioi_han_c} < {n_a} (KHÔNG ĐẠT)")
    print(f"  - Câu d (6 depot mỗi nhóm, giới hạn c/ICC): tối đa {gioi_han_d}")
    print(f"  - Câu e (Chênh 6 điểm, n={n_e}, 20 người/nhóm): m ≥ {m_e} yêu cầu/người (DE = {1 + (m_e - 1) * 0.02:.2f})")
    print('=' * 70)
