import random

Name = str(input("What is your name ?"))

print("Good Luck {0} !" .format(Name))
print("Enjoy the Game!")
print("Start Guessing...")

#List of Words
Wordlist = ["About" , "Alert" , "Argue" , "" , "Above" , "Alike" , "Arise" , "Began" , "Abuse" , "Alive" , "Array" , "Begin"] 

#Choose a Random Word
Word = random.choice(Wordlist)
Word = Word.lower()
#Guess the Word
Guesses = " "

turns = 10

while turns > 0:
    failed = 0
    
    for character in Word:
        if character in Guesses:
            print(character , end= " ")
            
        else:
            print("_")
            failed += 1
            
    if failed == 0:
        
        print("You Win !")
        print("The Word is {0}".format(Word))
        break
    
    print()
    Guess = str(input("Guess a Character"))
    Guesses += Guess
    
    if Guess not in Word:
        turns -= 1
        print("Wrong \nTry Again")
        print("You have {0} more guesses".format(turns))
        
        if turns == 0:
            print("You Lose")
    