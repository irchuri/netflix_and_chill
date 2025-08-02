def extract_duration_int(df):
    df = df.copy()
    df['duration_int'] = df['duration'].apply(lambda x: int(''.join(filter(str.isdigit, str(x)))))
    return df