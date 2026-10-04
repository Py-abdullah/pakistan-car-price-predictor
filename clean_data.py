import pandas as pd
import re

# File paths
INPUT_FILE = "data/raw/cars_raw.csv"
OUTPUT_FILE = "data/processed/cars_clean.csv"

# Read data
df = pd.read_csv(INPUT_FILE)


# Clean price
def clean_price(value):

    if pd.isna(value):
        return None

    value = str(value).lower().strip()
    value = value.replace(",", "")
    value = value.replace("rs", "")
    value = value.replace("pkr", "")
    value = value.strip()

    # Handle lacs
    if "lac" in value:
        number = re.findall(r"\d+\.?\d*", value)

        if number:
            return float(number[0]) * 100000

    # Handle million
    if "million" in value:
        number = re.findall(r"\d+\.?\d*", value)

        if number:
            return float(number[0]) * 1000000

    # Normal numbers
    number = re.findall(r"\d+\.?\d*", value)

    if number:
        return float(number[0])

    return None


# Clean mileage
def clean_mileage(value):

    if pd.isna(value):
        return None

    value = str(value).lower().strip()
    value = value.replace(",", "")

    # 65k -> 65000
    if re.search(r"\b\d+\.?\d*\s*k\b", value):
        number = re.findall(r"\d+\.?\d*", value)

        if number:
            return float(number[0]) * 1000

    # 78000 km -> 78000
    number = re.findall(r"\d+\.?\d*", value)

    if number:
        return float(number[0])

    return None


# Clean location
def clean_location(value):

    if pd.isna(value):
        return None

    value = str(value).lower().strip()

    location_map = {
        "lhr": "lahore",
        "lahore": "lahore",
        "isb": "islamabad",
        "islamabad": "islamabad",
        "khi": "karachi",
        "karachi": "karachi"
    }

    return location_map.get(value, value)


# Clean engine
def clean_engine(value):

    if pd.isna(value):
        return None

    value = str(value).lower()

    number = re.findall(r"\d+", value)

    if number:
        return int(number[0])

    return None


# Apply cleaning
df["price_clean"] = df["price"].apply(clean_price)
df["mileage_clean"] = df["mileage"].apply(clean_mileage)
df["location_clean"] = df["location"].apply(clean_location)
df["engine_clean"] = df["engine"].apply(clean_engine)

# Clean year
df["year"] = pd.to_numeric(df["year"], errors="coerce")


# Show cleaned data
print("\nCLEANED DATA:")
print(df[[
    "price",
    "price_clean",
    "mileage",
    "mileage_clean",
    "location",
    "location_clean",
    "engine",
    "engine_clean",
    "year"
]])
df.to_csv(OUTPUT_FILE, index=False)

print("Cleaned file saved successfully!")