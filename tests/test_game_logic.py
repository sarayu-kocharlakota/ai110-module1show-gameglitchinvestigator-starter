#FIX: Added pytest tests to verify Too Low, Too High, and Win outcomes with AI's support and guidance
from logic_utils import check_guess

def test_winning_guess():
    #FIX: Updated test to accurately read the outcome returned by check_guess
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
