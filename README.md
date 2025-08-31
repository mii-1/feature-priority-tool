# 📈 Data-Driven Feature Prioritization (RICE)

A lightweight tool to demonstrate data-driven product decisions. Upload/modify feature metrics and compute RICE scores to form a roadmap.

## Metrics
- Reach (users/month)
- Impact (1=Low, 2=Medium, 3=High, 5=Massive)
- Confidence (0-100%)
- Effort (person-months)

RICE = (Reach * Impact * Confidence) / Effort

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
