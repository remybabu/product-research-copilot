from utils.openai_client import client

def make_decision(problem, research):

    prompt = f"""
You are a Senior Product Manager responsible for making product decisions.

You are given:

PROBLEM:
{problem}

RESEARCH INSIGHTS:
{research}

Your task is to produce a structured product decision.

Follow this format strictly:

---

## 1. Possible Solutions (2–3 options)
For each solution, describe clearly:
- What it is
- How it solves the problem

---

## 2. Trade-offs Analysis
For each option evaluate:
- Impact (High / Medium / Low)
- Effort (High / Medium / Low)
- Risk (High / Medium / Low)

---

## 3. Recommended Solution
Choose ONE option and explain:
- Why this is the best choice
- Expected user impact
- Expected business impact

---

## 4. Risks & Assumptions
List:
- Key risks
- Hidden assumptions
- What could go wrong after launch

---

## 5. Success Metrics (VERY IMPORTANT)
Define:
- 2–3 key KPIs to measure success
- How you will know if this decision worked

---

Make your answer clear, structured, and concise.
Avoid generic statements.
Think like a real product leader at a tech company.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content