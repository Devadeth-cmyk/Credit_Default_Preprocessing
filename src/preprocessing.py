import pandas as pd

from src.config import (
    FEATURE_COLUMNS,
    NUMERICAL_COLUMNS,
)


# ============================================================
# INPUT VALIDATION
# ============================================================

def validate_input(data: dict) -> None:
    """
    Validate a single customer's raw input.

    Validation is performed before applying the same
    preprocessing transformations used during training.
    """

    # --------------------------------------------------------
    # Required features
    # --------------------------------------------------------

    missing_columns = [
        column
        for column in FEATURE_COLUMNS
        if column not in data
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required features: {missing_columns}"
        )

    # --------------------------------------------------------
    # Check numeric values
    # --------------------------------------------------------

    for column in FEATURE_COLUMNS:

        value = data[column]

        if value is None:
            raise ValueError(
                f"{column} cannot be None."
            )

        try:
            float(value)
        except (TypeError, ValueError):
            raise ValueError(
                f"{column} must be numeric."
            )

    # --------------------------------------------------------
    # LIMIT_BAL
    # --------------------------------------------------------

    if float(data["LIMIT_BAL"]) < 0:
        raise ValueError(
            "LIMIT_BAL cannot be negative."
        )

    # --------------------------------------------------------
    # AGE
    # --------------------------------------------------------

    age = float(data["AGE"])

    if not 18 <= age <= 100:
        raise ValueError(
            "AGE must be between 18 and 100."
        )

    # --------------------------------------------------------
    # SEX
    # --------------------------------------------------------

    sex = int(float(data["SEX"]))

    if sex not in [1, 2]:
        raise ValueError(
            "SEX must be 1 or 2."
        )

    # --------------------------------------------------------
    # EDUCATION
    # --------------------------------------------------------

    education = int(float(data["EDUCATION"]))

    if education not in [0, 1, 2, 3, 4, 5, 6]:
        raise ValueError(
            "EDUCATION must be one of: 0, 1, 2, 3, 4, 5, 6."
        )

    # --------------------------------------------------------
    # MARRIAGE
    # --------------------------------------------------------

    marriage = int(float(data["MARRIAGE"]))

    if marriage not in [0, 1, 2, 3]:
        raise ValueError(
            "MARRIAGE must be one of: 0, 1, 2, 3."
        )

    # --------------------------------------------------------
    # PAYMENT STATUS
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

        value = float(data[column])

        # UCI dataset uses values from -2 to 8.
        if value < -2 or value > 8:
            raise ValueError(
                f"{column} must be between -2 and 8."
            )

    # --------------------------------------------------------
    # Monetary values
    # --------------------------------------------------------

    monetary_columns = [
        "LIMIT_BAL",
        "BILL_AMT1",
        "BILL_AMT2",
        "BILL_AMT3",
        "BILL_AMT4",
        "BILL_AMT5",
        "BILL_AMT6",
        "PAY_AMT1",
        "PAY_AMT2",
        "PAY_AMT3",
        "PAY_AMT4",
        "PAY_AMT5",
        "PAY_AMT6",
    ]

    for column in monetary_columns:

        if float(data[column]) < 0:
            raise ValueError(
                f"{column} cannot be negative."
            )


# ============================================================
# PREPROCESS INPUT
# ============================================================

def preprocess_input(
    data: dict,
    scaler
) -> pd.DataFrame:
    """
    Convert raw customer input into the exact feature
    representation expected by the trained Keras ANN.

    The preprocessing matches the notebook:

    1. Validate input.
    2. Create a DataFrame.
    3. Keep the exact 23 model features.
    4. Replace EDUCATION 0, 5, 6 with 4.
    5. Replace MARRIAGE 0 with 3.
    6. Convert features to numeric.
    7. Standardize only the 14 numerical columns.
    8. Return features in the exact training order.
    """

    # --------------------------------------------------------
    # 1. Validate input
    # --------------------------------------------------------

    validate_input(data)

    # --------------------------------------------------------
    # 2. Create DataFrame
    # --------------------------------------------------------

    df = pd.DataFrame([data])

    # --------------------------------------------------------
    # 3. Keep exact model features
    # --------------------------------------------------------

    df = df[FEATURE_COLUMNS].copy()

    # --------------------------------------------------------
    # 4. Apply notebook preprocessing
    # --------------------------------------------------------

    # Notebook:
    # EDUCATION values 0, 5, 6 -> 4

    df["EDUCATION"] = df["EDUCATION"].replace(
        [0, 5, 6],
        4
    )

    # Notebook:
    # MARRIAGE value 0 -> 3

    df["MARRIAGE"] = df["MARRIAGE"].replace(
        0,
        3
    )

    # --------------------------------------------------------
    # 5. Convert all features to numeric
    # --------------------------------------------------------

    for column in FEATURE_COLUMNS:

        df[column] = pd.to_numeric(
            df[column],
            errors="raise"
        )

    # --------------------------------------------------------
    # 6. Scale numerical columns only
    # --------------------------------------------------------

    df[NUMERICAL_COLUMNS] = scaler.transform(
        df[NUMERICAL_COLUMNS]
    )

    # --------------------------------------------------------
    # 7. Final feature order
    # --------------------------------------------------------

    df = df[FEATURE_COLUMNS]

    return df
