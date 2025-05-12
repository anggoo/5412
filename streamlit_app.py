import streamlit as st
import json
from collections import defaultdict

st.title("🔢 Label Counter from JSON")
st.markdown("Upload multiple `.json` files. This app counts how many times each `label` appears.")

uploaded_files = st.file_uploader("Upload JSON files", type="json", accept_multiple_files=True)

if uploaded_files:
    label_counts = defaultdict(int)

    for uploaded_file in uploaded_files:
        try:
            data = json.load(uploaded_file)
            for shape in data.get("shapes", []):
                label = shape.get("label")
                if label:
                    label_counts[label] += 1
        except Exception as e:
            st.error(f"❌ Error in file {uploaded_file.name}: {e}")

    if label_counts:
        st.subheader("📊 Label Frequency")
        for label, count in label_counts.items():
            st.write(f"**{label}**: {count} time(s)")
    else:
        st.warning("No valid labels found in uploaded files.")
