import random

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



def usr_input():
    return input("enter the letter :").lower()

def masked_word(word , guess) :
    guess_wrd = []
    for i in word :
            if i in guess :
                guess_wrd.append(i) 
            
            else :
                guess_wrd.append("_")
    
    return "".join(guess_wrd)
            
def update_word(secret_word,guesses,guess,turns) :
    if guess not in guesses :
        if guess not in secret_word  :
            turns -= 1
            return turns
        else :
            return turns
        




        






# def play_hang(word) :
#     wrd_completion = get_word(word)
#     guessed = False
#     guess_letter = []
#     tried = 6
#     print(wrd_completion)
    
#     while not guessed and tried > 0 :
#         guess = usr_input()

        
#         if len(guess) == 1 and guess.isalpha() :
#             if guess  in guess_letter :
#                 print("already written letter")
            
#             elif guess not in word :
#                 tried = display_tries(tried)
#                 print("no of tries left :",tried)
#                 print(wrd_completion)
#                 guess_letter.append(guess)
            
#             else :
#                 guess_letter.append(guess)
#                 wrd_list = list(wrd_completion)
#                 indexnum = []
#                 for i , letter in enumerate(word) :
#                     if letter == guess :
#                         indexnum.append(i)
#                 for index in indexnum :
#                     wrd_list[index*2] = guess
#                     wrd_completion = "".join(wrd_list)
#                     if "_" not in wrd_completion :
#                         guessed = True
#                         # print(guessed)
#                 print(wrd_completion)
                
        

#         else :
#             print("wrong guess")
#             print(wrd_completion)
#             print("\n")


#     if guessed == True :
#         print("u guessed right ...the word is :"+word)

        
#     else :
#         print("sorry u loose , the word is :"+ word )

       
    
   
   

def main():
    word = get_random_word()
    play_hang(word)
    
    while input("do u want a continue (y/n):") == 'y' :
        word =  get_random_word()
        play_hang(word)

    
if __name__ == "__main__":
    main()




                        
                 