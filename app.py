import pickle

import streamlit as st
import pandas as pd

from tensorflow.keras.models import load_model

from src.config import (
    MODEL_PATH,
    SCALER_PATH,
    FEATURE_COLUMNS,
    DEFAULT_THRESHOLD,
    LOW_RISK_THRESHOLD,
    HIGH_RISK_THRESHOLD,
)

from src.preprocessing import preprocess_input


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Credit Card Default Prediction",
    page_icon="💳",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_prediction_model():

    model = load_model(MODEL_PATH)

    return model


# ============================================================
# LOAD SCALER
# ============================================================

@st.cache_resource
def load_scaler():

    with open(SCALER_PATH, "rb") as file:
        scaler = pickle.load(file)

    return scaler


# ============================================================
# LOAD EVERYTHING
# ============================================================

try:

    model = load_prediction_model()
    scaler = load_scaler()

except Exception as e:

    st.error(
        "Unable to load the trained model or scaler."
    )

    st.exception(e)

    st.stop()


# ============================================================
# HEADER
# ============================================================

st.title("💳 Credit Card Default Prediction")

st.markdown(
    """
    Enter the customer's financial and repayment information
    to estimate the probability of credit-card default.
    """
)

st.divider()


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:

    limit_bal = st.number_input(
        "Credit Limit",
        min_value=0.0,
        value=200000.0,
        step=5000.0
    )

with col2:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35,
        step=1
    )

with col3:

    sex = st.selectbox(
        "Gender",
        options=[1, 2],
        format_func=lambda x:
            "Male" if x == 1 else "Female"
    )


col1, col2 = st.columns(2)

with col1:

    education = st.selectbox(
        "Education",
        options=[1, 2, 3, 4],
        format_func=lambda x: {
            1: "Graduate School",
            2: "University",
            3: "High School",
            4: "Others"
        }[x]
    )

with col2:

    marriage = st.selectbox(
        "Marital Status",
        options=[1, 2, 3],
        format_func=lambda x: {
            1: "Married",
            2: "Single",
            3: "Others"
        }[x]
    )


# ============================================================
# PAYMENT HISTORY
# ============================================================

st.subheader("📊 Repayment Status")

st.caption(
    "Use the dataset's payment-status encoding. "
    "-2 to 8 are valid values."
)

pay_col1, pay_col2, pay_col3 = st.columns(3)

with pay_col1:

    pay_0 = st.number_input(
        "PAY_0",
        min_value=-2,
        max_value=8,
        value=0,
        step=1
    )

    pay_2 = st.number_input(
        "PAY_2",
        min_value=-2,
        max_value=8,
        value=0,
        step=1
    )

with pay_col2:

    pay_3 = st.number_input(
        "PAY_3",
        min_value=-2,
        max_value=8,
        value=0,
        step=1
    )

    pay_4 = st.number_input(
        "PAY_4",
        min_value=-2,
        max_value=8,
        value=0,
        step=1
    )

with pay_col3:

    pay_5 = st.number_input(
        "PAY_5",
        min_value=-2,
        max_value=8,
        value=0,
        step=1
    )

    pay_6 = st.number_input(
        "PAY_6",
        min_value=-2,
        max_value=8,
        value=0,
        step=1
    )


# ============================================================
# BILL AMOUNTS
# ============================================================

st.subheader("💰 Bill Amounts")

bill_col1, bill_col2, bill_col3 = st.columns(3)

with bill_col1:

    bill_amt1 = st.number_input(
        "Bill Amount 1",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )

    bill_amt2 = st.number_input(
        "Bill Amount 2",
        min_value=0.0,
        value=48000.0,
        step=1000.0
    )

with bill_col2:

    bill_amt3 = st.number_input(
        "Bill Amount 3",
        min_value=0.0,
        value=45000.0,
        step=1000.0
    )

    bill_amt4 = st.number_input(
        "Bill Amount 4",
        min_value=0.0,
        value=43000.0,
        step=1000.0
    )

with bill_col3:

    bill_amt5 = st.number_input(
        "Bill Amount 5",
        min_value=0.0,
        value=40000.0,
        step=1000.0
    )

    bill_amt6 = st.number_input(
        "Bill Amount 6",
        min_value=0.0,
        value=38000.0,
        step=1000.0
    )


# ============================================================
# PAYMENT AMOUNTS
# ============================================================

