Data Insights Dashboards

A lightweight analytics and insights toolkit built for Product Managers, CSMs, and Product Analysts.
This repository demonstrates how to convert raw operational data into dashboards, insights, and clean visual outputs — using simple, production-friendly Python scripts.

📊 What This Repo Demonstrates

1. Clean and prepare raw datasets
2. Analyze ticket volume, funnel performance, and spend patterns
3. Build lightweight segmentation logic
4. Generate charts that resemble PM dashboards
5. Think in systems and extract meaningful insights
6. Work with CSVs, Python, and basic analytics tooling

```
📁 Repository Structure
data-insights-dashboards/
│
├── datasets/
│   ├── ticket_data.csv
│   ├── funnel_data.csv
│   ├── spend_data.csv
│   └── README.md
│
├── scripts/
│   ├── clean_data.py
│   ├── ticket_volume_analysis.py
│   ├── funnel_analysis.py
│   ├── segmentation_engine.py
│   └── generate_charts.py
│
├── outputs/
│   ├── charts/
│   └── data/
│
└── README.md
```
📂 Datasets Included
1. ticket_data.csv
Simulated customer support tickets with timestamps, priority, category, agent, and CSAT.
Useful for ticket volume, SLA, and agent performance analysis.

2. funnel_data.csv
A sample product funnel covering Landing → Signup → Onboarding → Activation → Paid.
Great for conversion and drop-off analysis.

3. spend_data.csv
Synthetic travel and operational spend data across Sales, Marketing, Engineering, and Finance.
Ideal for segmentation and spend insights.

⚙ Scripts
1. clean_data.py
Standardizes, cleans, and preprocesses datasets.

2. ticket_volume_analysis.py
Analyzes ticket count, category distribution, priority mix, and SLA patterns.

3. funnel_analysis.py
Computes conversion rates and drop-offs across funnel stages.

4. segmentation_engine.py
Performs basic segmentation (e.g., by spend levels, priority, behavior).

5. generate_charts.py
Produces PM-friendly visualizations (line charts, bar charts, funnel charts).

📈 Outputs

✔ Cleaned CSV files
✔ Summary statistics
✔ PNG charts for dashboards

Located inside:
```
outputs/data/
outputs/charts/
```
