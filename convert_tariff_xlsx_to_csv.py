import pandas as pd
import os

# Define paths
input_dir = r"E:\UIT\DS111\tariff_rate_raw"
output_dir = r"E:\UIT\DS111\Raw data\tariff_csv"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# List all .xlsx files in the input directory
xlsx_files = [f for f in os.listdir(input_dir) if f.endswith('.xlsx') and not f.startswith('~$')]

print(f"Found {len(xlsx_files)} .xlsx files in {input_dir}")

# Expected columns including 'id' (already present in Excel)
expected_columns = [
    'id',
    'Country/Territory',
    'Year of MFN applied tariff',
    'Binding coverage | Bound in %',
    'Simple average | Bound',
    'Simple average | MFN applied',
    'Duty-free | Bound',
    'Duty-free | MFN applied',
    'Non-ad valorem duties | Bound',
    'Non-ad valorem duties | MFN applied',
    'Duties > 15% | Bound',
    'Duties > 15% | MFN applied',
    'Duties > 3 * AVG | Bound',
    'Duties > 3 * AVG | MFN applied',
    'Concessions not yet implemented in 2024',
    'Maximum duty | Bound',
    'Maximum duty | MFN applied',
    'Number of distinct duty rates | Bound',
    'Number of distinct duty rates | MFN applied',
    'Coefficient of variation | Bound',
    'Coefficient of variation | MFN applied',
    'Number of MFN applied tariff lines',
    'Country/Territory'  # Duplicate at the end
]

for xlsx_file in xlsx_files:
    xlsx_path = os.path.join(input_dir, xlsx_file)
    csv_filename = os.path.splitext(xlsx_file)[0] + '.csv'
    csv_path = os.path.join(output_dir, csv_filename)

    try:
        # Read Excel file, skipping first 6 rows
        df = pd.read_excel(xlsx_path, skiprows=6, header=0)

        # Assign expected columns
        if len(df.columns) < len(expected_columns):
            print(f"Error: '{xlsx_file}' has fewer columns ({len(df.columns)}) than expected ({len(expected_columns)}). Skipping.")
            continue
        elif len(df.columns) > len(expected_columns):
            df.columns = expected_columns + list(df.columns[len(expected_columns):])
        else:
            df.columns = expected_columns

        # Save to CSV
        df.to_csv(csv_path, index=False)
        print(f"Successfully converted '{xlsx_file}' to '{csv_filename}'")
    except Exception as e:
        print(f"Error converting '{xlsx_file}': {e}")

print("Conversion process completed.")