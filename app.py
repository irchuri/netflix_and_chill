import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from utils.data_loader import load_data
from utils.filters import apply_filters
from utils.metrics import (
    get_rating_distribution,
    get_top_genres,
    get_yearly_additions,
    movie_vs_show,
    genre_by_country,
    content_by_country,
    get_duration_metrics,
    top_genre_combos,
)

st.set_page_config(page_title="Netflix and Chill", layout="wide")
st.title("🎬 Netflix and Chill Dashboard")

# Загрузка данных
df = load_data("Netflix.csv")

# Фильтры
st.sidebar.header("Filters")
selected_type = st.sidebar.selectbox("Type", options=["All", "Movie", "TV Show"])
selected_country = st.sidebar.selectbox("Country", options=["All"] + sorted(df["country"].dropna().unique()))
selected_genre = st.sidebar.selectbox("Genre", options=["All"] + sorted(set(genre for sublist in df["genres_list"].dropna() for genre in sublist)))

# Применение фильтров
filtered_df = apply_filters(df, selected_type, selected_country, selected_genre)

# Верхние метрики
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Titles", len(filtered_df))

mv_vs_show = movie_vs_show(filtered_df)
if not mv_vs_show.empty and 'Movie' in mv_vs_show['type'].values:
    movie_percent = mv_vs_show[mv_vs_show['type'] == 'Movie']['percentage'].values[0]
    col2.metric("Movies (%)", f"{round(movie_percent, 1)}%")
else:
    col2.metric("Movies (%)", "N/A")

top_genres = get_top_genres(filtered_df)
if not top_genres.empty:
    col3.metric("Top Genre", top_genres.iloc[0]['genre'])
else:
    col3.metric("Top Genre", "N/A")


# Вкладки
tab1, tab2, tab3 = st.tabs(["Ratings & Years", "Genres & Countries", "Durations & Pairs"])

with tab1:
    st.subheader("Rating Distribution")
    rating_df = get_rating_distribution(filtered_df)
    st.bar_chart(rating_df.set_index("rating"))

    st.subheader("Yearly Additions")
    yearly_df = get_yearly_additions(filtered_df)
    st.line_chart(yearly_df.set_index("year"))

with tab2:
    st.subheader("Top Genres")
    genre_df = get_top_genres(filtered_df)
    st.bar_chart(genre_df.set_index("genre").head(10))

    st.subheader("Top Countries in Selected Genre")
    if selected_genre != "All":
        genre_country = genre_by_country(df, selected_genre)
        st.bar_chart(genre_country.set_index("country").head(10))
    else:
        st.info("Select a genre to see country distribution.")

    st.subheader("Content Type by Country")
    by_country_df = content_by_country(filtered_df)
    st.dataframe(by_country_df)

with tab3:
    st.subheader("Duration Distribution")
    duration_df = get_duration_metrics(filtered_df)
    st.dataframe(duration_df)

    st.subheader("Top Genre Pairs")
    pair_df = top_genre_combos(filtered_df)
    st.bar_chart(pair_df.set_index("genre_pair").head(10))

# Таблица данных
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Скачать
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    return output.getvalue()

st.download_button("📥 Download as Excel", data=to_excel(filtered_df), file_name="netflix_filtered.xlsx")
