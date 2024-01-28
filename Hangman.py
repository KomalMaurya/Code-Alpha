#Hangman Game
import random                                       #importing random module
import hangman_stages
List_of_words = ['Krishna','Radha','Ram','Ganesh','Shiva','Narayana','Laxmi','Saraswati','Paravti','Sita','Hanuman','Brahma','Sati','Khatushyam','Ganga','Yamuna','Surya','Jagannath','Rameshwaram','Kedarnath','Badrinath']   #Making a list of words!
chosen_word = random.choice(List_of_words)          #Choosing a random word from the list
chance=6
result=[]
for i in chosen_word:
    result+='_'
    
while True:
    guess_alpha = input("Guess a letter : ")        #Guess the Word
    for j in range(len(chosen_word)):
        alpha=chosen_word[j]
        if alpha==guess_alpha:
            result[j]=guess_alpha
    print(result)
    if guess_alpha not in chosen_word:
        chance-=1 
        if chance==0:
            print("All your chances are over! You LOSE!")
            print(chosen_word)
            print(hangman_stages.stages[0])
            break
    if '_' not in result:
        print("You WON!")
        break
    print(hangman_stages.stages[chance])