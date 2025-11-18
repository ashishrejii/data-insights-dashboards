import pandas as pd
import json
import os

def analyze_tickets(input_path, output_path):
    """
    Performs basic ticket analytics:
    - Daily ticket volume
    - Category distribution
    - Priority distribution
    - Average resolution time (SLA indicator)
    """

    df = pd.read_csv(input_path)

    # Convert timestamps
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["resolved_at"] = pd.to_datetime(df["resolved_at"])

    # Daily ticket volume
    daily_volume = df.groupby(df["created_at"].dt.date).size().to_dict()

    # Tickets by category
    category_volume = df["category"].value_counts().to_dict()

    # Tickets by priority
    priority_volume = df["priority"].value_counts().to_dict()

    # SLA: Resolution time in hours
    df["resolution_hours"] = (df["resolved_at"] - df["created_at"]).dt.total_seconds() / 3600
    avg_resolution_time = round(df["resolution_hours"].mean(), 2)

    results = {
        "daily_ticket_volume": daily_volume,
        "tickets_by_category": category_volume,
        "tickets_by_priority": priority_volume,
        "avg_resolution_time_hours": avg_resolution_time
    }

    # Ensure folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save results
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    return results


if __name__ == "__main__":
    input_file = "../datasets/ticket_data.csv"
    output_file = "../outputs/data/summary_stats.json"

    results = analyze_tickets(input_file, output_file)
    print("Ticket analysis completed:")
    print(json.dumps(results, indent=4))

