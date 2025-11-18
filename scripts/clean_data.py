import pandas as pd
import os

def clean_csv(input_path, output_path):
    """
    Cleans a CSV file by:
    - Dropping null rows
    - Stripping whitespace
    - Standardizing text columns
    - Parsing date columns
    """

    df = pd.read_csv(input_path)

    # Drop rows that are fully empty
    df = df.dropna(how="all")

    # Strip whitespace from column names
    df.columns = [col.strip() for col in df.columns]

    # Strip whitespace inside string cells
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.strip()

    # Convert columns containing "date" or "at" into datetime
    date_cols = [col for col in df.columns if "date" in col.lower() or "at" in col.lower()]

    for col in date_cols:
        try:
            df[col] = pd.to_datetime(df[col], errors="coerce")
        except:
            pass

    # Normalize common text fields
    text_cols = ["category", "dept", "priority"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].str.lower()

    # Create output folder if not present
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False)

    return f"Cleaned file saved to: {output_path}"


if __name__ == "__main__":
    input_file = "../datasets/ticket_data.csv"
    output_file = "../outputs/data/cleaned_tickets.csv"

    print(clean_csv(input_file, output_file))
