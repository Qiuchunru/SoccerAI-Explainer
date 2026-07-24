def build_prompt(match_description):


    prompt = f"""

You are a professional soccer analyst.

Analyze the following match situation.

Explain:

1. Formation changes
2. Player roles
3. Tactical advantages
4. Possible weaknesses


Match:

{match_description}


Provide a clear explanation for soccer fans.

"""


    return prompt
