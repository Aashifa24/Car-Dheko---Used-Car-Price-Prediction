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

<div class="sidebar-title">🚗 Car Dekho</div>
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

car_model_list = { 
    'Maruti': ['Maruti Celerio', 'Maruti SX4 S Cross', 'Maruti Ciaz', 'Maruti Baleno', 'Maruti Swift', 'Maruti Wagon R', 
               'Maruti Ertiga', 'Maruti Alto 800', 'Maruti Alto', 'Maruti Ritz', 'Maruti Alto K10', 'Maruti Ignis', 
               'Maruti Vitara Brezza', 'Maruti Swift Dzire', 'Maruti Gypsy', 'Maruti Celerio X', 'Maruti Omni', 
               'Maruti 1000', 'Maruti Zen', 'Maruti SX4', 'Maruti A-Star', 'Maruti XL6', 'Maruti Ertiga Tour', 
               'Maruti 800', 'Maruti Wagon R Stingray', 'Maruti Zen Estilo', 'Maruti Versa', 'Maruti Brezza', 
               'Maruti Swift Dzire Tour', 'Maruti FRONX', 'Maruti Celerio Tour 2018-2021', 'Maruti Grand Vitara'],

    'Ford': ['Ford Ecosport', 'Ford Endeavour', 'Ford Figo', 'Ford Ikon', 'Ford Aspire', 
             'Ford Freestyle', 'Ford Fiesta', 'Ford Mondeo', 'Ford Fiesta Classic'],

    'Tata': ['Tata Tiago', 'Tata Nexon', 'Tata New Safari', 'Tata Harrier', 'Tata Tigor', 'Tata Safari Storme', 
             'Tata Altroz', 'Tata Nexon EV Max', 'Tata Indica V2', 'Tata Nexon EV Prime', 'Tata Hexa', 
             'Tata Manza', 'Tata Nano', 'Tata Indigo', 'Tata Zest', 'Tata Sumo', 'Tata Punch', 'Tata Tiago NRG', 
             'Tata Indica', 'Tata Yodha Pickup', 'Tata Indigo Marina', 'Tata Aria', 'Tata Bolt', 'Tata Sumo Victa'],

    'Hyundai': ['Hyundai Xcent', 'Hyundai Venue', 'Hyundai Grand i10', 'Hyundai i20', 'Hyundai Santro', 'Hyundai Santro Xing', 
                'Hyundai Elantra', 'Hyundai Getz', 'Hyundai Creta', 'Hyundai i10', 'Hyundai EON', 'Hyundai Alcazar', 
                'Hyundai Tucson', 'Hyundai Verna', 'Hyundai Santa Fe', 'Hyundai i20 Active', 'Hyundai Accent', 
                'Hyundai Grand i10 Nios', 'Hyundai i20 N Line', 'Hyundai Sonata', 'Hyundai Aura', 'Hyundai Xcent Prime', 'Hyundai Kona'],
    'Jeep': ['Jeep Compass', 'Jeep Meridian', 'Jeep Wrangler', 'Jeep Compass Trailhawk'],

    'Datsun': ['Datsun GO', 'Datsun RediGO', 'Datsun GO Plus'],

    'Honda': ['Honda Jazz', 'Honda City', 'Honda Brio', 'Honda CR-V', 'Honda WR-V', 'Honda New Accord', 
              'Honda Amaze', 'Honda Civic', 'Honda BR-V', 'Honda Mobilio', 'Honda City Hybrid'],

    'Mahindra': ['Mahindra XUV500', 'Mahindra Scorpio', 'Mahindra KUV 100', 'Mahindra XUV300', 'Mahindra Ssangyong Rexton', 
                 'Mahindra Thar', 'Mahindra e2o Plus', 'Mahindra TUV 300', 'Mahindra Bolero Power Plus', 'Mahindra TUV 300 Plus', 
                 'Mahindra Marazzo', 'Mahindra XUV700', 'Mahindra Quanto', 'Mahindra Xylo', 'Mahindra Bolero Camper', 
                 'Mahindra Renault Logan', 'Mahindra Jeep', 'Mahindra Bolero', 'Mahindra Scorpio N', 'Mahindra KUV 100 NXT', 
                 'Mahindra E Verito', 'Mahindra Bolero Neo', 'Mahindra Bolero Pik Up Extra Long'],

    'Mercedes-Benz': ['Mercedes-Benz GLA', 'Mercedes-Benz S-Class', 'Mercedes-Benz E-Class', 'Mercedes-Benz C-Class', 
                      'Mercedes-Benz GL-Class', 'Mercedes-Benz A-Class Limousine', 'Mercedes-Benz A Class', 
                      'Mercedes-Benz B Class', 'Mercedes-Benz M-Class', 'Mercedes-Benz GLE', 'Mercedes-Benz CLA', 
                      'Mercedes-Benz GLS', 'Mercedes-Benz GLA Class', 'Mercedes-Benz GLC', 'Mercedes-Benz GLC Coupe', 
                      'Mercedes-Benz AMG GLA 35', 'Mercedes-Benz AMG A 35', 'Mercedes-Benz G', 'Mercedes-Benz CLS-Class', 
                      'Mercedes-Benz SLC', 'Mercedes-Benz EQC', 'Mercedes-Benz AMG GLC 43', 'Mercedes-Benz AMG G 63'],

    'BMW': ['BMW 5 Series', 'BMW 3 Series GT', 'BMW X3', 'BMW 3 Series', 'BMW X5', 'BMW 6 Series', 
            'BMW X4', 'BMW X1', 'BMW 7 Series', 'BMW 3 Series Gran Limousine', 'BMW 1 Series', 
            'BMW X7',  'BMW 2 Series'],

    'Renault': ['Renault Duster', 'Renault KWID', 'Renault Lodgy', 'Renault Kiger', 'Renault Triber', 
                'Renault Captur', 'Renault Fluence', 'Renault Pulse', 'Renault Scala'],

    'Audi': ['Audi A4', 'Audi A6', 'Audi Q7', 'Audi Q5', 'Audi A3', 'Audi Q3', 'Audi A3 cabriolet', 
             'Audi Q3 Sportback', 'Audi A8', 'Audi Q2', 'Audi S5 Sportback'],

    'Toyota': ['Toyota Fortuner', 'Toyota Yaris', 'Toyota Innova', 'Toyota Urban cruiser', 'Toyota Corolla Altis', 
               'Toyota Glanza', 'Toyota Etios', 'Toyota Etios Cross', 'Toyota Hyryder', 'Toyota Etios Liva', 
               'Toyota Vellfire', 'Toyota Land Cruiser 300', 'Toyota Fortuner Legender', 'Toyota Qualis', 
               'Toyota Corolla'],

    'Mini': ['Mini 3 DOOR', 'Mini Cooper', 'Mini Cooper Countryman', 'Mini 5 DOOR', 
             'Mini Cooper SE', 'Mini Cooper Clubman', 'Mini Cooper Convertible'],

    'Kia': ['Kia Seltos', 'Kia Carnival', 'Kia Sonet', 'Kia Carens'],

    'Skoda': ['Skoda Rapid', 'Skoda Octavia', 'Skoda Superb', 'Skoda Kushaq', 'Skoda Laura', 
              'Skoda Yeti', 'Skoda Slavia', 'Skoda Fabia', 'Skoda Kodiaq'],

    'Volkswagen': ['Volkswagen Polo', 'Volkswagen Vento', 'Volkswagen T-Roc', 'Volkswagen Taigun', 'Volkswagen Jetta',
                   'Volkswagen Tiguan', 'Volkswagen Ameo', 'Volkswagen Tiguan Allspace', 'Volkswagen Passat', 
                   'Volkswagen Virtus', 'Volkswagen CrossPolo'],

    'Volvo': ['Volvo S60', 'Volvo XC40', 'Volvo XC 90', 'Volvo S90', 'Volvo S 80', 
              'Volvo XC60', 'Volvo S60 Cross Country', 'Volvo V40'],

    'MG': ['MG Hector Plus', 'MG Hector', 'MG Astor', 'MG Comet EV', 'MG Gloster', 'MG ZS EV'],

    'Nissan': ['Nissan Terrano', 'Nissan Magnite', 'Nissan Micra Active', 'Nissan Sunny', 'Nissan Micra', 'Nissan Kicks'], 
    'Fiat': ['Fiat Linea', 'Fiat Punto Abarth', 'Fiat Punto', 'Fiat Punto EVO', 'Fiat Grande Punto', 
             'Fiat Palio', 'Fiat Punto Pure', 'Fiat Avventura', 'Fiat Abarth Avventura'],

    'Mahindra Ssangyong': ['Mahindra Ssangyong Rexton'],

    'Mitsubishi': ['Mitsubishi Cedia', 'Mitsubishi Lancer', 'Mitsubishi Pajero', 'Mitsubishi Outlander'],

    'Jaguar': ['Jaguar XF', 'Jaguar F-Pace', 'Jaguar XE', 'Jaguar XJ', 'Jaguar F-TYPE'], 

    'Land Rover': ['Land Rover Discovery Sport', 'Land Rover Freelander 2', 'Land Rover Range Rover Sport', 
                   'Land Rover Range Rover Velar', 'Land Rover Range Rover Evoque', 'Land Rover Defender', 
                   'Land Rover Discovery', 'Land Rover Range Rover'], 

    'Chevrolet': ['Chevrolet Cruze', 'Chevrolet Beat', 'Chevrolet Spark', 'Chevrolet Tavera', 'Chevrolet Enjoy', 
                  'Chevrolet Aveo', 'Chevrolet Optra', 'Chevrolet Captiva', 'Chevrolet Aveo U-VA', 'Chevrolet Sail'], 

    'Citroen': ['Citroen C5 Aircross', 'Citroen C3'], 

    'Opel': ['OpelCorsa'],

    'Mahindra Renault': ['Mahindra Renault Logan'], 

    'Isuzu': ['Isuzu MU 7', 'Isuzu MU-X', 'Isuzu D-Max'], 

    'Lexus': ['Lexus ES', 'Lexus RX'], 

    'Porsche': ['Porsche Cayenne', 'Porsche Macan', 'Porsche 911', 'Porsche Panamera'], 

    'Hindustan Motors': ['Hindustan Motors Contessa']
}

city_list = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata']

try:
    with col1:
        car_name = st.selectbox("Car Name", options=list(car_model_list.keys()))
        car_models = car_model_list.get(car_name, [])
        kms_driven = st.number_input("Kilometers Driven", min_value=0, step=500, value=50000)
        engine = st.number_input("Engine (cc)", min_value=500, step=50, value=1200)
        no_of_years = st.number_input("Age of Car (Years)", min_value=0, step=1, value=5)

    with col2:
        car_model = st.selectbox("Car Model", options=car_models)
        city_name = st.selectbox("City", options=city_list)
        owner = st.selectbox("Number of Previous Owners", options=[0, 1, 2, 3])
        mileage = st.number_input("Mileage (kmpl)", min_value=5.0, step=0.5, value=15.0)

    with col3:
        fuel_type = st.selectbox("Fuel Type", options=["Diesel", "Petrol", "CNG", "LPG", "Electric"])
        transmission = st.selectbox("Transmission", options=["Manual", "Automatic"])
        max_power = st.number_input("Max Power (bhp)", min_value=40.0, step=0.5, value=80.0)
        
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