import pandas as pd

google_drive_link = 'https://drive.google.com/uc?id=1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y'
restaurant_data = pd.read_csv(google_drive_link)

city_col = 'City'
rating_col = 'Aggregate rating'

city_with_most_restaurants = restaurant_data[city_col].value_counts().idxmax()

average_ratings_by_city = restaurant_data.groupby(city_col)[rating_col].mean()

city_with_highest_avg_rating = average_ratings_by_city.idxmax()
highest_avg_rating = average_ratings_by_city.max()

print(f"City with the Most Restaurants: {city_with_most_restaurants}")
print("\nAverage Rating for Restaurants in Each City:")
print(average_ratings_by_city.to_string(index=True))
print(f"\nCity with the Highest Average Rating: {city_with_highest_avg_rating} (Average Rating: {highest_avg_rating:.2f})")
