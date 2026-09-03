from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Directory containing trained model artifacts
MODEL_DIR = BASE_DIR / "models"

# Trained Keras ANN
MODEL_PATH = MODEL_DIR / "credit_default_model.keras"

# Saved StandardScaler
SCALER_PATH = MODEL_DIR / "scaler.pkl"

# Saved feature information from the notebook
FEATURE_COLUMNS_PATH = MODEL_DIR / "feature_columns.pkl"

# Saved preprocessing configuration from the notebook
PREPROCESSING_CONFIG_PATH = MODEL_DIR / "preprocessing_config.pkl"


# ============================================================
# TARGET
# ============================================================

TARGET_COLUMN = "default payment next month"


# ============================================================
# FEATURES
# ============================================================

# The notebook drops ID before training.
# Therefore the ANN receives exactly these 23 features.

FEATURE_COLUMNS = [
    "LIMIT_BAL",
    "SEX",
    "EDUCATION",
    "MARRIAGE",
    "AGE",
    "PAY_0",
    "PAY_2",
    "PAY_3",
    "PAY_4",
    "PAY_5",
    "PAY_6",
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


# ============================================================
# NUMERICAL FEATURES
# ============================================================

# These are the columns that the notebook scales
# using StandardScaler.

NUMERICAL_COLUMNS = [
    "LIMIT_BAL",
    "AGE",
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


# ============================================================
# CATEGORICAL / DISCRETE FEATURES
# ============================================================

# These columns are NOT standardized in the notebook.

CATEGORICAL_COLUMNS = [
    "SEX",
    "EDUCATION",
    "MARRIAGE",
    "PAY_0",
    "PAY_2",
    "PAY_3",
    "PAY_4",
    "PAY_5",
    "PAY_6",
]


# ============================================================
# MODEL SETTINGS
# ============================================================

# The notebook converts probability to class using 0.5.

DEFAULT_THRESHOLD = 0.50


# ============================================================
# OPTIONAL APPLICATION RISK LEVELS
# ============================================================

# These are application-level labels.
# They are NOT part of the trained ANN.

LOW_RISK_THRESHOLD = 0.30
HIGH_RISK_THRESHOLD = 0.50
