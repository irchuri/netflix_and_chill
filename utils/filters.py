
def apply_filters(df, selected_type, selected_country, selected_genre):
    df = df.copy()
    if selected_type != 'All':
        df = df[df["type"] == selected_type]
    if selected_country != 'All':
        df = df[df["country"] == selected_country]
    if selected_genre != "All":
        df = df[df["genres_list"].apply(lambda genres: selected_genre in genres if isinstance(genres, list) else False)]
    return df