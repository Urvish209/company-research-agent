import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="AI Company Research Agent",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Powered Research & Recommendation Agent")

st.write(
    "Generate a structured intelligence report for any company."
)

company_name = st.text_input(
    "Enter Company Name",
    placeholder="Example: Adani Realty, Prestige Group, Sobha"
)

def generate_company_report(company):

    prompt = f"""
You are a senior business analyst and AI consultant.

Research the company: {company}

Create a detailed report with the following sections:

# Company Overview
- What the company does
- Industry
- Scale
- Geographic presence

# Key Business Information
- Major offerings
- Recent developments
- Expansion plans
- Important public information

# Potential Business Challenges
- Operational challenges
- Sales challenges
- Customer experience challenges

Explain reasoning behind each challenge.

# AI Opportunities
For each opportunity provide:
1. Problem
2. AI Solution
3. Expected Business Impact

Make recommendations specific to the company.

# Personalized CEO Pitch

Create a one-page personalized pitch including:
- Why we reached out
- Opportunities identified
- Recommended AI solutions
- Expected business value

Make the report professional and practical.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=4000
    )

    return response.choices[0].message.content


if st.button("Generate Report"):

    if not company_name.strip():
        st.warning("Please enter a company name.")
        st.stop()

    with st.spinner("Generating report..."):

        try:

            report = generate_company_report(company_name)

            st.success("Report Generated Successfully!")

            st.markdown(report)

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name=f"{company_name}_report.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")