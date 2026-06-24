def build_prompt(text):
    return f"""
You are an elite soccer analyst.

Analyze the text below step-by-step.

Description:
{text}

Instructions:

1. Identify the likely formation.
2. Identify tactical patterns.
3. Explain why these tactics were effective.
4. Identify weaknesses.
5. Suggest tactical improvements.
6. Provide a summary for casual fans.

Rules:
- Be evidence-based
- Only use information from the description
- If missing info, clearly state assumptions
- Keep response clear and structured
"""
