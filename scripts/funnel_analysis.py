import pandas as pd
import json
import os

def analyze_funnel(input_path, output_path):
    """
    Performs funnel conversion analysis:
    - Conversion rate per stage
    - Dropoff per stage
    - Overall funnel efficiency
    """

    df = pd.read_csv(input_path)

    stages = df["stage"].tolist()
    users = df["users"].tolist()
    conversions = df["conversions"].tolist()
    dropoffs = df["dropoff"].tolist()

    # Conversion rate per stage
    conversion_rates = {
        stage: round((conv / users[i]) * 100, 2)
        for i, (stage, conv) in enumerate(zip(stages, conversions))
    }

    # Dropoff percent per stage
    dropoff_rates = {
        stage: round((dropoffs[i] / users[i]) * 100, 2)
        for i, stage in enumerate(stages)
    }

    # Funnel completion rate: users who reached final stage / users at first stage
    overall_completion_rate = round((conversions[-1] / users[0]) * 100, 2)

    results = {
        "conversion_rates_percent": conversion_rates,
        "dropoff_rates_percent": dropoff_rates,
        "overall_completion_rate_percent": overall_completion_rate
    }

    # Create folder if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    return results


if __name__ == "__main__":
    input_file = "../datasets/funnel_data.csv"
    output_file = "../outputs/data/funnel_stats.json"

    results = analyze_funnel(input_file, output_file)
    print("Funnel analysis complete:")
    print(json.dumps(results, indent=4))

