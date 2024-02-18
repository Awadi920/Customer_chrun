import streamlit as st
import pandas as pd
import pickle
import time
knn_model = pickle.load(open("knn_Model.pickle", "rb"))

knn_Model.pickle
# Noms des caractéristiques utilisées lors de l'ajustement du modèle
feature_names = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
                 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling',
                 'MonthlyCharges', 'TotalCharges', 'InternetService_DSL',
                 'InternetService_Fiber optic', 'InternetService_No',
                 'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year',
                 'PaymentMethod_Bank transfer (automatic)',
                 'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check',
                 'PaymentMethod_Mailed check']

# Fonction pour prédire la churn
def predict_churn(input_data):
    # Simuler un délai de traitement pour la barre de progression
    with st.spinner('Predicting...'):
        time.sleep(2)  # Simuler un calcul de prédiction
        prediction = knn_model.predict(input_data)
    return prediction

# Titre de l'application
st.title('Predict Customer Churn')

# Description de chaque champ
st.write('Enter customer details:')

# Formulaire pour saisir les valeurs des attributs
gender = st.selectbox('Gender', ['Male', 'Female'])
senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])
partner = st.selectbox('Partner', ['No', 'Yes'])
dependents = st.selectbox('Dependents', ['No', 'Yes'])
tenure = st.number_input('Tenure (Months)', min_value=0)
phone_service = st.selectbox('Phone Service', ['No', 'Yes'])
multiple_lines = st.selectbox('Multiple Lines', ['No', 'Yes'])
online_security = st.selectbox('Online Security', ['No', 'Yes'])
online_backup = st.selectbox('Online Backup', ['No', 'Yes'])
device_protection = st.selectbox('Device Protection', ['No', 'Yes'])
tech_support = st.selectbox('Tech Support', ['No', 'Yes'])
streaming_tv = st.selectbox('Streaming TV', ['No', 'Yes'])
streaming_movies = st.selectbox('Streaming Movies', ['No', 'Yes'])
paperless_billing = st.selectbox('Paperless Billing', ['No', 'Yes'])
monthly_charges = st.number_input('Monthly Charges')
total_charges = st.number_input('Total Charges')
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
payment_method = st.selectbox('Payment Method', ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])

# Convertir les valeurs sélectionnées en format attendu par le modèle
gender = 1 if gender == 'Female' else 0
senior_citizen = 1 if senior_citizen == 'Yes' else 0
partner = 1 if partner == 'Yes' else 0
dependents = 1 if dependents == 'Yes' else 0
phone_service = 1 if phone_service == 'Yes' else 0
multiple_lines = 1 if multiple_lines == 'Yes' else 0
online_security = 1 if online_security == 'Yes' else 0
online_backup = 1 if online_backup == 'Yes' else 0
device_protection = 1 if device_protection == 'Yes' else 0
tech_support = 1 if tech_support == 'Yes' else 0
streaming_tv = 1 if streaming_tv == 'Yes' else 0
streaming_movies = 1 if streaming_movies == 'Yes' else 0
paperless_billing = 1 if paperless_billing == 'Yes' else 0
internet_service_dsl = 1 if internet_service == 'DSL' else 0
internet_service_fiber_optic = 1 if internet_service == 'Fiber optic' else 0
internet_service_no = 1 if internet_service == 'No' else 0
contract_month_to_month = 1 if contract == 'Month-to-month' else 0
contract_one_year = 1 if contract == 'One year' else 0
contract_two_year = 1 if contract == 'Two year' else 0
payment_method_bank_transfer = 1 if payment_method == 'Bank transfer (automatic)' else 0
payment_method_credit_card = 1 if payment_method == 'Credit card (automatic)' else 0
payment_method_electronic_check = 1 if payment_method == 'Electronic check' else 0
payment_method_mailed_check = 1 if payment_method == 'Mailed check' else 0

# Créer un DataFrame avec les valeurs saisies par l'utilisateur
input_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [senior_citizen],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'OnlineSecurity': [online_security],
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'PaperlessBilling': [paperless_billing],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges],
    'InternetService_DSL': [internet_service_dsl],
    'InternetService_Fiber optic': [internet_service_fiber_optic],
    'InternetService_No': [internet_service_no],
    'Contract_Month-to-month': [contract_month_to_month],
    'Contract_One year': [contract_one_year],
    'Contract_Two year': [contract_two_year],
    'PaymentMethod_Bank transfer (automatic)': [payment_method_bank_transfer],
    'PaymentMethod_Credit card (automatic)': [payment_method_credit_card],
    'PaymentMethod_Electronic check': [payment_method_electronic_check],
    'PaymentMethod_Mailed check': [payment_method_mailed_check]
})

# Vérifier si les noms des caractéristiques correspondent
if set(input_data.columns) != set(feature_names):
    st.error(f"Feature names mismatch. Expected: {feature_names}, but got: {input_data.columns}.")
else:
    # Prédire la churn en utilisant le modèle KNN
    if st.button('Predict'):
        with st.spinner(text='Predicting...'):
            prediction = predict_churn(input_data)
            if prediction[0] == 1:
                st.success('The customer is likely to churn.')
            else:
                st.success('The customer is not likely to churn.')
            
