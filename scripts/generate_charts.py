import pandas as pd
import matplotlib.pyplot as plt
import os
import json

def generate_ticket_volume_chart(ticket_path, output_path):
    df = pd.read_csv(ticket_path)

    category_counts = df["category"].value_counts()

    plt.figure(figsize=(8, 5))
    category_counts.plot(kind="bar")
    plt.title("Ticket Volume by Category")
    plt.xlabel("Category")
    plt.ylabel("Ticket Count")

    os.makedirs(output_path, exist_ok=True)
    plt.savefig(os.path.join(output_path, "ticket_volume.png"))
    plt.close()


def generate_funnel_chart(funnel_path, output_path):
    df = pd.read_csv(funnel_path)

    plt.figure(figsize=(8, 5))
    plt.bar(df["stage"], df["conversions"])
    plt.title("Funnel Conversion by Stage")
    plt.xlabel("Stage")
    plt.ylabel("Conversions")

    os.makedirs(output_path, exist_ok=True)
    plt.savefig(os.path.join(output_path, "funnel_conversion.png"))
    plt.close()


def generate_csat_chart(ticket_path, output_path):
    df = pd.read_csv(ticket_path)

    def csat_band(score):
        if score >= 4:
            return "High Satisfaction"
        elif score == 3:
            return "Neutral"
        else:
            return "Low Satisfaction"

    df["csat_band"] = df["csat_score"].apply(csat_band)
    csat_counts = df["csat_band"].value_counts()

    plt.figure(figsize=(7, 7))
    csat_counts.plot(kind="pie", autopct="%1.1f%%")
    plt.title("CSAT Distribution")

    os.makedirs(output_path, exist_ok=True)
    plt.savefig(os.path.join(output_path, "csat_segments.png"))
    plt.close()


if __name__ == "__main__":
    ticket_file = "../datasets/ticket_data.csv"
    funnel_file = "../datasets/funnel_data.csv"
    charts_folder = "../outputs/charts/"

    generate_ticket_volume_chart(ticket_file, charts_folder)
    generate_funnel_chart(funnel_file, charts_folder)
    generate_csat_chart(ticket_file, charts_folder)

    print("Charts generated successfully!")
