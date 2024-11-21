from vnstock3 import Vnstock

stock = Vnstock().stock(source="VCI")

# 1. lấy tất cả mã chứng khoán từ VCI
stock_code_list = stock.listing.all_symbols()
stock_code_list.to_excel("data/xlsx/vietnam_stock_code_list/1_vietnam_stock_all_code_data.xlsx", index=False)  # Lưu file Excel
stock_code_list.to_csv('data/csv/vietnam_stock_code_list/1_vietnam_stock_all_code_data.csv', header=True, index=True)
print("1. Đã lấy tất cả Mã chứng khoán từ VCI")

# 2. Danh sách mã chứng khoán theo ngành ICB
stock_code_list = stock.listing.symbols_by_industries()
stock_code_list.to_excel("data/xlsx/vietnam_stock_code_list/2_vietnam_stock_all_code_industries_icb_data.xlsx", index=False)  # Lưu file Excel
stock_code_list.to_csv('data/csv/vietnam_stock_code_list/2_vietnam_stock_all_code_industries_icb_data.csv', header=True, index=True)
print("2. Đã lấy Danh sách mã chứng khoán theo ngành ICB")

# 3. Danh sách ngành ICB
stock_code_list = stock.listing.industries_icb()
stock_code_list.to_excel("data/xlsx/vietnam_stock_code_list/3_vietnam_stock_industries_icb_data.xlsx", index=False)  # Lưu file Excel
stock_code_list.to_csv('data/csv/vietnam_stock_code_list/3_vietnam_stock_industries_icb_data.csv', header=True, index=True)

print("3. Danh sách ngành ICB")

# liệt kê danh sách mã chứng khoán theo sàn giao dịch
stock_code_list = stock.listing.symbols_by_exchange()
stock_code_list.to_excel("data/xlsx/vietnam_stock_code_list/4_vietnam_stock_by_exchange_data.xlsx", index=False)  # Lưu file Excel
stock_code_list.to_csv('data/csv/vietnam_stock_code_list/4_vietnam_stock_by_exchange_data.csv', header=True, index=True)
print("4. Đã liệt kê danh sách mã chứng khoán theo sàn giao dịch")