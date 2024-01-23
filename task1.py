import pandas as pd

google_drive_link = 'https://drive.google.com/uc?id=1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y'
restaurants_data = pd.read_csv(google_drive_link)

cuisine_column_name = 'Cuisines'

cuisine_counts = restaurants_data[cuisine_column_name].value_counts()
top_cuisines = cuisine_counts.head(3)

total_restaurants = len(restaurants_data)
percentage_top_cuisines = (top_cuisines / total_restaurants) * 100

print("Top Three Cuisines:")
for rank, (cuisine, count) in enumerate(zip(top_cuisines.index, top_cuisines), start=1):
    print(f"{rank}. {cuisine.ljust(25)}: {count} restaurants")

print("\nPercentage of Restaurants Serving Each Top Cuisine:")
for rank, (cuisine, percentage) in enumerate(zip(top_cuisines.index, percentage_top_cuisines), start=1):
    print(f"{rank}. {cuisine.ljust(25)}: {percentage:.2f}%")
