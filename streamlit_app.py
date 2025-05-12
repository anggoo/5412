import streamlit as st
import json
from collections import defaultdict

st.title("🧮 Multi-JSON Label Point Counter")
st.markdown("Drag and drop multiple `.json` files below. The app will count how many points each label has across all files.")

uploaded_files = st.file_uploader("Upload JSON files", type="json", accept_multiple_files=True)

if uploaded_files:
    label_counts = defaultdict(int)

    for uploaded_file in uploaded_files:
        try:
            data = json.load(uploaded_file)
            for shape in data.get("shapes", []):
                label = shape.get("label")
                points = shape.get("points", [])
                label_counts[label] += len(points)
        except Exception as e:
            st.error(f"Error in file {uploaded_file.name}: {e}")

    if label_counts:
        st.subheader("📊 Points per Label")
        for label, count in label_counts.items():
            st.write(f"**{label}**: {count} points")
    else:
        st.warning("No valid labels or points found in uploaded files.")
