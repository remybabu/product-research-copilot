from utils.openai_client import client

def research_market(problem_output):
    prompt = f"""
    You are a product researcher.

    Based on this:

    {problem_output}

    Provide:
    - Existing solutions
    - Competitor approaches
    - Market gaps
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content