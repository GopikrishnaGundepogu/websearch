# -*- coding: utf-8 -*-
"""Phone Pattern + Google Tools Generator"""

import re
import urllib.parse
import streamlit as st

# ✅ Must be first Streamlit command
st.set_page_config(page_title="Web Search Pattern Generator", layout="centered")

def generate_google_links(phone):
    """Generate dashboards, supermario, and biztools links for a phone number."""
    # Digits only (no +, no spaces, no dashes)
    digits_only = re.sub(r"[^\d]", "", phone)

    # Keep +, remove spaces/dashes for BizTools
    plus_digits = re.sub(r"[^\d+]", "", phone)

    # URL encode versions
    encoded_full = urllib.parse.quote(phone.strip()) # keep original with spaces/dashes
    encoded_plus_digits = urllib.parse.quote(plus_digits)

    dashboards = f"https://dashboards.corp.google.com/_ae0481b4_d760_44ff_962e_57ddb7a1dd30?p=ATTRIBUTE:P:{digits_only}"
    supermario = f"https://supermario.corp.google.com/adv?phone={encoded_full}"
    biztools = f"https://biztools.corp.google.com/local/business/admin/p%3A{encoded_plus_digits}"

    return dashboards, supermario, biztools


def format_outputs(business, patterns, phone):
    # Output 1
    out1 = f'{business} "{patterns[0]}"'

    # Output 2: original, pattern2, pattern5
    out2 = f'{business} "{patterns[0]}" OR "{patterns[1]}" OR "{patterns[4]}"'

    # Output 3: all 6
    all_patterns = ' OR '.join(f'"{p}"' for p in patterns)
    out3 = f"{business} {all_patterns}"

    # Google tool links
    dashboards, supermario, biztools = generate_google_links(phone)

    return out1, out2, out3, dashboards, supermario, biztools


# Streamlit UI
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
