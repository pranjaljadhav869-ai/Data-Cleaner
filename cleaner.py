import pandas as pd


def read_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)

    elif file.name.endswith(".xlsx") or file.name.endswith(".xls"):
        return pd.read_excel(file)

    else:
        return None


def remove_null(df):
    return df.dropna()


def remove_duplicate(df):
    return df.drop_duplicates()
def calculate_quality_score(df):
    """
    Calculate Data Quality Score from 0 to 100.
    """

    if df.empty:
        return 0

    # Total cells
    total_cells = df.shape[0] * df.shape[1]

    # Missing cells
    missing_cells = df.isnull().sum().sum()

    # Missing percentage
    missing_percentage = (
        missing_cells / total_cells
    ) * 100

    # Duplicate rows
    duplicate_rows = df.duplicated().sum()

    # Duplicate percentage
    duplicate_percentage = (
        duplicate_rows / len(df)
    ) * 100

    # Quality score
    score = 100 - missing_percentage - duplicate_percentage

    # Keep score between 0 and 100
    score = max(0, min(100, score))

    return round(score, 2)
