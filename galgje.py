import time

print "welkom bij Galgje"

time.sleep (1)

print "Speler 1 kiest een woord, speler 2 moet deze gaan raden"

time.sleep(2)

print "Speler 2 mag maximaal 9 keer een verkeerde letter kiezen"

time.sleep (3)

print "Als speler 2 alle letters goed geraden heeft, wint hij het spel"

time.sleep (1)
print "Speler 1, welk woord moet speler 2 gaan raden?"

def get_word():
    word = raw_input()
    return word.upper()

#interface die geprint in console word
def play(word):
    word_completion = "_" * len(word)#streepjes voor niet geraden woorden
    guessed = False #standaard 0 geraden woorden
    guessed_letters = []#list var voor geschatte letters
    guessed_words = []#list var voor geschatte woorden
    tries = 9 #hoeveelheid pogingen
    print("Laten we galgje spelen!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    #game mechanisme; boven de 0 pogingen is doorgaan
    while not guessed and tries > 0:
        guess = raw_input("Raad een letter of woord").upper()
        if len(guess) == 1 and guess.isalpha():#als gok niet goed is dan
            if guess in guessed_letters:
                print("Je hebt dit woord al geraden", guess)
            elif guess not in word:
                print(guess, "Zit niet in dit woord")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Goed gedaan,", guess, "zit in het woord")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Je hebt het woord al geraden", guess)
            elif guess != word:
                print(guess, "Is niet het woord.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Ongeldige karakters")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Goed gedaan! Je hebt gewonnen!")
    else:
        print("Oeps, jouw pogingen zijn op, het woord was " + word)


def display_hangman(tries):
    stages = [  # fase 9 - game over
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # fase 8
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # fase 7
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # fase 6
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # fase 5
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # fase 4
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # fase 3
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                #fase 2
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                #fase 1: leeg
                """
                   
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                #fase 0 default
                """
                   
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while raw_input("Opnieuw spelen? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
    
    
    #https://www.youtube.com/watch?v=m4nEnsavl6w 
    #tutorial die ik gevolgd heb.
