import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import base64

# Set page configuration
st.set_page_config(page_title="Used Car Price Predictor", page_icon="🚗", layout="wide")

# Function to set background image
def set_background(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        background_css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """
        st.markdown(background_css, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("⚠️ Background image not found. Please check the file path and ensure the image exists.")
    except Exception as e:
        st.error(f"⚠️ An error occurred while setting the background image: {e}")

# Set the background image
try:
    set_background("C:/Users/aashi/Downloads/car_theme.webp")
except Exception as e:
    st.error(f"⚠️ Error in background setup: {e}")

# Custom CSS for text color and shadow
custom_css = """
<style>
h1, h2, h3, h4, h5, h6, p {
    color: black; /* Change text to white for better contrast */
    font-weight: bold; /* Make text bold */
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar with app info

# Sidebar with app info
st.sidebar.markdown("""
<style>
.sidebar-title {
    color: #FF4500; /* Bright orange color */
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
    text-shadow: 2px 2px 5px #FFA500; /* Add a glowing shadow */
}
.sidebar-content {
    color: #008CBA; /* Bright blue color */
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}
.developer {
    color: #32CD32; /* Bright green color */
    font-size: 16px;
    font-style: italic;
    font-weight: bold;
    margin-top: 10px;
}
</style>

<div class="sidebar-title">🚗 Car Dheko</div>
<div class="sidebar-content">
Welcome to the Used Car Price Predictor App!
</div>
<div class="developer">Developer: Aashifa</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""\
- Predict the price of used cars based on multiple features.
- Provide accurate insights for customers and sales representatives.
""")

# Header
st.title("Used Car Price Prediction Tool")
st.subheader("Enhancing customer experience with ML-powered insights")

# Collect user inputs for features
st.markdown("### Input Car Details")
col1, col2, col3 = st.columns(3)

# Example car list (replace with your dataset's car names)
car_list = ['Maruti', 'Ford', 'Tata', 'Hyundai', 'Jeep', 'Datsun', 'Honda', 'Mahindra',
        'Mercedes-Benz', 'BMW', 'Renault', 'Audi', 'Toyota', 'Mini', 'Kia', 'Skoda',
        'Volkswagen', 'Volvo', 'MG', 'Nissan', 'Fiat', 'Mahindra Ssangyong',
        'Mitsubishi', 'Jaguar', 'Land Rover', 'Chevrolet', 'Citroen', 'Opel',
        'Mahindra Renault', 'Isuzu', 'Lexus', 'Porsche', 'Hindustan Motors'
]

city_list = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata']

try:
    with col1:
        car_name = st.selectbox("Car Name", options=car_list)
        kms_driven = st.number_input("Kilometers Driven", min_value=0, step=500, value=50000)
        engine = st.number_input("Engine (cc)", min_value=500, step=50, value=1200)
        no_of_years = st.number_input("Age of Car (Years)", min_value=0, step=1, value=5)

    with col2:
        city_name = st.selectbox("City", options=city_list)
        owner = st.selectbox("Number of Previous Owners", options=[0, 1, 2, 3])
        mileage = st.number_input("Mileage (kmpl)", min_value=5.0, step=0.5, value=15.0)
        max_power = st.number_input("Max Power (bhp)", min_value=40.0, step=0.5, value=80.0)

    with col3:
        fuel_type = st.selectbox("Fuel Type", options=["Diesel", "Petrol", "CNG", "LPG", "Electric"])
        transmission = st.selectbox("Transmission", options=["Manual", "Automatic"])
except Exception as e:
    st.error(f"⚠️ Error occurred while collecting inputs: {e}")

# One-hot encoding for categorical inputs
fuel_type_columns = ["Fuel Type_Diesel", "Fuel Type_Petrol", "Fuel Type_CNG", "Fuel Type_LPG", "Fuel Type_Electric"]
transmission_columns = ["Transmission_Manual", "Transmission_Automatic"]

# Prepare user input
try:
    user_data = {
        "Kms Driven": kms_driven,
        "Engine": engine,
        "No_of_Years": no_of_years,
        "Owner": owner,
        "Mileage": mileage,
        "Max Power": max_power,
    }

    # Add encoded columns for fuel type
    for col in fuel_type_columns:
        user_data[col] = 1 if f"Fuel Type_{fuel_type}" == col else 0

    # Add encoded columns for transmission
    for col in transmission_columns:
        user_data[col] = 1 if f"Transmission_{transmission}" == col else 0

    # Add one-hot encoded car columns
    car_columns = [f"Car_{c}" for c in car_list]  # Replace with actual car columns from training
    for col in car_columns:
        user_data[col] = 1 if f"Car_{car_name}" == col else 0
except Exception as e:
    st.error(f"⚠️ Error occurred while preparing input data: {e}")

# Load the model and feature columns
@st.cache_resource
def load_model_and_features():
    try:
        with open("rf_regression_model.pkl", "rb") as model_file:
            model = pickle.load(model_file)
        feature_columns = model.feature_names_in_
        return model, feature_columns
    except FileNotFoundError:
        st.error("⚠️ Model file not found. Please ensure it exists at the specified location.")
        return None, None
    except Exception as e:
        st.error(f"⚠️ An error occurred while loading the model: {e}")
        return None, None

model, feature_columns = load_model_and_features()

if model is None or feature_columns is None:
    st.stop()  # Stop execution if the model or features can't be loaded

# Ensure all required columns are present in the input data
try:
    for col in feature_columns:
        if col not in user_data:
            user_data[col] = 0  # Add missing columns with default value

    features_df = pd.DataFrame([user_data])[feature_columns]  # Match column order
except Exception as e:
    st.error(f"⚠️ Error occurred while aligning input data: {e}")

# CSS to style the button
st.markdown("""\
    <style>
    .stButton > button {
        background-color: red;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Predict car price
if st.button("Predict Price"):
    try:
        predicted_price = model.predict(features_df)
        st.markdown(f"### Estimated Price: ₹{predicted_price[0]:,.2f} Lakhs")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")

# Footer
st.markdown("---")
st.markdown("© 2024 Car Dheko - Enhancing Customer Experience with Machine Learning.")
