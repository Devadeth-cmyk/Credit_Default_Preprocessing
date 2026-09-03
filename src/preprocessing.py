import pandas as pd

from src.config import (
    FEATURE_COLUMNS,
    NUMERICAL_COLUMNS,
)


def preprocess_input(data: dict):
    """
    Preprocess a single customer's input.

    The preprocessing follows the same logic used in the
    training notebook:

    1. Create DataFrame
    2. Replace invalid EDUCATION values
    3. Replace invalid MARRIAGE value
    4. Keep the exact 23 feature columns
    5. Scale the 14 numerical columns using the saved scaler
    """

    # --------------------------------------------------------
    # 1. Convert input dictionary to DataFrame
    # --------------------------------------------------------

    df = pd.DataFrame([data])


    # --------------------------------------------------------
    # 2. Validate required columns
    # --------------------------------------------------------

    missing_columns = [
        column
        for column in FEATURE_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required features: {missing_columns}"
        )

    # --------------------------------------------------------
    # Basic numerical validation
    # --------------------------------------------------------

    if data["LIMIT_BAL"] < 0:
        raise ValueError("LIMIT_BAL cannot be negative.")

    if not 18 <= data["AGE"] <= 100:
        raise ValueError("AGE must be between 18 and 100.")


    # --------------------------------------------------------
    # SEX
    # Dataset encoding:
    # 1 = male
    # 2 = female
    # --------------------------------------------------------

    if data["SEX"] not in [1, 2]:
        raise ValueError("SEX must be 1 or 2.")


    # --------------------------------------------------------
    # EDUCATION
    # Dataset values after preprocessing:
    # 1, 2, 3, 4
    # --------------------------------------------------------

    if data["EDUCATION"] not in [0, 1, 2, 3, 4, 5, 6]:
        raise ValueError(
            "EDUCATION must be one of: 0, 1, 2, 3, 4, 5, 6."
        )


    # --------------------------------------------------------
    # MARRIAGE
    # 0 is allowed because notebook converts it to 3.
    # --------------------------------------------------------

    if data["MARRIAGE"] not in [0, 1, 2, 3]:
        raise ValueError(
            "MARRIAGE must be one of: 0, 1, 2, 3."
        )


    # --------------------------------------------------------
    # Payment status
    # --------------------------------------------------------

    payment_columns = [
        "PAY_0",
        "PAY_2",
        "PAY_3",
        "PAY_4",
        "PAY_5",
        "PAY_6",
    ]

    for column in payment_columns:

        value = data[column]

        # Dataset normally uses -2 through 8
        if value < -2 or value > 8:
            raise ValueError(
                f"{column} must be between -2 and 8."
            )

def preprocess_input(data: dict, scaler):
    """
    Convert raw application input into the exact feature
    representation expected by the trained ANN.
    """

    # Validate first
    validate_input(data)

    # Create DataFrame
    df = pd.DataFrame([data])

    # --------------------------------------------------------
    # 3. Keep only model features
    # --------------------------------------------------------

    df = df[FEATURE_COLUMNS].copy()


    # --------------------------------------------------------
    # 4. Apply notebook preprocessing
    # --------------------------------------------------------

    # Notebook:
    # EDUCATION values 0, 5, 6 → 4
    df["EDUCATION"] = df["EDUCATION"].replace(
        [0, 5, 6],
        4
    )

    # Notebook:
    # MARRIAGE value 0 → 3
    df["MARRIAGE"] = df["MARRIAGE"].replace(
        [0],
        3
    )


    # --------------------------------------------------------
    # 5. Convert everything to numeric
    # --------------------------------------------------------

    for column in FEATURE_COLUMNS:
        df[column] = pd.to_numeric(
            df[column],
            errors="raise"
        )


    # --------------------------------------------------------
    # 6. Apply the SAVED StandardScaler
    # --------------------------------------------------------

    df[NUMERICAL_COLUMNS] = scaler.transform(
        df[NUMERICAL_COLUMNS]
    )


    # --------------------------------------------------------
    # 7. Final feature order check
    # --------------------------------------------------------

    df = df[FEATURE_COLUMNS]


    return df
