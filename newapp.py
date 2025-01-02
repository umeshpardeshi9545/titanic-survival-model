import pickle
import streamlit as st
import pickle
import requests
from io import BytesIO

# URL to the raw model file on GitHub
url = "https://github.com/umeshpardeshi9545/titanic-survival-model/blob/main/Titanic_model.pkl"

try:
    # Fetch the file
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for HTTP issues

    # Load the model
    model = pickle.load(BytesIO(response.content))

# Load the model with a corrected file path
#model = pickle.load(open(r'Titanic_model.pkl', "rb"))

def main():
    st.title("Survived or not")
    # Input variables
    Pclass = st.text_input("Pclass")
    Age = st.text_input("Age")  
    SibSp = st.text_input("SibSp")
    Parch = st.text_input("Parch")
    Fare = st.text_input("Fare")
    Sex_male = st.text_input("Sex_male")
    Embarked_Q = st.text_input("Embarked_Q")
    Embarked_S = st.text_input("Embarked_S")

    # Prediction
    if st.button("Predict"):
        try:
            # Ensure inputs are converted to the right types (e.g., float or int)
            makepred = model.predict([[float(Pclass), float(Age),float(SibSp), float(Parch), float(Fare), 
                                        float(Sex_male), float(Embarked_Q), float(Embarked_S)]])
            st.success(f"The prediction is: {makepred[0]}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
