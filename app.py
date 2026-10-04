import streamlit as st
import pandas as pd
import joblib
# Load trained model
model = joblib.load("models/car_price_model.pkl")

# Page title
st.title("Used Car Price Prediction")

st.write("Enter car details to predict the estimated price.")
# Car name
car_name = st.selectbox(
    "Car Name / Model",
    [
        "Toyota Corolla GLi",
        "Honda Civic 1.8",
        "Suzuki Alto VXL",
        "Toyota Yaris ATIV",
        "Honda City Aspire",
        "Suzuki Wagon R",
        "Toyota Corolla Altis",
        "Honda Civic Oriel",
        "Suzuki Cultus VXL",
        "Toyota Vitz"
    ]
)

# Car year
year = st.number_input(
    "Car Year",
    min_value=1990,
    max_value=2026,
    value=2020,
    step=1
)
mileage = st.number_input(
    "Mileage (km)",
    min_value=0,
    max_value=1000000,
    value=45000,
    step=1000
)
engine = st.number_input(
    "Engine (cc)",
    min_value=500,
    max_value=8000,
    value=1300,
    step=100
)
location = st.selectbox(
    "Location",
    ["lahore", "islamabad", "karachi"]
)
transmission = st.selectbox(
    "Transmission",
    ["Automatic", "Manual"]
)
if st.button("Predict Price"):
    car = pd.DataFrame([
        {
            "year": year,
            "mileage_clean": mileage,
            "engine_clean": engine,
            "location_clean": location,
            "transmission": transmission
        }
    ])
    

    prediction = model.predict(car)

    st.success(f"Estimated Car Price: PKR {prediction[0]:,.0f}")
    st.title("Used Car Price Prediction")
st.subheader("Pakistan Used Car Price Estimator")
st.divider()

st.subheader("About This Project")

st.write(
    "This project uses Machine Learning to estimate the price "
    "of used cars in Pakistan based on car year, mileage, engine size, "
    "location, and transmission."
)