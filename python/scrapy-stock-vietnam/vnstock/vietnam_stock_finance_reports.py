from vnstock3 import Vnstock  # Nạp thư viện để sử dụng

code = 'SHB'
period = 'year'

stock = Vnstock().stock(symbol=code, source='VCI')

df = stock.finance.income_statement(period=period, lang='vi')
print(df.head())  # Hiển thị 5 dòng dữ liệu đầu tiên
df.to_excel("data/vietnam_stock_finance_reports/vietnam_stock_finance_" + year + "_" + code + ".xlsx", index=False)  # Lưu file Excel