from vnstock3 import Vnstock  # Nạp thư viện để sử dụng

stock = Vnstock().stock(
    symbol="ACB", source="TCBS"
)  # Định nghĩa biến vnstock lưu thông tin mã chứng khoán & nguồn dữ liệu bạn sử dụng
# CÁC DÒNG LỆNH DƯỚI ĐÂY CÓ THỂ THAY THẾ CHO PHÙ HỢP, THAM KHẢO THÊM HÀM KHÁC
df = stock.quote.history(
    start="2023-01-01", end="2024-12-31", interval="1D"
)  # Thiết lập thời gian tải dữ liệu và khung thời gian tra cứu là 1 ngày
print(df.head())  # Hiển thị 5 dòng dữ liệu đầu tiên
df.to_excel("gia_lich_su_ohlcv_ACB.xlsx", index=False)  # Lưu file Excel
