Reflection and Time Taken
Time Taken: 02:45:32
Reflection:
        Overall, I think I underestimated myself when it came down to this challenge. It was actually a lot of fun to design with a time limit. I didn’t know that I was able to speed code so quickly. I was constantly checking to see how much time I had left and wasn’t originally planning on doing the hangman graphic. However, everything went smooth as silk! I had a lot of fun doing this. I want to try doing more challenges in the future!!!
        I also realized a couple of interesting things about my code. When I’m not on my ADHD meds, I tend to be able to think of possible problems before they happen much better then when I am on them. I used the first 30 minutes to plan out my problem (as seen below), and while I did use it a bit, I kinda just went with my gut. I also found that I had enough time to write docstrings to explain my code and what it does, which I always like to do so I can look back and reuse it for other projects!
        Regardless of whether or not I get this job, I thank you for this opportunity to test myself and motivate me to start coding more of my own projects! This has been a great experience and has given me confidence that if it comes down to a time crunch, I can code under pressure. 
Planning:
1. Greet the user welcoming them to the game
* “Welcome to hangman!!”
2. The program randomly selects a word from a list of 10 words with different lengths, you as the developer choose the words.
* We’ll need to import random here
* Make a list of possible words
3. The program indicates to the user how many letters are in the word
* Do this with underscores
* EX: ____
* Separated List
4. The user is asked to guess a letter
* Prompt: “Guess a letter!”
a. If the letter is in the word, the letter is displayed in the correct position of the word with all previously guessed correct letters
* Replace underscore
   * EX: s_a__ 
* Record progress somewhere


b. If the letter is not in the word, display the letter indicating it is not in the word with all previously guessed letters that are not in the word
* Have a separate list recording guessed letters
* Guessed: [x, y, z,]
5. The program displays how many guesses have been made, with how many correct and incorrect guesses.
* Total Guesses:
Incorrect Guesses:
6. The program continues to ask the user for guesses until all the letters in the word are guessed correctly.
   * While True:
7. When all letters of the word are guessed correctly,
a. the program tells the user they have correctly guessed the word
   * Congrats! {correct_word} is the word!
b. and indicates the number of guesses it took
   * It took you {Guesses} Guesses!
8. The program then asks the user if they would like to try again or quit
   * Would you like to try again? (y/n)
a. If the user indicates they want to continue, the program chooses a different word randomly and the play continues
   * Have a used_words list.
b. If the user indicates they want to quit, the program thanks them for playing and quits.
   * Thanks for playing!!
9. You can choose to use a terminal interface or a web interface
   * This is gonna have to be a terminal because I AM NOT SMART ENOUGH FOR WEB YET. 
10. Gallows
   * Design in PyCharm inside docstrings