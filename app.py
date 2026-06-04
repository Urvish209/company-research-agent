import streamlit as st
from groq import Groq

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Company Intelligence Platform",
    page_icon="🚀",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.stApp {
    background-color: #0F172A;
}

/* Hide Streamlit Menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Title */

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: white;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #CBD5E1;
    margin-bottom: 35px;
}

/* Input */

.stTextInput input {
    background-color: #1E293B !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid #334155 !important;
    height: 50px;
}

/* Button */

.stButton button {
    background-color: #2563EB;
    color: white;
    border-radius: 12px;
    border: none;
    height: 50px;
    font-size: 16px;
    font-weight: 600;
}

.stButton button:hover {
    background-color: #1D4ED8;
}

/* Metrics */

[data-testid="stMetric"] {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #334155;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

[data-testid="stMetricLabel"] {
    color: #CBD5E1 !important;
}

/* Expander */

.streamlit-expanderHeader {
    color: white !important;
}

div[data-testid="stExpander"] {
    background-color: #1E293B;
    border-radius: 12px;
    border: 1px solid #334155;
}

/* Generated Report Text */

.stMarkdown {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# GROQ CLIENT
# =====================================

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="main-title">
🚀 AI Company Intelligence Platform
</div>

<div class="sub-title">
Strategic Research • Business Intelligence • AI Transformation
</div>
""", unsafe_allow_html=True)

# =====================================
# METRICS
# =====================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Coverage", "360°")

# with col2:
#     st.metric("Analysis", "Strategic")

with col3:
    st.metric("Output", "CEO Ready")

st.write("")

# =====================================
# INPUT
# =====================================

company_name = st.text_input(
    "",
    placeholder="Enter Company Name (Adani Realty, Microsoft, Amazon, Prestige Group...)"
)

# =====================================
# REPORT GENERATOR
# =====================================

def generate_company_report(company):

    prompt = f"""
You are a Senior Strategy Consultant and AI Transformation Advisor.

Analyze the company: {company}

Generate a highly detailed intelligence report.

=========================================
1. EXECUTIVE SUMMARY
=========================================

Provide:
- Company snapshot
- Industry position
- Strategic observations
- Growth outlook

=========================================
2. COMPANY OVERVIEW
=========================================

Include:
- What the company does
- Industry
- Scale
- Geographic presence
- Market positioning
- Competitive advantages

=========================================
3. KEY BUSINESS INFORMATION
=========================================

Identify:

- Major offerings
- Revenue drivers
- Target customers
- Recent developments
- Expansion plans
- Strategic initiatives
- Important public information

Explain why each point matters.

=========================================
4. POTENTIAL BUSINESS CHALLENGES
=========================================

Analyze:

A. Operational Challenges

B. Sales Challenges

C. Customer Experience Challenges

D. Technology Challenges

For every challenge provide:

- Observation
- Reasoning
- Potential Business Impact

Avoid generic answers.

=========================================
5. AI OPPORTUNITIES
=========================================

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
3. Customer Support
4. Operations
5. Analytics
6. Document Processing
7. Decision Making

=========================================
6. IMPLEMENTATION ROADMAP
=========================================

Create:

Short-Term (0-3 Months)

Medium-Term (3-12 Months)

Long-Term (1-3 Years)

=========================================
7. CEO PERSONALIZED PITCH
=========================================

Imagine you are meeting the CEO.

Write a one-page executive pitch including:

- Why we reached out
- Key findings
- Business challenges
- AI opportunities
- Recommended roadmap
- Expected business outcomes

Make it persuasive and professional.

Use clear headings, bullet points, and consultant-style formatting.
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

# =====================================
# GENERATE BUTTON
# =====================================

if st.button(
    "🚀 Generate Intelligence Report",
    use_container_width=True
):

    if not company_name.strip():
        st.warning("Please enter a company name.")
        st.stop()

    with st.spinner("Researching company and generating intelligence report..."):

        try:

            report = generate_company_report(company_name)

            st.success("Report Generated Successfully")

            st.divider()

            with st.expander(
                "📄 Intelligence Report",
                expanded=True
            ):
                st.markdown(report)

            st.download_button(
                label="📥 Download Intelligence Report",
                data=report,
                file_name=f"{company_name}_AI_Intelligence_Report.txt",
                mime="text/plain",
                use_container_width=True
            )

        except Exception as e:
            st.error(str(e))