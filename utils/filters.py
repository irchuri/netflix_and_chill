import pandas as pd


def apply_filters(df, selected_type, selected_country, selected_genres):
    df = df.copy()
    if selected_type != 'All':
        df = df[df["type"] == selected_type]
    if selected_country != 'All':
        df = df[df["country"] == selected_country]
    if 'All' not in selected_genres:
        df = df[df['genres_list'].apply(lambda x: any(genre in x for genre in selected_genres))]
    return df