import pandas as pd
import os

# Định nghĩa đường dẫn thư mục chứa các tệp CSV đầu vào
input_dir = r"E:\UIT\DS111\Raw data\tariff_csv"

print(f"Bắt đầu quá trình làm sạch dữ liệu cho các tệp CSV trong {input_dir}")

# Liệt kê tất cả các tệp .csv trong thư mục đầu vào
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

for csv_file in csv_files:
    csv_path = os.path.join(input_dir, csv_file)
    
    try:
        # Đọc tệp CSV vào DataFrame
        df = pd.read_csv(csv_path)
        
        # Xóa cột 'Country/Territory' cuối cùng nếu nó tồn tại và là bản sao
        # (Được xác định là bản sao nếu có nhiều hơn một cột cùng tên)
        if 'Country/Territory' in df.columns and df.columns.tolist().count('Country/Territory') > 1:
            # Tìm chỉ mục của cột 'Country/Territory' cuối cùng
            cols = df.columns.tolist()
            last_country_col_index = len(cols) - 1 - cols[::-1].index('Country/Territory')
            df = df.drop(df.columns[last_country_col_index], axis=1)
            print(f"Đã xóa cột 'Country/Territory' trùng lặp trong '{csv_file}'")

        # Xóa các cột có tên bắt đầu bằng 'Unnamed:'
        # Đây thường là các cột trống được tạo ra trong quá trình chuyển đổi từ Excel
        unnamed_cols = [col for col in df.columns if col.startswith('Unnamed:')]
        if unnamed_cols:
            df = df.drop(columns=unnamed_cols)
            print(f"Đã xóa các cột không tên {unnamed_cols} trong '{csv_file}'")
        
        # Lưu dữ liệu đã làm sạch trở lại cùng tệp CSV, ghi đè lên tệp gốc
        df.to_csv(csv_path, index=False)
        print(f"Đã làm sạch và ghi đè thành công tệp '{csv_file}'")
        
    except Exception as e:
        print(f"Lỗi khi làm sạch tệp '{csv_file}': {e}")

print("Quá trình làm sạch dữ liệu đã hoàn tất.")
