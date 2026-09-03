from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model directory
MODEL_DIR = BASE_DIR / "models"

# Saved model files
MODEL_PATH = MODEL_DIR / "credit_default_model.pth"
SCALER_PATH = MODEL_DIR / "scaler.pkl"
CONFIG_PATH = MODEL_DIR / "model_config.pkl"

# ============================================================
# TARGET
# ============================================================

TARGET_COLUMN = "default payment next month"


# ============================================================
# FEATURES
# ============================================================

# These are the exact 23 features used by the ANN.
# ID is intentionally NOT included.

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

# These are the exact columns standardized in the notebook.

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
# RISK LEVELS
# ============================================================

# These are application-level labels.
# They are NOT additional model outputs.

LOW_RISK_THRESHOLD = 0.30
HIGH_RISK_THRESHOLD = 0.50
