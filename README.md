# Understanding Movie Trends in Bollywood

## 📌 Project Overview
This project analyzes Bollywood movie trends using data science techniques. It explores box office collections, genre distributions, and actor performances using **Pandas, Matplotlib, and Seaborn** for data manipulation and visualization.

## 🔍 Key Features
- **Data Cleaning & Preprocessing**: Standardizes movie titles, genres, and actor names.
- **Genre Analysis**: Determines the most popular genres by movie count.
- **Box Office Trends**: Tracks total revenue collected per genre and per lead actor.
- **Data Visualizations**:
  - Bar charts for genre and actor-based collections.
  - Pie chart for genre-based box office revenue.
  - Line chart for yearly revenue trends.
  - Word cloud for popular genres.

## 📊 Technologies Used
- Python 🐍
- Pandas 🗂️
- Matplotlib 📈
- Seaborn 🎨
- WordCloud ☁️

## 📂 Dataset
The dataset consists of Bollywood movies with columns such as:
- `movie_title` - Title of the movie
- `genre` - Primary genre of the movie
- `release_year` - Year of release
- `box_office_crores` - Total box office earnings (in crores)
- `lead_actor` - Lead actor of the movie

## 🔧 How to Run
1. Install dependencies using:
   ```sh
   pip install pandas matplotlib seaborn wordcloud
   ```
2. Run the script:
   ```sh
   python bollywood_trends.py
   ```
3. View generated graphs and insights.

## 📌 Results
- **Most popular genre:** Action (Highest number of movies & earnings)
- **Highest box office collection:** Actor X
- **Steady increase in movie releases over the years**
- **Thriller genre has the least earnings**

## 📎 Files
- `bollywood_trends.py` → Main analysis script
- `bollywood_movies_cleaned.csv` → Cleaned dataset
- `README.md` → Project documentation
- `box_office_by_genre.png` → Box office visualization

## 🚀 Future Enhancements
- Web scraping from IMDb for real-time data.
- Adding director-based analysis.
- Predictive modeling for box office success.

---
📢 **Contributions Welcome!** If you’d like to add new features, feel free to fork this repository and submit a PR! 🎬
