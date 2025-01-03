import pickle
import streamlit as st
import urllib.request
import io

# URL to the raw model file on GitHub
url = "https://raw.githubusercontent.com/umeshpardeshi9545/titanic-survival-model/main/Titanic_model.pkl"

# Load the model from the URL
try:
    with urllib.request.urlopen(url) as response:
        model_data = response.read()
        model = pickle.load(io.BytesIO(model_data))
    print("Model loaded successfully!")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

def main():
    st.title("Survived or Not")
    
    # Input variables
    Pclass = st.text_input("Pclass (Passenger Class)")
    Age = st.text_input("Age")
    SibSp = st.text_input("Siblings/Spouses Aboard")
    Parch = st.text_input("Parents/Children Aboard")
    Fare = st.text_input("Fare")
    Sex_male = st.text_input("Sex (Male: 1, Female: 0)")
    Embarked_Q = st.text_input("Embarked at Queenstown (1 for Yes, 0 for No)")
    Embarked_S = st.text_input("Embarked at Southampton (1 for Yes, 0 for No)")

    # Prediction
    if st.button("Predict"):
        if model is None:
            st.error("The model could not be loaded. Please check the file URL or format.")
            return
        
        try:
            inputs = [float(Pclass), float(Age), float(SibSp), float(Parch), float(Fare), 
                      float(Sex_male), float(Embarked_Q), float(Embarked_S)]
            prediction = model.predict([inputs])
            st.success(f"The prediction is: {'Survived' if prediction[0] == 1 else 'Did not survive'}")
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

if __name__ == '__main__':
    main()





"""
import pickle
import streamlit as st
import urllib.request
import io

# URL to the raw model file on GitHub
url = "https://raw.githubusercontent.com/umeshpardeshi9545/titanic-survival-model/main/Titanic_model.pkl"

# Load the model from the URL
try:
    with urllib.request.urlopen(url) as response:
        model_data = response.read()  # Read response as bytes
        model = pickle.load(io.BytesIO(model_data))  # Use io.BytesIO to handle the bytes
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

# Load the model with a corrected file path
#model = pickle.load(open('Titanic_model.pkl', "rb"))

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

"""
