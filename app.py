import streamlit as st
from groq import Groq

# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(
    page_title="AI Company Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# Custom CSS
# ---------------------------

st.markdown("""
<style>

.stApp {
    background-color: #F8FAFC;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #111827;
}

.sub-title {
    font-size: 18px;
    color: #6B7280;
    margin-bottom: 20px;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Groq Client
# ---------------------------

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# ---------------------------
# Sidebar
# ---------------------------

with st.sidebar:

    st.title("📊 AI Research Agent")

    st.markdown("""
This platform generates:

✅ Company Overview

✅ Business Intelligence

✅ Business Challenges

✅ AI Opportunities

✅ CEO Pitch

---

Powered by:

- Streamlit
- Groq
- Llama 3.3 70B
""")

# ---------------------------
# Header
# ---------------------------

st.markdown("""
<div class="main-title">
AI Company Intelligence Platform
</div>

<div class="sub-title">
Research • Business Analysis • AI Strategy • Executive Recommendations
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Input Section
# ---------------------------

company_name = st.text_input(
    "Enter Company Name",
    placeholder="Adani Realty, Prestige Group, Microsoft, Amazon..."
)

# ---------------------------
# Report Function
# ---------------------------

def generate_company_report(company):

    prompt = f"""
You are a Senior Strategy Consultant and AI Transformation Advisor.

Analyze the company: {company}

Generate a detailed executive-level intelligence report.

=================================================

1. EXECUTIVE SUMMARY

Provide:

- Company snapshot
- Industry position
- Strategic observations
- Growth outlook

=================================================

2. COMPANY OVERVIEW

Include:

- What the company does
- Industry
- Company scale
- Geographic presence
- Market positioning
- Competitive advantages

=================================================

3. KEY BUSINESS INFORMATION

Identify:

- Major offerings
- Revenue drivers
- Target customers
- Recent developments
- Expansion plans
- Strategic initiatives
- Important public information

Explain why each point is important.

=================================================

4. POTENTIAL BUSINESS CHALLENGES

Analyze:

A. Operational Challenges

B. Sales Challenges

C. Customer Experience Challenges

D. Technology Challenges

For each challenge provide:

- Observation
- Reasoning
- Business Impact

Avoid generic answers.

=================================================

5. AI OPPORTUNITIES

Provide company-specific recommendations.

For each opportunity include:

- Business Problem
- AI Solution
- Implementation Approach
- Expected ROI
- Business Impact

Cover:

1. Sales
2. Marketing
3. Customer Service
4. Operations
5. Analytics
6. Document Processing
7. Decision Making

=================================================

6. IMPLEMENTATION ROADMAP

Create:

Short Term (0-3 Months)

Medium Term (3-12 Months)

Long Term (1-3 Years)

=================================================

7. CEO PERSONALIZED PITCH

Imagine you are meeting the CEO.

Write a professional one-page pitch explaining:

- Why you reached out
- Key observations
- Business challenges discovered
- AI opportunities identified
- Recommended solutions
- Expected business outcomes

The pitch should sound like a consulting firm presentation.

=================================================

Use professional formatting with headings and bullet points.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=4000
    )

    return response.choices[0].message.content

# ---------------------------
# Generate Button
# ---------------------------

if st.button("🚀 Generate Intelligence Report", use_container_width=True):

    if not company_name.strip():
        st.warning("Please enter a company name.")
        st.stop()

    with st.spinner("Researching company and generating report..."):

        try:

            report = generate_company_report(company_name)

            st.success("Report Generated Successfully")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Analysis Type", "Strategic")

            with col2:
                st.metric("Coverage", "360°")

            with col3:
                st.metric("Focus", "AI Transformation")

            st.divider()

            with st.expander(
                "📄 View Intelligence Report",
                expanded=True
            ):
                st.markdown(report)

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name=f"{company_name}_report.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")