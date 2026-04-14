🧠 Product Research Copilot

An AI-powered multi-agent product thinking tool that helps Product Managers and Business Analysts turn vague ideas into structured, decision-ready product insights.

Built using OpenAI API and Streamlit.

---

🚀 Overview

Product Research Copilot simulates a real-world product discovery workflow by breaking down a user’s idea into:

1. Problem Analysis  
2. Market & Research Insights  
3. Product Decision with Trade-offs  

It helps bridge the gap between raw ideas and structured product decisions used in real agile teams.

---

🎯 Key Features
 🔍 Problem Analysis
- Converts vague inputs into structured product problems
- Identifies target users, pain points, and assumptions
🌍 Market Research
- Summarizes possible solutions and competitor approaches
- Identifies gaps and opportunities
🧭 Product Decision Engine
- Generates multiple solution options
- Evaluates trade-offs (impact, effort, risk)
- Recommends the best approach
- Defines success metrics (KPIs)

---

🛠️ Tech Stack

- Python  
- Streamlit  
- OpenAI API  
- Python-dotenv  

---

🧠 Product Thinking Behind This Project

This project is designed to replicate how real Product Managers work:

- Start with problem clarity, not solutions  
- Analyze market context and user needs  
- Evaluate trade-offs before making decisions  
- Define success using measurable metrics  

It reflects real-world PM workflows used in Agile teams.

---

📦 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/product-research-copilot.git
cd product-research-copilot

****2. Create a virtual environment****
python -m venv venv

3. Activate the virtual environment

Mac / Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Set up environment variables

Create a .env file in the project root and add:

OPENAI_API_KEY=your_api_key_here

6. Run the application
streamlit run app.py

7. Open in browser
Open the local URL shown in the terminal (usually):

http://localhost:8501

Open the local URL shown in the terminal (usually):

http://localhost:8501
