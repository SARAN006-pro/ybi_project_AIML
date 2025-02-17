import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Bollywood Movie Data (Replace with real data from IMDb or other sources)
data = {
    "movie_title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E", "Movie F", "Movie G", "Movie H", "Movie I", "Movie J"],
    "genre": ["Action", "Romance", "Comedy", "Drama", "Action", "Comedy", "Romance", "Thriller", "Drama", "Action"],
    "release_year": [2023, 2022, 2023, 2021, 2022, 2023, 2020, 2022, 2021, 2023],
    "box_office_crores": [150, 88, 120, 60, 200, 80, 98, 70, 58, 180],
    "lead_actor": ["Actor X", "Actor Y", "Actor Z", "Actor X", "Actor X", "Actor Y", "Actor Z", "Actor X", "Actor Z", "Actor X"]
}

# Create DataFrame
bollywood_df = pd.DataFrame(data)

# Basic Data Exploration
print(bollywood_df.head())
print(bollywood_df.info())

# Genre Analysis
genre_counts = bollywood_df['genre'].value_counts()
print("Movie Count by Genre:\n", genre_counts)

# Box Office Collection by Genre
box_office_by_genre = bollywood_df.groupby('genre')['box_office_crores'].sum()
print("Total Box Office Collection by Genre:\n", box_office_by_genre)

# Lead Actor Analysis
lead_actor_box_office = bollywood_df.groupby('lead_actor')['box_office_crores'].sum()
print("Total Box Office Collection by Lead Actor:\n", lead_actor_box_office)

# Visualization
plt.figure(figsize=(10, 5))
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
plt.title("Movie Count by Genre")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x=box_office_by_genre.index, y=box_office_by_genre.values, palette='coolwarm')
plt.title("Total Box Office Collection by Genre")
plt.xlabel("Genre")
plt.ylabel("Box Office (Crores)")
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x=lead_actor_box_office.index, y=lead_actor_box_office.values, palette='magma')
plt.title("Total Box Office Collection by Lead Actor")
plt.xlabel("Lead Actor")
plt.ylabel("Box Office (Crores)")
plt.show()

# Pie Chart for Box Office Collection by Genre
plt.figure(figsize=(8, 8))
plt.pie(box_office_by_genre, labels=box_office_by_genre.index, autopct='%1.1f%%', startangle=140)
plt.title("Box Office Collection by Genre")
plt.show()
