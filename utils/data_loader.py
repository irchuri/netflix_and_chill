import pandas as pd


def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=True)
    df = df.dropna(subset=[col for col in df.columns if col != 'director'])
    df['genres_list'] = df['listed_in'].apply(lambda x: x.split(', '))
    return df


