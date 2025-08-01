from streamlit.testing.v1.element_tree import Dataframe
import pandas as pd


def get_rating_distribution(df):
    df = df.copy()
    rating_df = df['rating'].value_counts(sort=False).reset_index()
    rating_df.columns = ['rating','count']
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