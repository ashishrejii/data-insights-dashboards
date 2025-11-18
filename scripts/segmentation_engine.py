import pandas as pd
import os

def segment_tickets(input_path, output_path):
    """
    Segments tickets into:
    - Priority groups
    - Category groups
    - CSAT performance bands
    - Agent workload buckets
    """

    df = pd.read_csv(input_path)

    # Priority segments
    priority_counts = df["priority"].value_counts().reset_index()
    priority_counts.columns = ["priority", "ticket_count"]

    # Category segments
    category_counts = df["category"].value_counts().reset_index()
    category_counts.columns = ["category", "ticket_count"]

    # CSAT segmentation
    def csat_band(score):
        if score >= 4:
            return "High Satisfaction"
        elif score == 3:
            return "Neutral"
        else:
            return "Low Satisfaction"

    df["csat_band"] = df["csat_score"].apply(csat_band)
    csat_segments = df["csat_band"].value_counts().reset_index()
    csat_segments.columns = ["csat_band", "ticket_count"]

    # Agent workload segmentation
    agent_workload = df["agent"].value_counts().reset_index()
    agent_workload.columns = ["agent", "tickets_handled"]

    # Combine into a single table for output
    combined_segments = pd.concat(
        [
            priority_counts.assign(segment_type="priority"),
            category_counts.assign(segment_type="category"),
            csat_segments.assign(segment_type="csat_band"),
            agent_workload.assign(segment_type="agent_workload")
        ],
        axis=0,
        ignore_index=True
    )

    # Ensure folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    combined_segments.to_csv(output_path, index=False)

    return combined_segments


if __name__ == "__main__":
    input_file = "../datasets/ticket_data.csv"
    output_file = "../outputs/data/segments.csv"

    segments = segment_tickets(input_file, output_file)
    print("Segmentation completed:")
    print(segments)

