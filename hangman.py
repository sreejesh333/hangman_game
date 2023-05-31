import random

guessed = 0
correct = 1
wrong = 2

def get_random_word(wordfile = "/usr/share/dict/words"):
    candidate_words = []
    with open(wordfile) as f: 
        for word in f:
            word = word.strip()
            if len(word) >= 6 and word.islower() and word.isalpha() :
                candidate_words.append(word)
    word = random.choice(candidate_words)
    return word


def get_word(word) :
    len_wrds = "_" * len(word)
    return len_wrds




def masked_word(word , guess) :
    guess_wrd = []
    for i in word :
            if i in guess :
                guess_wrd.append(i) 
            
            else :
                guess_wrd.append("_")
    return "".join(guess_wrd)



def get_status(secret_word, guesses, turns_remaining):
    mask_word = masked_word(secret_word, guesses)
    guessed_letters = " ".join(guesses)
    return f"""word:{mask_word}   guesses : {guessed_letters}   turns_left : {turns_remaining}"""

def check(secret_word, guesses, turns_remaining, new_guess):
    if new_guess in guesses:
        return guessed, turns_remaining
    else:
        guesses.append(new_guess)
        if new_guess in secret_word:
            return correct, turns_remaining
        else:
            return wrong, turns_remaining-1

        

def game(secret_word, guesses, turns_remaining):
    if turns_remaining == 0:
        return True, f"You lost...The word is {secret_word}"
    masked = masked_word(secret_word, guesses)
    if "_" in masked:
        return False, None
    else:
        return True, f"You won...The word is {secret_word}"


    
def main():
    secret_word = get_random_word()
    guesses = []
    turns_remaining = 8
    while True:
        print (get_status(secret_word, guesses, turns_remaining))
        guess = input("Enter a letter ")
        
        status, turns_remaining = check(secret_word, guesses, turns_remaining, guess)
        if status == guessed:
            print ("You already guessed that")
        
        finished, message = game(secret_word, guesses, turns_remaining)
        if message:
            print (message)
        if finished:
            break


if __name__ == "__main__":
    main()
            




                        
                 