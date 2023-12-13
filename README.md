# Credit Card Fraud Detection

![Project Image](https://r4.wallpaperflare.com/wallpaper/850/74/373/business-buy-card-commercial-wallpaper-836f37178e025794e66a6af4640d7f0a.jpg)

This project focuses on detecting fraudulent credit card transactions through machine learning techniques. It utilizes a Logistic Regression model trained on a dataset containing transactions made by European cardholders in September 2013.

## Introduction

Credit card fraud poses a significant challenge affecting financial institutions and cardholders globally. This project aims to leverage machine learning algorithms to identify and prevent fraudulent transactions, providing enhanced security for cardholders and financial systems.

## Features

- **Data**: The dataset consists of numerical features obtained via PCA transformation to ensure confidentiality.
- **Model**: Logistic Regression is employed for fraud detection.
- **Streamlit App**: A user-friendly interface is built using Streamlit, enabling users to input transaction details for prediction.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/vipulmalyan/credit-card-fraud-detection.git
    cd credit-card-fraud-detection
    ```

2. **Install necessary packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Access the app via the provided URL**.

3. **Enter transaction details** (amount, time, etc.) to predict if the transaction is legitimate or fraudulent.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
