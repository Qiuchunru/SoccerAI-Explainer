"""
AI Analysis Module

Handles soccer tactical explanation generation.

Currently uses prompt-based simulation.
Designed for IBM Granite integration.
"""


from prompts import build_prompt



def analyze_match(match_description):


    prompt = build_prompt(
        match_description
    )


    # Future:
    # Replace this section with IBM Granite API call


    response = f"""
⚽ Soccer Tactical Analysis


Match Situation:

{match_description}



AI Explanation:


1. Tactical Overview

The team appears to adjust its strategy
based on match conditions.



2. Formation Impact

The formation change affects:

- Defensive structure
- Midfield control
- Attacking opportunities



3. Player Roles

Players need to adapt their positioning
and responsibilities.



4. Strategic Insight

The tactical decision demonstrates how
coaches use formations and player movement
to gain advantages.


Generated using AI tactical reasoning.
"""


    return response
