import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/processed/cars_clean.csv")

print(df.describe())

print("\nPrice statistics:")
print(df["price_clean"].describe())

print("\nLocation counts:")
print(df["location_clean"].value_counts())


# Price distribution

plt.figure(figsize=(10, 6))

sns.histplot(df["price_clean"], kde=True)

plt.title("Car Price Distribution")
plt.xlabel("Price (PKR)")
plt.ylabel("Number of Cars")

plt.show()


# Year vs Price

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="year",
    y="price_clean"
)

plt.title("Car Year vs Price")
plt.xlabel("Year")
plt.ylabel("Price")

plt.show()


# Mileage vs Price

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="mileage_clean",
    y="price_clean"
)

plt.title("Mileage vs Price")
plt.xlabel("Mileage")
plt.ylabel("Price")

plt.show()