# -*- coding: utf-8 -*-
"""Phone Pattern + Google Tools Generator"""

import re
import urllib.parse
import streamlit as st

# ✅ Must be first Streamlit command
st.set_page_config(page_title="Web Search Pattern Generator", layout="centered")

st.title("🌐 Web Search + Google Tools Links")

with st.form("pattern_form"):
    business = st.text_input("Enter Name")
    phone = st.text_input("Enter Phone Number (e.g., +91 72870-62455)")
    submitted = st.form_submit_button("Generate")

if submitted:
    if not business or not phone:
        st.warning("⚠️ Please enter both Name and Phone Number.")
    else:
        patterns = clean_number_patterns(phone)
        out1, out2, out3, dashboards, supermario, biztools = format_outputs(business, patterns, phone)

        st.markdown("---")
        st.subheader("📌 Search Patterns")
        st.code(out1)
        st.code(out2)
        st.code(out3)

        st.markdown("---")
        st.subheader("📌 Google Tools Links")
        st.markdown(f"[Dashboards]({dashboards})")
        st.markdown(f"[SuperMario]({supermario})")
        st.markdown(f"[BizTools]({biztools})")
