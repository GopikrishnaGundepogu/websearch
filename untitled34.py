import re
import urllib.parse
import streamlit as st

st.set_page_config(page_title="Web Search Pattern Generator", layout="centered")

def generate_google_links(phone):
    """Generate dashboards, supermario, and biztools links for a phone number."""
    digits_only = re.sub(r"[^\d]", "", phone) # only digits
    plus_digits = re.sub(r"[^\d+]", "", phone) # keep + for biztools

    encoded_full = urllib.parse.quote(phone.strip()) # keep original with spaces/dashes
    encoded_plus_digits = urllib.parse.quote(plus_digits) # for biztools

    dashboards = f"https://dashboards.corp.google.com/_ae0481b4_d760_44ff_962e_57ddb7a1dd30?p=ATTRIBUTE:P:{digits_only}"
    supermario = f"https://supermario.corp.google.com/adv?phone={encoded_full}"
    biztools = f"https://biztools.corp.google.com/local/business/admin/p%3A{encoded_plus_digits}"

    return dashboards, supermario, biztools


st.title("🌐 Web Search + Google Tools Links")

with st.form("pattern_form"):
    phone = st.text_input("Enter Phone Number (e.g., +91 72870-62455)")
    submitted = st.form_submit_button("Generate")

if submitted:
    if not phone:
        st.warning("⚠️ Please enter a Phone Number.")
    else:
        dashboards, supermario, biztools = generate_google_links(phone)

        # Show individual links
        st.markdown("### Individual Links")
        st.markdown(f"[Dashboards]({dashboards})")
        st.markdown(f"[SuperMario]({supermario})")
        st.markdown(f"[BizTools]({biztools})")

        # Create one combined launcher (HTML + JS)
        multi_link_html = f"""
        <script>
        function openAll() {{
            window.open("{dashboards}", "_blank");
            window.open("{supermario}", "_blank");
            window.open("{biztools}", "_blank");
        }}
        </script>
        <button onclick="openAll()">🚀 Open All Google Tools</button>
        """
        st.markdown(multi_link_html, unsafe_allow_html=True)
