from vnstock3 import Vnstock  # Nạp thư viện để sử dụng

code = "SHB"
stock = Vnstock().stock(source="TCBS")

df = stock.trading.price_board(symbols_list=[code])
print(df.head())  # Hiển thị 5 dòng dữ liệu đầu tiên
df.to_excel("vietnam_stock_realtime_price_of_" + code + ".xlsx", index=False)  # Lưu file Excel