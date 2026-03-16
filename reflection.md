# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Bugs I noticed: 
1. The hints were not accurate at all. When I guessed 1, it prompted me to guess a number lower than that and when I guessed 100, it prompted me to guess a number higher than that. I expected the hints to be accurate.
2. The hints were not aligning with my guesses. I guessed 5 and it said to go higher, but the secret number was 3. I expected the hints to align with my responses properly. 
3. I was not able to start a new game, the "New Game" button did not work. I expected it to work as I wanted to play the game multiple times.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
For this project, I used ChatGPT to help me debug errors, give me suggestions on how to fix parts of my code to allow the game to run smoothly, and fix issues with pytest, and understand terminal commands.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One example of when AI gave me a correct suggestion was when it told me what was causing my tests to fail. The "check_guess" function returns two values, the outcome and a message, but the original tests were only checking one. So, in the tests_game_logic.py file, I updated it to correctly extract the result using  outcome, _ = check_guess(...) and then verified the guess. After making this change using AI's help, all three tests passed and the game ran smoothly.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One example of a misleading AI suggestion was when it told me to activate a virtual environment using 'source ~/.venv/bin/activate'. However, I did not have a virtual environment set up yet, so this caused me many issues in my terminal for a long time. I attempted to fix this issue by checking the project folder and running 'ls -a' to see the files. After realizing the virtual environment did not exist, I ran the game without it and it ran perfectly. This showed me that not all AI suggestions will work or always be correct. Sometimes, they need to be verified. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I knew a bug was fixed by checking the game in real time. I ran the game to see if the hints alligned with my guesses and if all the buttons worked. I inputted many numbers to see if the "Go Lower" and "Go Higher" hints were working after making changes to the code. I made sure the score was accurate, the game ended when the guess limit was at its end, and the "New Game" button worked so I could play again.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code. 
I ran pytest in tests/test_game_logic.py where I verified that check_guess worked correctly by producing the correct outcome between my guesses and the actual secret number. I changed up the test by extracting the outcome (previously explained) and then asserted the outcome. Running this test helped me know if all three of my tests passed. This told me that all the logic (for scoring and hints) and game itself run smoothly and accurately. 

- Did AI help you design or understand any tests? How?
AI truly helped me understand why some tests kept failing. It made me realize that check_guess was originally only checking one value when it was meant to return two (outcome and guess). AI's guidance helped me fix this which led my tests to pass and the game to run smoothly.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
