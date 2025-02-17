import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Enhanced Bollywood Movie Data
data = {
    "movie_title": ["Action King", "Love Saga", "Comedy Nights", "Dramatic Life", "Power Moves", 
                    "Laugh Riot", "Romantic Journey", "Mystery Case", "Emotional Ride", "Warrior"],
    "genre": ["Action", "Romance", "Comedy", "Drama", "Action", "Comedy", "Romance", "Thriller", "Drama", "Action"],
    "release_year": [2023, 2022, 2023, 2021, 2022, 2023, 2020, 2022, 2021, 2023],
    "box_office_crores": [250, 105, 150, 85, 300, 120, 110, 95, 75, 280],
    "lead_actor": ["Actor A", "Actor B", "Actor C", "Actor A", "Actor A", "Actor B", "Actor C", "Actor D", "Actor C", "Actor A"],
    "director": ["Director X", "Director Y", "Director Z", "Director X", "Director X", 
                 "Director Y", "Director Z", "Director W", "Director Z", "Director X"]
}

# Create DataFrame
bollywood_df = pd.DataFrame(data)

# Save to CSV (optional)
bollywood_df.to_csv("bollywood_movies.csv", index=False)

# Display first few rows
print(bollywood_df.head())
