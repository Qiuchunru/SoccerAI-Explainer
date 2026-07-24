from backend.ai import analyze_match


def test_analyze_match():

    match_description = (
        "The team changed from "
        "4-3-3 to 3-5-2 formation."
    )


    result = analyze_match(
        match_description
    )


    assert result is not None

    assert "Tactical" in result
