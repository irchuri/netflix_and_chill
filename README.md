# Netflix and Chill 🎬

A Streamlit dashboard for visual analysis of Netflix movies and TV shows.

This project was created as part of a Machine Learning team test assignment,  
featuring interactive filtering, metric cards, genre analysis, and a bit of fun.

## 🔍 Features
- Filter by type (Movie / TV Show), country, and genre
- Visualize rating distribution and content additions over time
- Analyze top genres and word frequency in descriptions
- Generate a word cloud from selected data
- Export filtered data to `.xlsx`

## 🛠 Tech Stack
- Python 3.x
- Streamlit
- Pandas, NumPy
- Matplotlib, Seaborn, WordCloud

## ▶ How to run
1. Install dependencies:
```pip install -r requirements.txt```
2. Run the app:
```streamlit run app.py```
3. Open in browser (usually at `http://localhost:8501`)

## 📁 Project structure
```
📦 netflix_and_chill
├── app.py
├── requirements.txt
├── Netflix.csv
├── README.md
└── utils/
    ├── data_loader.py
    ├── filters.py
    └── metrics.py
```

## 🧠 Author
Created by [@irchuri](https://github.com/irchuri) — with LitEnergy and a bit of tomfoolery.