import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load the dataset from the new directory path
#file_path = "/Users/vipul/Downloads/CodeClause/Credit Card Fraud Detection/creditcard.csv"
#cred_card_data = pd.read_csv(file_path)

# Separate data for analysis
#legit = cred_card_data[cred_card_data.Class == 0]
#fraud = cred_card_data[cred_card_data.Class == 1]
#legit_sample = legit.sample(n=492)

# Create a balanced dataset
#new_dataset = pd.concat([legit_sample, fraud], axis=0)

# Split the data into features and targets
#X = new_dataset.drop(columns="Class", axis=1)
#Y = new_dataset["Class"]

# Split the data into training and testing sets
#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the Logistic Regression model
#model = LogisticRegression()
#model.fit(X_train, Y_train)

# Save the trained model using pickle
#with open('model.pkl', 'wb') as file:
 #   pickle.dump(model, file)

# Streamlit App
def main():
    st.title('Credit Card Fraud Detection')

    # Load the trained model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    st.markdown('## Enter Transaction Details')

    input_data = {}

    for idx, column in enumerate(X.columns):
        unique_key = f"{column}_input_{idx}"  # Unique key for each input widget
        st.markdown(f"<span style='font-weight: bold;'>{column}</span>", unsafe_allow_html=True)
        input_data[column] = st.number_input(label="", format="%.2f", step=0.01, key=unique_key)


    if st.button('Predict'):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)

        # Display prediction on the main page
        st.markdown('## Prediction Result')
        if prediction[0] == 0:
            st.success('Prediction: Legitimate Transaction')
        else:
            st.error('Prediction: Fraudulent Transaction')

if __name__ == '__main__':
    main()



page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://r4.wallpaperflare.com/wallpaper/850/74/373/business-buy-card-commercial-wallpaper-836f37178e025794e66a6af4640d7f0a.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

hide_st_style = '''
<style> footer {visibility: hidden;} 
</style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)

footer_html = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    color: white; /* Text color */
    padding: 10px;
    text-align: center; /* Center the text */
    font-size: 18px; /* Adjust the font size */
}
</style>
<div class="footer">Made by Vipul Malyan</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
