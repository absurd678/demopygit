import random
WORDS = ('Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch', 'Verkhnenovokutlumbetyevo', 'Yamagawahamachiyogamizu')
word = random.choice(WORDS)
correct = word
correct = random.sample(correct, k=len(correct))
correct1 = ''.join(correct)

i = 0
print("Hello there, it's bigbrain game to see you iq level,\nYou will try to guess the name of city \nYou have only 3 tries, good luck","\n",correct1)
myword = str(input("Write your variant: "))
while i < 60:
    if i < 2:
        if myword != word:
            print("No, it isn't, try again!")
            i += 1
            myword = str(input("Write your variant: "))
        else:
            print("Congratulations!")
            break
    else:
        print("You lost, unfortunately, the word is - ", word)
        n = input("Click Enter to see my troll face)")
        print(
              """            
░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░██░░▀█▄▄▄█▄▄█▄████░█
░░░░█░░░▀▀▄░█░░░█░███████░█
░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█               
              """
              )
        break
