import pandas as pd
import matplotlib.pyplot as plt

data_link = 'https://drive.google.com/uc?id=1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y'
df = pd.read_csv(data_link)

price_col = 'Price range'

plt.figure(figsize=(10, 6))
df[price_col].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Price Ranges Distribution')
plt.xlabel('Price Range')
plt.ylabel('Restaurants Count')
plt.xticks(rotation=0)
plt.show()

price_counts = df[price_col].value_counts()
total_restaurants = len(df)
percentage_by_price = (price_counts / total_restaurants) * 100

print("\nPercentage of Restaurants in Each Price Range:")
print(percentage_by_price.to_string(index=True))
