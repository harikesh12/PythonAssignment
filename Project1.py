# Problem Statement: You have to write a Word Puzzle Game in which the user has to form
# the correct word out of a given set of characters. In the game the user has to solve this
# puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
# in random sequence. Give the user score +1 for each correct answer and give -1 for each
# wrong answer. At last print the final score. You can store any number of words in the list, but
# in each round of the game only 5 words are shown to the user.

import random
def wordPuzzle():
    word=["erathf","anme","ruitf","pplea","acr","nanaba","kibe"]
    correctWord=["father","name","fruit","apple","car","banana","bike"]
    i=1                   # counter for having to display just 5 word 
    right=0
    wrong=0
    print("Please do correct formation of given word")
    while i<=5:
        r_i = random.randint(0,len(word)-1)   # to generate random index out of "word" list
        print("Your" , i,"word is : ", word[r_i])
        a=input("Enter correct formation of word : ")
        if a==correctWord[r_i]:
            print("You have entered correct answer ")
            word.remove(word[r_i])            # removed word from list so that it wont repeat in next iteration of random generation of Index 
            correctWord.remove(correctWord[r_i])  # removed word from "correct word"list so that it is not present at wrong index of wrong word
            right+=1
            i+=1
        else:
            print("Entred input is wrong")
            word.remove(word[r_i])             # removed word from list so that it wont repeat in next iteration of random generation of Index 
            correctWord.remove(correctWord[r_i])   # removed word from "correct word"list so that it is not present at wrong index of wrong word
            wrong-=1
            i+=1
    return right+wrong    
print("Your Total score is ", wordPuzzle())
