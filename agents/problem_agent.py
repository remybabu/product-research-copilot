from utils.openai_client import client

def analyze_problem(user_input):
    prompt = f"""
    You are a senior Product Manager.

    Convert this into a structured product problem:

    Input: {user_input}

    Output:
    - Problem Statement
    - Target Users
    - Key Pain Points
    - Assumptions
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content