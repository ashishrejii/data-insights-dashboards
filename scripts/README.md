# Scripts

This folder contains lightweight Python scripts used for cleaning datasets, analyzing operational patterns, and generating PM-friendly dashboards.

These scripts demonstrate practical data fluency—ideal for Product Managers, CSMs, Product Analysts, and Technical PM roles.

---

## 1. clean_data.py
Cleans raw CSV files by:
- removing empty rows  
- parsing date fields  
- standardizing text columns  
- normalizing category/priority labels  

**Output:** cleaned CSV in `outputs/data/`.

---

## 2. ticket_volume_analysis.py
Analyzes support ticket patterns:
- daily ticket volume  
- category distribution  
- priority mix  
- average resolution time (SLA indicator)  

**Output:** `summary_stats.json`.

---

## 3. funnel_analysis.py
Performs product funnel analysis:
- stage-wise conversion  
- dropoff rates  
- overall funnel completion  

**Output:** `funnel_stats.json`.

---

## 4. segmentation_engine.py
Segments ticket data into:
- priority groups  
- category groups  
- CSAT satisfaction bands  
- agent workload buckets  

**Output:** `segments.csv`.

---

## 5. generate_charts.py
Creates PM-friendly visualizations:
- ticket volume chart  
- funnel conversion chart  
- CSAT distribution chart  

**Output:** PNG images in `outputs/charts/`.

---

## Running Scripts
Each script is designed to be run individually:
```
python <script_name>.py
```

Ensure datasets exist in `datasets/` before running.

---

## Skills Demonstrated
- Data cleaning  
- Analytical thinking  
- Visualization  
- Segmentation  
- Interpretation of operational metrics  
- PM-level insight generation  

