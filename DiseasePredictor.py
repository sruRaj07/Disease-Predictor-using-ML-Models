# Webapp using Streamlit
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np  # Added for type conversion

# Function to load models safely
def load_model(file_path):
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error(f"Error: Model file '{file_path}' not found.")
        return None
    except Exception as e:
        st.error(f"Error loading model '{file_path}': {e}")
        return None

# Loading saved models
breast_cancer_model = load_model('Saved Models/breast_cancer_model.sav')
diabetes_model = load_model('Saved Models/diabetes_model.sav')
heart_disease_model = load_model('Saved Models/heart_disease_model.sav')
kidney_disease_model = load_model('Saved Models/kidney_disease.sav')
covid_disease_model = load_model('Saved Models/Covid19_model.sav')

# Sidebar
with st.sidebar:
    select = option_menu(
        'Disease Prediction Systems',
        ['Home', 'Covid-19 Disease Prediction', 'Breast Cancer Prediction', 
         'Diabetes Prediction', 'Heart Disease Prediction', 'Kidney Disease Prediction', 
         'Our Services'],
        icons=['house', 'activity', 'activity', 'person', 'heart', 'activity', 'gear'],
        default_index=0
    )

# Home Page
if select == 'Home':
    st.title('Welcome to Disease Predictor')
    st.write("""
    This website helps predict the likelihood of developing a disease using 
    machine learning models based on patient history and medical data.
    **Note:** This is not a substitute for medical consultation.
    """)

# Breast Cancer Prediction
if select == 'Breast Cancer Prediction' and breast_cancer_model:
    st.title('Breast Cancer Prediction using Machine Learning')

    # Collect user input
    inputs = [st.text_input(f'Enter {feature}') for feature in [
        'radius mean', 'texture mean', 'perimeter mean', 'area mean', 'smoothness mean', 
        'compactness mean', 'concavity mean', 'concave points mean', 'symmetry mean', 'fractal dimension mean',
        'radius se', 'texture se', 'perimeter se', 'area se', 'smoothness se', 'compactness se',
        'concavity se', 'concave points se', 'symmetry se', 'fractal dimension se',
        'radius worst', 'texture worst', 'perimeter worst', 'area worst', 'smoothness worst',
        'compactness worst', 'concavity worst', 'concave points worst', 'symmetry worst', 'fractal dimension worst'
    ]]

    # Predict if button clicked
    if st.button('Breast Cancer Test Result'):
        try:
            # Convert inputs to float and reshape for model
            user_data = np.array([float(i) for i in inputs]).reshape(1, -1)
            prediction = breast_cancer_model.predict(user_data)

            result = 'Patient has breast cancer' if prediction[0] == 1 else 'Patient does not have breast cancer'
            st.success(result)
        except ValueError:
            st.error("Please enter valid numeric inputs.")

# Diabetes Prediction
if select == 'Diabetes Prediction' and diabetes_model:
    st.title('Diabetes Prediction using Machine Learning')

    # Collect user input
    inputs = [st.text_input(f'Enter {feature}') for feature in [
        'Number of Pregnancies', 'Glucose', 'Blood Pressure', 'Skin Thickness', 
        'Insulin', 'BMI', 'Diabetes Pedigree Function', 'Age', 'Skin'
    ]]

    if st.button('Diabetes Test Result'):
        try:
            user_data = np.array([float(i) for i in inputs]).reshape(1, -1)
            prediction = diabetes_model.predict(user_data)

            result = 'Patient has diabetes' if prediction[0] == 1 else 'Patient does not have diabetes'
            st.success(result)
        except ValueError:
            st.error("Please enter valid numeric inputs.")

# Heart Disease Prediction
if select == 'Heart Disease Prediction' and heart_disease_model:
    st.title('Heart Disease Prediction using Machine Learning')

    inputs = [st.text_input(f'Enter {feature}') for feature in [
        'Age', 'Sex', 'Cp', 'Trestbps', 'Chol', 'Fbs', 'Restecg', 
        'Thalach', 'Exang', 'Oldpeak', 'Slope', 'Ca', 'Thal'
    ]]

    if st.button('Heart Disease Test Result'):
        try:
            user_data = np.array([float(i) for i in inputs]).reshape(1, -1)
            prediction = heart_disease_model.predict(user_data)

            result = 'Patient has heart disease' if prediction[0] == 1 else 'Patient does not have heart disease'
            st.success(result)
        except ValueError:
            st.error("Please enter valid numeric inputs.")

# Kidney Disease Prediction
if select == 'Kidney Disease Prediction' and kidney_disease_model:
    st.title('Kidney Disease Prediction using Machine Learning')

    inputs = [st.text_input(f'Enter {feature}') for feature in [
        'Bp', 'Sp', 'Al', 'Su', 'Rbc', 'Bu', 'Sc', 'Sod', 'Pot', 'Hemo', 'Wbcc', 'Rbcc', 'Htn'
    ]]

    if st.button('Kidney Disease Test Result'):
        try:
            user_data = np.array([float(i) for i in inputs]).reshape(1, -1)
            prediction = kidney_disease_model.predict(user_data)

            result = 'Patient has kidney disease' if prediction[0] == 1 else 'Patient does not have kidney disease'
            st.success(result)
        except ValueError:
            st.error("Please enter valid numeric inputs.")

# Covid-19 Prediction
if select == 'Covid-19 Disease Prediction' and covid_disease_model:
    st.title('Covid-19 Prediction using Machine Learning')

    Age = st.text_input('Enter Your Age')
    BodyTemp = st.text_input('Enter Your Body Temperature')
    
    symptoms = {'Fatigue': 0, 'Cough': 0, 'Body Pain': 0, 'Sore Throat': 0, 'Breathing Difficulty': 0}
    for symptom in symptoms:
        symptoms[symptom] = 1 if st.radio(f'Do you have {symptom.lower()}?', ('Yes', 'No')) == 'Yes' else 0

    if st.button('Covid-19 Prediction Test Result'):
        try:
            user_data = np.array([float(Age), float(BodyTemp)] + list(symptoms.values())).reshape(1, -1)
            prediction = covid_disease_model.predict(user_data)

            result = 'Patient has Covid-19' if prediction[0] == 1 else 'Patient does not have Covid-19'
            st.success(result)
        except ValueError:
            st.error("Please enter valid numeric inputs.")