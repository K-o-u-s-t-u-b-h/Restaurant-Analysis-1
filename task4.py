import pandas as pd

link = 'https://drive.google.com/uc?id=1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y'
data = pd.read_csv(link)

online_col = 'Has Online delivery'
rating_col = 'Aggregate rating'

online_percentage = (data[online_col].value_counts(normalize=True) * 100).round(2)

avg_rating_with = data[data[online_col] == 'Yes'][rating_col].mean()
avg_rating_without = data[data[online_col] == 'No'][rating_col].mean()

print(f"Online Percentage: {online_percentage['Yes']}%")
print("\nAverage Rating Comparison:")
print(f"  With Online: {avg_rating_with:.2f}")
print(f"  Without Online: {avg_rating_without:.2f}")
