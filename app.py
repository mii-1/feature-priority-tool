import streamlit as st
import pandas as pd

st.title("📈 Data-Driven Feature Prioritization (RICE)")

st.write("Upload a CSV or edit the sample below. Columns: feature, reach, impact, confidence, effort")

try:
    df = pd.read_csv("data/feature_usage.csv")
except Exception:
    df = pd.DataFrame(columns=["feature","reach","impact","confidence","effort"])

uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)

edited = st.data_editor(df, num_rows="dynamic", use_container_width=True)

def compute_rice(df):
    d = edited.copy()
    for col in ["reach","impact","confidence","effort"]:
        d[col] = pd.to_numeric(d[col], errors="coerce").fillna(0.0)
    d["RICE"] = (d["reach"] * d["impact"] * (d["confidence"]/100.0)) / d["effort"].replace(0, 0.1)
    return d.sort_values("RICE", ascending=False)

if st.button("Compute RICE"):
    ranked = compute_rice(edited)
    st.subheader("Ranked Features")
    st.dataframe(ranked, use_container_width=True)
    st.subheader("RICE by Feature")
    st.bar_chart(ranked.set_index("feature")["RICE"])

