#! python3
import os


#adventure game
run = True
menu = True
play = False

#funtions to look good
def draw():
    print("Xx-----------------------xX")

#funtions to use in game

while run:
    while menu:
        draw()
        print("1. New game")
        print("2. Save & quit")
        draw()
        choice = input("> ")

        
        #menu bar ------------------------------ code
        if choice == "1":
            name = input("What is your name: ")
            menu = False 
            play = True

        elif choice == "2":
            quit()
        #menu bar ------------------------------ code
        

    while play:
        print("""\033[36;1;40m Xx---- WELLCOM TO LEDSEN ----xX 
              \n\033[34;1;40m You are in a deep cave name ledselt of no man returns. 
              A cave of dead end.\n Monsters are every were and you have to find the
              \033[31;1;40m Red heart
              \033[34;1;40m to save your mother and get out of this maze like cave.""")
        
        First = input("\033[0;37;40m A monster is coming at you.\n On the ground there is a sword and a dagger. What will you use: ")

        if First == "sword":
            print("You have a sword now")
        else:
            print("You get the dagger")

        Destionation = input("> ")
        
        Destionation = Destionation.upper()
        if Destionation  == "QUIT":
            play = False
            menu = True

    

        

        
