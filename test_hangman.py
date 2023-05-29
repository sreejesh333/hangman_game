import os
import tempfile
import hangman

def test_select_random_word_min_length():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["cat\n","elephant\n","mouse\n","dog\n",])
    
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "elephant"

    os.unlink(name)

def test_select_random_word_no_non_alpha_chars():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["pine's\n","Dr.\n","Ångström\n","elephant\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "elephant"

    os.unlink(name)

def test_select_random_word_no_capitals():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["Alexander\n","AMD\n","California\n","elephant\n"])
    f.close()

    for _ in range(20):
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

# def test_display_tries():
#     try_check = hangman.display_tries(6)
#     assert try_check == 5

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

    








    