st.subheader("💵 Previous Payment Amounts")

payment_col1, payment_col2, payment_col3 = st.columns(3)

with payment_col1:

    pay_amt1 = st.number_input(
        "Payment Amount 1",
        min_value=0.0,
        value=3000.0,
        step=500.0
    )

    pay_amt2 = st.number_input(
        "Payment Amount 2",
        min_value=0.0,
        value=3000.0,
        step=500.0
    )

with payment_col2:

    pay_amt3 = st.number_input(
        "Payment Amount 3",
        min_value=0.0,
        value=3000.0,
        step=500.0
    )

    pay_amt4 = st.number_input(
        "Payment Amount 4",
        min_value=0.0,
        value=3000.0,
        step=500.0
    )

with payment_col3:

    pay_amt5 = st.number_input(
        "Payment Amount 5",
        min_value=0.0,
        value=3000.0,
        step=500.0
    )

    pay_amt6 = st.number_input(
        "Payment Amount 6",
        min_value=0.0,
        value=3000.0,
        step=500.0
    )


# ============================================================
# CREATE INPUT DICTIONARY
# ============================================================

input_data = {

    "LIMIT_BAL": limit_bal,

    "SEX": sex,

    "EDUCATION": education,

    "MARRIAGE": marriage,

    "AGE": age,

    "PAY_0": pay_0,
    "PAY_2": pay_2,
    "PAY_3": pay_3,
    "PAY_4": pay_4,
    "PAY_5": pay_5,
    "PAY_6": pay_6,

    "BILL_AMT1": bill_amt1,
    "BILL_AMT2": bill_amt2,
    "BILL_AMT3": bill_amt3,
    "BILL_AMT4": bill_amt4,
    "BILL_AMT5": bill_amt5,
    "BILL_AMT6": bill_amt6,

    "PAY_AMT1": pay_amt1,
    "PAY_AMT2": pay_amt2,
    "PAY_AMT3": pay_amt3,
    "PAY_AMT4": pay_amt4,
    "PAY_AMT5": pay_amt5,
    "PAY_AMT6": pay_amt6,
}


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🔍 Predict Credit Default Risk",
    type="primary",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    try:

        # ----------------------------------------------------
        # Preprocess
        # ----------------------------------------------------

        processed_data = preprocess_input(
            input_data,
            scaler
        )


        # ----------------------------------------------------
        # Model prediction
        # ----------------------------------------------------

        probability = model.predict(
            processed_data,
            verbose=0
        )[0][0]


        probability_percent = probability * 100


        # ----------------------------------------------------
        # Classification
        # ----------------------------------------------------

        prediction = int(
            probability >= DEFAULT_THRESHOLD
        )


        # ----------------------------------------------------
        # Risk category
        # ----------------------------------------------------

        if probability < LOW_RISK_THRESHOLD:

            risk_level = "LOW RISK"
            risk_color = "green"

        elif probability < HIGH_RISK_THRESHOLD:

            risk_level = "MEDIUM RISK"
            risk_color = "orange"

        else:

            risk_level = "HIGH RISK"
            risk_color = "red"


        # ----------------------------------------------------
        # Results
        # ----------------------------------------------------

        st.divider()

        st.subheader("Prediction Result")

        result_col1, result_col2, result_col3 = st.columns(3)

        with result_col1:

            st.metric(
                "Default Probability",
                f"{probability_percent:.2f}%"
            )

        with result_col2:

            if prediction == 1:

                st.error("⚠️ DEFAULT PREDICTED")

            else:

                st.success("✅ NO DEFAULT PREDICTED")

        with result_col3:

            if risk_color == "green":

                st.success(risk_level)

            elif risk_color == "orange":

                st.warning(risk_level)

            else:

                st.error(risk_level)


        # ----------------------------------------------------
        # Probability bar
        # ----------------------------------------------------

        st.write("Probability of Default")

        st.progress(
            float(probability)
        )


        # ----------------------------------------------------
        # Explanation
        # ----------------------------------------------------

        if prediction == 1:

            st.warning(
                f"The model estimates a "
                f"{probability_percent:.2f}% probability "
                "of default."
            )

        else:

            st.success(
                f"The model estimates a "
                f"{probability_percent:.2f}% probability "
                "of default."
            )


    except Exception as e:

        st.error(
            "An error occurred while making the prediction."
        )

        st.exception(e)
