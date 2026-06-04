# AI-Powered Research & Recommendation Agent

## Overview

This application generates a structured intelligence report for any company.

### Features

- Company Overview
- Business Information
- Business Challenges
- AI Opportunities
- CEO Pitch

## Tech Stack

- Python
- Streamlit
- OpenAI API
- OpenAI Web Search

## Installation

Install packages:

```bash
pip install -r requirements.txt
```

Add API key in:

```env
OPENAI_API_KEY=your_key_here
```

Run:

```bash
streamlit run app.py
```

## Architecture

User Input
↓
Streamlit
↓
OpenAI API
↓
Web Search
↓
Analysis
↓
Report