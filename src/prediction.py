import pickle

from tensorflow.keras.models import load_model

from src.config import (
    MODEL_PATH,
    SCALER_PATH,
    DEFAULT_THRESHOLD,
    LOW_RISK_THRESHOLD,
    HIGH_RISK_THRESHOLD,
)

from src.preprocessing import preprocess_input


# ============================================================
# LOAD SCALER
# ============================================================

with open(SCALER_PATH, "rb") as file:
    scaler = pickle.load(file)


# ============================================================
# LOAD KERAS MODEL
# ============================================================

model = load_model(
    MODEL_PATH,
    compile=False
)


# ============================================================
# PREDICTION
# ============================================================

def predict_customer(data: dict) -> dict:
    """
    Predict credit card default probability for one customer.

    Parameters
    ----------
    data : dict
        Raw customer information.

    Returns
    -------
    dict
        Probability, prediction class, and application risk level.
    """

    # --------------------------------------------------------
    # Preprocess input
    # --------------------------------------------------------

    processed = preprocess_input(
        data,
        scaler
    )

    # --------------------------------------------------------
    # Generate probability
    # --------------------------------------------------------

    probability = float(
        model.predict(
            processed,
            verbose=0
        )[0][0]
    )

    # --------------------------------------------------------
    # Convert probability to class
    # --------------------------------------------------------

    prediction = int(
        probability >= DEFAULT_THRESHOLD
    )

    # --------------------------------------------------------
    # Application-level risk classification
    # --------------------------------------------------------

    if probability < LOW_RISK_THRESHOLD:

        risk = "LOW"

    elif probability < HIGH_RISK_THRESHOLD:

        risk = "MEDIUM"

    else:

        risk = "HIGH"

    # --------------------------------------------------------
    # Return result
    # --------------------------------------------------------

    return {
        "probability": probability,
        "prediction": prediction,
        "risk": risk,
    }
