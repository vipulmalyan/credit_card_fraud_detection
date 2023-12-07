import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle



X=pickle.load(open("features.pkl","rb"))

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
