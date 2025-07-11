import streamlit as st

# Suspicious indicators
suspicious_keywords = [
    "free", "private", "sexy", "earn", "click", "win", "bitcoin",
    "login", "verify", "giveaway", "gift", "cash", "porn", "adult"
]
suspicious_tlds = [".xyz", ".click", ".top", ".club", ".run", ".tk", ".gq", ".ml"]
shorteners = [
    "bit.ly", "t.co", "tinyurl.com", "is.gd", "shorte.st", "klix.run", "rebrand.ly"
]

# Function to check if link is suspicious
def is_suspicious(url: str) -> list:
    reasons = []
    url = url.lower()
    if any(short in url for short in shorteners):
        reasons.append("Uses link shortener")
    if any(word in url for word in suspicious_keywords):
        reasons.append("Contains suspicious keyword")
    if any(url.endswith(tld) for tld in suspicious_tlds):
        reasons.append("Suspicious TLD (.xyz, .run, etc.)")
    return reasons

# ---------- Streamlit App ----------
st.set_page_config(page_title="Link Safety Checker", page_icon="🔗")
st.title("🔗 Link Safety Checker")
st.markdown("Paste one or more links below. It will tell you if they are **safe** or **dangerous**.")

# Text Input
input_links = st.text_area("Paste links here (one per line):", height=200)

# Check Button
if st.button("Check Links"):
    if not input_links.strip():
        st.warning("⚠️ Please enter at least one link.")
    else:
        links = input_links.strip().splitlines()

        for link in links:
            reasons = is_suspicious(link.strip())
            if reasons:
                st.error(f"❌ Dangerous: `{link}`")
            else:
                st.success(f"✅ Safe: `{link}`")
