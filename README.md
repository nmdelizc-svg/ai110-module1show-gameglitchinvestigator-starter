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

- [Purpose] Glitchy Guesser is a number guessing game built with Streamlit. The player picks a difficulty, which sets the number range and attempt limit. A secret number is generated each round and the player has to guess it within the allowed attempts, getting hints along the way telling them if they went too high or too low. The final score is based on how many attempts it took to win.
- [Bugs] Most of the bugs were logic issues hiding in plain sight. The hints were completely inverted, with "Too High" telling the player to go higher and "Too Low" telling them to go lower. The Normal and Hard difficulty ranges were also swapped. The secret number kept alternating between an int and a string on even attempts, which broke comparisons entirely. On top of that, the win score was being incremented twice due to a redundant +1, invalid guesses were consuming attempts before input was even validated, and starting a new game only reset some of the state, leaving score and history carrying over from the previous round.
- [Fixed] 
-Corrected the hint messages and swapped the difficulty ranges back to their proper values.
-Removed the int/str alternation so the secret is always stored as an int.
-Fixed the double increment in update_score and removed the broken Too High/Too Low score logic entirely, leaving score changes only on a win.
-Moved the attempt counter to after input validation so invalid guesses no longer waste a turn.
-Added a full state reset on New Game and moved the core functions from app.py into logic_utils.py.

## 📸 Demo

- [(image.png)] [Screenshot of fixed, winning game here]

## 🚀 Stretch Features

- [(image-1.png)] [Challenge 1: Advanced Edge-Case Testing]
