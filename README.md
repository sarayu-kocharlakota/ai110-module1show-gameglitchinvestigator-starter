# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience
This game is a Streamlit-based number game that challenges players to test their debugging and problem-solving skills by observing and solving game logic mistakes.

The two main bugs I found were that the higher/lower hints were inaccurate when compared with my number guesses and tests failed as the check_guess function returns two values (outcome and message) but the tests only verified one. 

To make things easier and cleaner, I moved all game logic into logic_utils.py. I fully modified the tests in tests/test_game_logic.py to handle both values returned by check_guess and I made sure to run 'pytest' to verfiy if all three of my tests passed. 

## 📸 Demo
![Game Demo](pytest.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
