import random 
words=['Abstruse','Alias','Antithesis','Apathetic','Asthetic','Beguile','Bombastic','Callous','Colonel','Covet','Claustrophobia','Crypt','Duplicate','Dwarves','Eclectic','Fall','Gazebo','Gypsy','Haphazard','Happiness','Heterogenous','Insane','Irony','Jinx','Lieutenant','Masquerade','Memento','Moron','Paradise','Pervert','Pixel','Polka','Quarell','Rat','Remix','Rogue','Sphinx','Tangent','Update','Velocity','Willy','Xylophone','Yacht','Zealous','Zephyr']
word = random.choice(words) 
print("Guess The Characters:") 
guesses = '' 
turns = 7
while turns > 0: 
    failed = 0
    for char in word:      
        if char in guesses:  
            print(char) 
              
        else:  
            print("_") 
            failed = failed + 1
            
    if failed == 0: 
        print("You Win")  
        print("The Word Is: ", word)  
        break
    
    guess = input("Guess A Character:") 
    guesses = guesses + guess  

    if guess not in word: 
            turns = turns - 1
            print("You Have", turns, 'More Guesses') 
            if (turns == 7):
                print("Wrong Guess, Try Again")
                print()
                print()
                print()
                print()
                print("___|___")
                print()

            if (turns == 6):
                print("Wrong Guess, Try Again")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("___|___")

            if (turns == 5):
                print("Wrong Guess, Try Again")    
                print("   ____________")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   | ")
                print("___|___")

            if (turns == 4):
                print("Wrong Guess, Try Again")
                print("   ____________")
                print("   |          _|_")
                print("   |         /   \\")
                print("   |        |     |")
                print("   |         \\_ _/")
                print("   |")
                print("   |")
                print("   |")
                print("___|___")

            if (turns == 3):
                print("Wrong Guess, Try Again")
                print("   ____________")
                print("   |          _|_")
                print("   |         /   \\")
                print("   |        |     |")
                print("   |         \\_ _/")
                print("   |           |")
                print("   |           |")
                print("   |")
                print("___|___")

            if (turns == 2):
                print("Wrong Guess, Try Again")
                print("   ____________")
                print("   |          _|_")
                print("   |         /   \\")
                print("   |        |     |")
                print("   |         \\_ _/")
                print("   |           |")
                print("   |           |")
                print("   |          / \\ ")
                print("___|___      /   \\")


            if (turns == 1):
                print("GAME OVER!")
                print("   ____________")
                print("   |          _|_")
                print("   |         /   \\")
                print("   |        |     |")
                print("   |         \\_ _/")
                print("   |          _|_")
                print("   |         / | \\")
                print("   |          / \\ ")
                print("___|___      /   \\")
                print("GAME OVER! The Word Was",word)

