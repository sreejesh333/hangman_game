import os
import tempfile
import hangman

def test_select_random_word_min_length():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["cat\n","elephant\n","mouse\n","dog\n",])
    
    f.close()
    secret_word = hangman.get_random_word(name)
    assert secret_word == "elephant"

    os.unlink(name)

def test_select_random_word_no_non_alpha_chars():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["pine's\n","Dr.\n","Ångström\n","elephant\n"])
    f.close()
    secret_word = hangman.get_random_word(name)
    assert secret_word == "elephant"

    os.unlink(name)

def test_select_random_word_no_capitals():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["Alexander\n","AMD\n","California\n","elephant\n"])
    f.close()

    secret_word = hangman.get_random_word(name)
    assert secret_word == "elephant"

    os.unlink(name)


def test_select_random_word_no_repetitions():
    secret_words = set()
    for _ in range(10):
        secret_words.add(hangman.get_random_word())
    assert len(secret_words) == 10
    
def test_get_word():
     secret_word = hangman.get_word("elephant")
     assert secret_word == "________"



def test_masked_word_correctguesses() :
    assert hangman.masked_word("elephant" , ["p"]) == "___p____"

def test_masked_word_wrongguesses() :
    assert hangman.masked_word("elephant" , ["x"]) == "________"

def test_masked_word_noguess() :
    assert hangman.masked_word("elephant" , [" "]) == "________"

def test_masked_word_repeatedletters() :
    assert hangman.masked_word("elephant" , ["e"]) == "e_e_____"

def test_masked_word_enter_repeat_letter() :
    assert hangman.masked_word("elephant" , ["a","a"]) == "_____a__"

def test_masked_word_full_wrd_correct() :
    assert hangman.masked_word("elephant" , ["e","l","p","h","a","n","t"]) == "elephant"


# def test_check_game_win():
#     assert hangman.check_game_win('elephant', 'elephant') == 'You Win!'

# def test_check_game_loose():
    
#     assert hangman.check_game_win('elephant', '_lephant') == 'You Lose!'


# def test_check_game_next_turn():
    
#     assert hangman.check_game_loop('_lephant', 'elephant',) == True

# def test_game_out_of_turns():
#     assert hangman.check_game_loop('-leph-nt','elephant',['z','y','x','j','k','o','q','u']) == False






def test_status_no_guess() :
    secrt_wrd = "elephant"
    guesses = []
    turns = 7
    assert hangman.get_status(secrt_wrd, guesses , turns) == '''word:________   guesses :    turns_left : 7'''

def test_get_status_basic():
    secret_word = "elephant"
    guesses = ["p", "h", "v"]
    turns_remaining = 3
    hangman.get_status(secret_word, guesses, turns_remaining)
    assert hangman.get_status(secret_word, guesses, turns_remaining) == """Secret word:___ph___
Guesses : p h v
Remaining turns : 3"""









    
