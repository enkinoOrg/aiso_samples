import pandas as pd
import numpy as np
import io

def fun(input_data):
    csv_bytes = input_data[0]
    csv_bytes = io.StringIO(csv_bytes)
    na_values = ['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null']
    df = pd.read_csv(csv_bytes, na_values=na_values)
    nums = df.select_dtypes(include=[np.number]).columns.tolist()
    for col in df:
        if(df[col].isnull().any()):
            if(col in nums):
                df[col] = df[col].fillna(df[col].mean())
            else:
                df[col] = df[col].fillna(df[col].mode().iloc[0])
    df = df.drop(df.filter(regex='Unnamed').columns, axis=1)
    return [df.to_string()]
