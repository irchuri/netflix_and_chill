from streamlit.testing.v1.element_tree import Dataframe
import pandas as pd
from preprocessing import extract_duration_int
from itertools import combinations


def get_rating_distribution(df):
    df = df.copy()

    rating_df = df['rating'].value_counts(sort=False).reset_index()
    rating_df.columns = ['rating', 'count']
    rating_df = rating_df.sort_values(by='count', ascending=False)

    return rating_df


def get_top_genres(df):
    df = df.copy()

    genre_list = sum(df['genres_list'].values, [])
    genre_ser = pd.Series(genre_list).value_counts()
    genre_df = genre_ser.reset_index()
    genre_df.columns = ['genre', 'count']

    return genre_df


def get_yearly_additions(df):
    df = df.copy()

    yearly_df = df['release_year'].value_counts(sort=False).reset_index()
    yearly_df.columns = ['year', 'count']
    yearly_df = yearly_df.sort_values(by='year', ascending=False)

    return yearly_df


def movie_vs_show(df):
    df = df.copy()

    type_df = (df['type'].value_counts(normalize=True) * 100).reset_index()
    type_df.columns = ['type', 'percentage']
    type_df['percentage'] = type_df['percentage'].round(2)

    return type_df


def genre_by_country(df, selected_genre):
    df = df.copy()

    if selected_genre and selected_genre != 'All':
        df = df[df['genres_list'].apply(lambda x: selected_genre in x)]

    genre_country_df = df['country'].value_counts().reset_index()
    genre_country_df.columns = ['country', 'count']
    genre_country_df = genre_country_df.sort_values(by='count', ascending=False)

    return genre_country_df


def get_duration_metrics(df):
    df = df.copy()

    movies_df = df[df['type'] == 'Movie'].copy()
    shows_df = df[df['type'] == 'TV Show'].copy()

    movies_df = extract_duration_int(movies_df)
    shows_df = extract_duration_int(shows_df)

    data = {
        'type': ['Movie', 'TV Show'],
        'mean': [movies_df['duration_int'].mean(), shows_df['duration_int'].mean()],
        'median': [movies_df['duration_int'].median(), shows_df['duration_int'].median()],
        'max': [movies_df['duration_int'].max(), shows_df['duration_int'].max()],
        'min': [movies_df['duration_int'].min(), shows_df['duration_int'].min()]
    }
    duration_df = pd.DataFrame(data)

    return duration_df


def content_by_country(df):
    df = df.copy()

    country_type_counts = df.groupby(['country', 'type']).size().reset_index(name='count')
    country_type_counts = country_type_counts.pivot(index='country', columns='type', values='count')

    country_type_counts.fillna(0, inplace=True)

    return country_type_counts


def top_genre_combos(df, top_n=3):
    df = df.copy()

    pairs = []

    df['genres_list'].apply(
        lambda genre_list: pairs.extend(
            [' + '.join(sorted(pair)) for pair in combinations(genre_list, 2)]
        ) if len(genre_list) >= 2 else None
    )

    pairs = pd.Series(pairs)
    pairs = pairs.value_counts().reset_index()
    pairs.columns = ['genre_pair', 'count']
    pairs = pairs.sort_values(by='count', ascending=False).head(top_n)

    return pairs

