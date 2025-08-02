# Netflix and Chill 🎬

A Streamlit dashboard for visual analysis of Netflix movies and TV shows.

This project was created as part of a Machine Learning team test assignment,  
featuring interactive filtering, metric cards, genre analysis, and a bit of fun.

## 🔍 Features
- Filter by type (Movie / TV Show), country, and genre
- Visualize rating distribution and content additions over time
- Get top-3 most common pairs of genres
- See duration distribution
- Export filtered data to `.xlsx`

## 🛠 Tech Stack
- Python 3
- Streamlit
- Pandas


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
Created by [@irchuri](https://github.com/irchuri) — with 2 liters of Milkis🍓 and a bit of tomfoolery.
