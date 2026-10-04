import pandas as pd
import joblib

# 1. Load trained model
model = joblib.load("models/car_price_model.pkl")

# 2. Create a new car
car = pd.DataFrame([
    {
        "year": 2020,
        "mileage_clean": 45000,
        "engine_clean": 1300,
        "location_clean": "lahore",
        "transmission": "Automatic"
    }
])

# 3. Make prediction
prediction = model.predict(car)

# 4. Display predicted price
print("-------------------------------")
print("Used Car Price Prediction")
print("-------------------------------")
print(f"Estimated Car Price: PKR {prediction[0]:,.0f}")