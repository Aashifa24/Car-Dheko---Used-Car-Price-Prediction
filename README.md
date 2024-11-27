# Car Dheko - Used Car Price Predictor App 🚗

## Overview

**Car Dheko** is an interactive web application built with **Streamlit** that predicts the price of a used car based on user-provided features such as car make, model, kilometers driven, engine capacity, and more. The app uses a machine learning model trained with a **Random Forest Regressor** to predict the car price in real time.

---

## Project Files

The following files are included in the project:

- **`project.ipynb`**: The Jupyter Notebook containing the overall code for data analysis, preprocessing, feature engineering, and model training.
- **`car_dekho_project_report.pdf`**: A comprehensive report detailing the project overview, objectives, methodology, and justification behind the model and approach.
- **`user_guide.pdf`**: A user guide explaining how to use the Streamlit application for car price prediction.
- **`demo.zip`**: A zipped folder of demo video showcasing how the Streamlit app works and how users can interact with it.
- **`app.py`**: The Streamlit Python script that implements the interactive web application for car price prediction.
- **`cleaned_cars_dataset.csv`**: The cleaned dataset used for model training, containing all the relevant car features.

---

## Features

### 1. **Car Price Prediction**
   - The app predicts the price of a used car based on multiple input features such as make, model, kilometers driven, engine capacity, fuel type, and more.

### 2. **Interactive Input Fields**
   - The app provides dynamic dropdowns for selecting the car's make, city, fuel type, and transmission type.
   - Numerical input fields for entering car attributes like kilometers driven, engine size, mileage, etc.

### 3. **Real-Time Predictions**
   - The app uses a pre-trained **Random Forest Regression Model** to predict car prices instantly based on user inputs.

### 4. **Error Handling & Input Validation**
   - The app checks for missing or invalid inputs and provides clear error messages to guide users in correcting any mistakes.

### 5. **Customizable Background**
   - The app includes a visually appealing car-themed background.

### 6. **User-Friendly Interface**
   - Bright, bold text with an intuitive layout to enhance user interaction and overall experience.

---

## Example Use Case

**Scenario**:  
A customer wishes to sell a **Hyundai** car with the following details:
- **Kilometers Driven**: 40,000 km
- **Engine Capacity**: 1600 cc
- **Car Age**: 5 years
- **Fuel Type**: Diesel
- **Transmission**: Manual
- **Mileage**: 19 kmpl
- **Max Power**: 115 bhp
- **Location**: Chennai
- **Previous Owners**: 1

**Steps**:
1. The customer inputs these details into the app.
2. Clicking the "Predict Price" button, the app provides an estimated price (e.g., ₹7.65 Lakhs).
3. The customer uses this predicted price to set a competitive selling price.

---

## Getting Started

### Prerequisites

Make sure you have the following installed:
- **Python 3.7 or higher**
- The necessary Python libraries:
    ```bash
    pip install streamlit pandas pickle pillow
    ```

### Launching the Application

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/car-dheko.git
    cd car-dheko
    ```

2. Ensure that the **model file** (`rf_regression_model.pkl`), **background image**, and all necessary files are in the correct directory.

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

---

## Handling Errors

- **Input Validation**: If there are missing or incorrect inputs (e.g., invalid car name or negative values), the app will display appropriate error messages.
    - Example: "Kilometers Driven must be greater than 0."
    - Example: "Engine(cc) must be greater than or equal to 500."

- **Model Loading Errors**: If the machine learning model fails to load, an error message will notify the user.
    - Example: "Model file not found. Please ensure it exists at the specified location."

- **Prediction Errors**: If something goes wrong during the prediction process, the app will display an error message.
    - Example: "Prediction failed. Please try again."

---

## System Requirements

- **Python 3.7 or higher**
- Libraries:
    - `streamlit`
    - `pandas`
    - `pickle`
    - `pillow`
- **Machine Learning Model File**:
    - `rf_regression_model.pkl`

---

## How to Contribute

We welcome contributions! To contribute:
1. Fork the repository.
2. Make changes or improvements.
3. Submit a pull request with a description of the changes.



## Credits

- **Developer**: Aashifa
- **© 2024 Car Dheko - Enhancing Customer Experience with Machine Learning
