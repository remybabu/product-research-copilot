import streamlit as st
from agents.problem_agent import analyze_problem
from agents.research_agent import research_market
from agents.decision_agent import make_decision

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Product Research Copilot", layout="centered")

# ----------------------------
# HEADER
# ----------------------------
st.title("🧠 Product Research Copilot")
st.markdown("### AI-powered assistant for Product Managers & Business Analysts")
st.markdown("---")

# ----------------------------
# INPUT
# ----------------------------
user_input = st.text_area("Enter your product question:")

# ----------------------------
# ACTION
# ----------------------------
if st.button("Run Analysis"):

    if user_input:

        # ----------------------------
        # PROBLEM ANALYSIS
        # ----------------------------
        with st.spinner("🔍 Analyzing problem..."):
            problem = analyze_problem(user_input)

        st.markdown("## 🔍 Problem Analysis")
        st.markdown(problem)
        st.markdown("---")

        # ----------------------------
        # RESEARCH INSIGHTS
        # ----------------------------
        with st.spinner("🌍 Researching market..."):
            research = research_market(problem)

        st.markdown("## 🌍 Research Insights")
        st.markdown(research)
        st.markdown("---")

        # ----------------------------
        # DECISION OUTPUT
        # ----------------------------
        with st.spinner("🧭 Generating recommendation..."):
            decision = make_decision(problem, research)

        st.markdown("## 🧭 Decision Recommendation")
        st.markdown(decision)
        st.markdown("---")

        # ----------------------------
        # PRODUCT BRIEF DOWNLOAD
        # ----------------------------
        product_brief = f"""
# Product Brief

## Problem
{problem}

## Research Insights
{research}

## Recommendation
{decision}
"""

        st.download_button(
            label="📄 Download Product Brief",
            data=product_brief,
            file_name="product_brief.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please enter a product question before running analysis.")