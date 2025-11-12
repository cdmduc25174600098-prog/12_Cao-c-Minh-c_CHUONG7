# Nhập giá sản phẩm và số lượng mua
gia_san_pham = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))

# Tính tổng chi phí
tong_chi_phi = gia_san_pham * so_luong

# Tính thuế VAT 10%
thue_vat = tong_chi_phi * 0.10

# Tính tổng tiền phải trả
tong_tien_phai_tra = tong_chi_phi + thue_vat

# In kết quả, làm tròn đến 2 chữ số thập phân
print(f"Tổng tiền phải trả (đã bao gồm VAT): {round(tong_tien_phai_tra, 2)} VND")