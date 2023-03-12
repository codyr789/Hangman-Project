import random


# RUN IN TERMINAL!


def gallows(guess_number):
    '''
    prints word picture of gallows based on number of guesses
    :param guess_number: number of incorrect guesses
    :return: prints gallows picture based on number of wrong guesses
    '''
    gallow_pics = [
    '''
    +===+
        |
        |
        |
        |
    ________''',
    '''
    +===+
    O   |
        |
        |
        |
    ________''',
   '''
   +===+
   O   |
   |   |
       |
       |
   ________''',
    '''
    +===+
    O   |
    |   |
    |   |
        |
    ________''',
    '''
    +===+
    O   |
   /|   |
    |   |
        |
    ________''',
    '''
    +===+
    O   |
   /|\  |
    |   |
        |
    ________''',
    '''
    +===+
    O   |
   /|\  |
    |   |
     \  |
    ________''',
    '''
    +===+
    O   |
   /|\  |
    |   |
   / \  |
    ________''',
    '''
    +===+
    O   |
   /|\_ |
    |   |
   / \  |
    ________''',
    '''
    +===+
    O   |
  _/|\_ |
    |   |
   / \  |
    ________''',
    '''
    +===+
    O   |
  _/|\_ |
    |   |
   / \_ |
    ________''',
   '''
   +===+
   O   |
 _/|\_ |
   |   |
 _/ \_ |
   ________''']
    if guess_number >= len(gallow_pics):
        return print(gallow_pics[-1])
    return print(gallow_pics[guess_number])


def unique(broken_letters):
    unique_letters = []
    for letter in broken_letters:
        if letter not in unique_letters:
            unique_letters.append(letter)
    return len(unique_letters)


def word_display(correct_letters, guessed_letters):
    '''
    displays the word based on letters that have been guessed with _ replacing letters that haven't been guessed.
    :param correct_letters: list of letters in word in order
    :param guessed_letters: word of letters that have been guessed
    :return: print's a string of letters and underscores based on guessed letters.

    '''
    display = []
    for letter in correct_letters:
        if letter not in guessed_letters:
            display.append('_')
        else:
            display.append(letter)
    return print(''.join(display))


def guess(broken_letters, remaining):
    '''
    Has user continue to guess until user has guessed the word
    :param broken_letters: list of letters in word being guessed
    :param remaining: number of unique letters in word being guessed
    :return: total_guesses: total guesses it took to guess word, incorrect_guesses: total incorrect guesses in the word.
    '''
    guessed_letters = []
    total_guesses = 0
    incorrect_guesses = 0
    correct_guesses = 0
    while True:
        gallows(incorrect_guesses)
        print('===============================================================================================')
        print(f'Guessed Letters: {guessed_letters}\nCorrect Guesses: {correct_guesses}\nIncorrect Guesses: {incorrect_guesses}')
        print('===============================================================================================')
        word_display(broken_letters, guessed_letters)
        print('===============================================================================================')
        inputed_letter = input('Guess a letter: ')
        if inputed_letter.isupper():
            inputed_letter = inputed_letter.lower()
        print('===============================================================================================')
        if inputed_letter in guessed_letters:
            print('Oops! You already guessed that letter! Try again.')
            print('===============================================================================================')
            total_guesses += 1
            continue
        guessed_letters.append(inputed_letter)
        if inputed_letter in broken_letters:
            print('Nice Guess!')
            print('===============================================================================================')
            remaining -= 1
            correct_guesses += 1
            if remaining == 0:
                return total_guesses, incorrect_guesses
        else:
            print('*Buzzer* Nope!')
            print('===============================================================================================')
            incorrect_guesses += 1
        total_guesses += 1
        continue


def pick_word(used_words):
    """
    Pick a word that hasn't been used in past games
    :param used_words: words that have been used.
    :return: word
    """
    all_words = ['ski', 'cool', 'magic', 'powers', 'special', 'absolute', 'zealously', 'tablecloth', 'habilitator', 'kindergarten']
    possible_words = []
    for word in all_words:
        if word not in used_words:
            possible_words.append(word)
    if len(possible_words) == 0:
        return False
    return random.choice(possible_words)


def main():
    # actual code being run, ends when we run out of words or when the user wants to quit
    used_words = []
    print('*****************************************')
    print('|||Let\'s get ready to Hangmannnnn!!!!|||')
    print('*****************************************')
    print('===============================================================================================')
    while True:
        correct_word = pick_word(used_words)
        used_words.append(correct_word)
        broken_word = list(correct_word)
        unique_count = unique(broken_word)
        if not correct_word:
            print('We\'re all out of words folks :(. Have a great day!')
            return
        print(f'Your word has {len(broken_word)} letters! Good luck!')
        print('===============================================================================================')
        guesses, incorrect_guesses = guess(broken_word, unique_count)
        print(f'Congrats! You got it!\nThe correct word was: {correct_word}\nIt took you {guesses} guesses!')
        if incorrect_guesses >= 11:
            print('You accidentally hung the man! :(')
        else:
            print('You didn\'t hang the man! Great job! :)')
        print('===============================================================================================')
        print('Would you like to play again? (y/n)')
        inputed_letter = input()
        if inputed_letter.isupper():
            inputed_letter = inputed_letter.lower()
        if inputed_letter == 'y':
            continue
        else:
            print('Thanks for playing mate! Have a wonderful day!!')
            return


if __name__ == '__main__':
    main()