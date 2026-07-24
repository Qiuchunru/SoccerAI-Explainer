
"""
AI Tactical Analysis Module

This module handles AI-based soccer tactical explanations.

Currently uses a prompt-based simulation.
Can be replaced with IBM Granite API integration.
"""


def analyze_match(match_description):
    """
    Analyze soccer match description and generate tactical explanation.

    Args:
        match_description (str):
            User provided match scenario

    Returns:
        str:
            AI generated tactical analysis
    """


    analysis = f"""
Soccer Tactical Analysis

Match Situation:
{match_description}


Tactical Explanation:

The described situation shows a tactical adjustment
designed to improve team performance.


Key Points:

1. Formation Analysis:
The team changed its structure to create better
balance between defense and attack.


2. Player Roles:
Players need to adapt their positioning,
movement, and responsibilities.


3. Strategic Impact:
The tactical change may create more attacking
opportunities while maintaining defensive stability.


AI Insight:

This tactical decision demonstrates how managers
adapt their strategy based on match conditions.
"""


    return analysis
