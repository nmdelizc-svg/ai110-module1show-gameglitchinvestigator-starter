# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  At first sight it appears to be a very basic number guessing game. After a few attempts at playing I quickly encountered a few issues. Some seem harmless and could be fixed by changing one or two lines but others make the game impossible to play. 

- List at least two concrete bugs you noticed at the start  
  From the start, I noticed the feedback after a wrong attempt appeared to be backwards. As I continued making guesses the number to be guessed would randomly change. After, when i explored the different difficulties, I noticed that the ranges for Normal and Hard were inverted. I also noticed that Normal mode allowed more guess attempts than the Easy one. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  For this project i used Claude Code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  A clear example was the New Game button in app.py. Originally it only regenerated the secret number but left attempts, score, status and history untouched, so starting a new game would carry over your old data. Claude pointed out that all of those needed to reset together, and suggested resetting attempts to 0, score to 0, status back to "playing", and clearing history, all in the same if new_game block. I verified it by playing a full game to a win or loss, hitting New Game, and confirming everything wiped cleanly before the next round started.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  In parse_guess, Claude kept suggesting to leave raw as a string and work around it, since some of the existing checks like the empty string comparison and the decimal point detection already treated it as one. But at the same time, when I asked if there were any bugs, it would point out that raw was being compared as a string instead of an integer, which contradicted its own suggestion. I ended up making the call to convert raw to an integer early using int() or int(float()) for decimals, since the whole point of the function is to produce a valid integer guess. The decimal check was the one place where I understood why Claude hesitated, since you do need the string form to detect the dot before converting, but everything after that should be working with the integer.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  A bug was truly fixed only when it passed both manual testing during development and a corresponding pytest. My process was to test by hand as I worked, then use Claude to generate formal tests to confirm I hadn't missed any edge cases.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  One of the tests i ran manually that took the longest was the parse_guess method. For me it was the most dificult since the logic at the begining was all over the place mixing strings and integers. On the pytest side before the range validation fix, parse_guess would return ok=True for a number like 999 on Easy mode, which meant the attempt counter incremented and the guess appeared in history even though the input was technically invalid. The pytest test made this visible immediately: it asserted ok=False for an out-of-range input and failed until the low/high bounds check was added to parse_guess.

- Did AI help you design or understand any tests? How?
  I used AI to design most of the tests. Since I did as much manual testing as i could i was confident on letting AI create the final test incase i missed anything. For this, i explained to Claude how i ran the tests by hand and asked to find any other methods of verification that i might have missed and make a test for it. Claude's generated tests were generally straightforward, which actually gave me confidence that my manual testing had covered the main cases, it wasn't finding major gaps I'd overlooked."
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Basically, when anything is clicked, moved, dragged, or interacted with in the slightest, the whole thing is redone from scratch, every individual button, every label, even the background color. Everything.
What makes it work is how insanely fast this happens. Even in bigger applications, you barely notice it's starting over at all.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    One habit I want to carry into future projects is making more frequent Git commits. At first I was a little intimidated since I'm not very familiar with Git, but I found commits to be incredibly useful, not just for tracking progress, but mostly as a form of documentation. I'll also keep using long, specific prompts when working with AI, since that's how I get the best results. It also helps me understand what I'm doing better, since I'm constantly revisiting details as I write them out.

- What is one thing you would do differently next time you work with AI on a coding task?
  I would be more careful about how much I trust what AI says without questioning it. I found myself following its suggestions too quickly instead of using it as a debugging tool and working things through myself first. Next time I want to ask more direct, targeted questions and treat AI as a resource, not just an answer machine. I would also like to get better at commenting my code. I often find myself solving problems and coming up with solutions entirely in my head without writing any of it down, when I could just document it directly in the code. That would make it much easier to stay on top of what I was doing, even after stepping away from the project for a while.
  
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project made me realize, more than ever, that AI is a tool designed to help you learn, not just to hand you answers. I usually find myself asking for straight solutions, which in my opinion is not the right way to use it. This time I decided to slow down and ask as many questions as I could to actually understand the logic behind the code, not just the idea but the whole process of turning an algorithm into something that works. Understanding the why behind each decision made me a much more confident programmer, and that is something I will carry into every project going forward.