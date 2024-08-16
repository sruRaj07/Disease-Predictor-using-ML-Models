# Disease-Predictor-using-ML-Models
In this project I have used Machine Learning Models to predict different types of Diseases like Diabetes, Heart Diseases etc.

Here is a detailed and professional README file template for your project. This template is designed to be informative and accessible to a global audience, with clear instructions and descriptions.

---

# **Disease Prediction Web Application**

## **Overview**

This web application predicts the likelihood of three diseases: **Heart Disease**, **Parkinson's Disease**, and **Diabetes**. The predictions are based on machine learning models developed using Python libraries such as `numpy`, `pandas`, `scikit-learn`, and `streamlit` for the web interface. This tool is designed to assist healthcare professionals and researchers in assessing the risk of these diseases based on patient data.

## **Table of Contents**

- [Project Structure](#project-structure)
- [Datasets](#datasets)
- [Machine Learning Models](#machine-learning-models)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## **Project Structure**

```
.
├── data/
│   ├── heart.csv
│   ├── parkinsons.csv
│   └── diabetes.csv
├── models/
│   ├── heart_model.pkl
│   ├── parkinsons_model.pkl
│   └── diabetes_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

- **`data/`**: Contains the datasets used for training the models.
- **`models/`**: Contains the serialized machine learning models for each disease.
- **`app.py`**: The main file for running the Streamlit web application.
- **`requirements.txt`**: Lists all Python dependencies required for the project.
- **`README.md`**: This file, explaining the project and how to use it.

## **Datasets**

1. **Heart Disease Dataset**:
   - **Features**: Age, sex, chest pain type, resting blood pressure, cholesterol level, etc.
   - **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)

2. **Parkinson's Disease Dataset**:
   - **Features**: Various vocal measurements such as MDVP (Fo), MDVP (Fhi), MDVP (Flo), etc.
   - **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Parkinsons)

3. **Diabetes Dataset**:
   - **Features**: Pregnancies, glucose level, blood pressure, skin thickness, insulin, BMI, age, etc.
   - **Source**: [Kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database)

## **Machine Learning Models**

- **Heart Disease Prediction**:
  - **Algorithm**: Logistic Regression
  - **Accuracy**: Approximately 85%

- **Parkinson's Disease Prediction**:
  - **Algorithm**: Support Vector Machine (SVM)
  - **Accuracy**: Approximately 90%

- **Diabetes Prediction**:
  - **Algorithm**: Random Forest Classifier
  - **Accuracy**: Approximately 80%

**Note**: The accuracy of the models may vary based on the data and the preprocessing techniques applied.

## **Installation**

Follow these steps to set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/disease-prediction-app.git
   cd disease-prediction-app
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

1. **Run the Streamlit application**:

   ```bash
   streamlit run app.py
   ```

2. **Access the application**:

   Open your browser and go to `http://localhost:8501/` to use the web interface.

3. **Make Predictions**:

   - Select the disease type (Heart, Parkinson's, Diabetes).
   - Input the necessary features.
   - Click on the "Predict" button to see the results.

## **Results**

- The application provides predictions with confidence scores for each of the three diseases based on the input features.
- The results are displayed on the web interface, along with a summary of the model's decision.

## **Future Enhancements**

- **Model Improvement**: Explore and implement advanced machine learning algorithms to improve prediction accuracy.
- **Additional Diseases**: Expand the application to include predictions for more diseases.
- **User Interface**: Enhance the UI/UX of the application for better user experience.
- **Mobile Support**: Adapt the application for mobile device compatibility.

## **Contributing**

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

This README file provides a comprehensive overview of your project, making it accessible to users and developers from around the world. Make sure to update the placeholder URLs and any specific project details as needed.
