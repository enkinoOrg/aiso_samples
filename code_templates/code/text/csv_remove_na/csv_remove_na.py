import pandas as pd
import io


def fun(input_data):
    csv_bytes = input_data[0]
    csv_bytes = io.StringIO(csv_bytes)
    na_values = ['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null']
    df = pd.read_csv(csv_bytes, na_values=na_values)
    df = df.drop(df.filter(regex='Unnamed').columns, axis=1)
    df.dropna(inplace=True)
    return [df.to_string()]