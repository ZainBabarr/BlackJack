import random, time, os

# Initializing Variables
playerSum = 0
dealerSum = 0

playerInput = ""

numPlayer1 = 0
numPlayer2 = 0
numPlayer = 0

numDealer = 0
numDealer1 = 0
dealerCard = 0

playAgain = ""

# Creating random list for picking cards
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A"]

# Setting up loop, if user wants to exit, press Q
while (playerInput != "Q"):
    
    # Dealer Cards

    # Choosing random cards for dealer
    dealerCard1 = (random.choice(cards))
    dealerCard = (random.choice(cards))

    # Dealer
    print("\nDealer:")

    # When 10 is chosen, formatting needs to be corrected accordingly
    if dealerCard1 == 10:
        print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   10   |      |    ?   |\n|        |      |        |\n|________|      |________|")
    
    # Any other card chosen will format accordingly
    else:
        print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   " + str(dealerCard1) + "    |      |    ?   |\n|        |      |        |\n|________|      |________|")

    #Player Cards

    # Choosing random cards for players
    playerCard1 = (random.choice(cards))
    playerCard2 = (random.choice(cards))
   
    # Player
    print("\n\nPlayer:")

    # PRINTING HAND
    
    # When cPlayer1 = 10 and cPlayer2 = 10 is chosen, formatting needs to be corrected accordingly
    if (playerCard1 == 10 and playerCard2 == 10):
        print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   10   |      |   10   |\n|        |      |        |\n|________|      |________|")
    
    # When cPlayer1 = 10 is chosen, formatting needs to be corrected accordingly
    elif playerCard1 == 10:
        print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   10   |      |   " + str(playerCard2) + "    |\n|        |      |        |\n|________|      |________|")
    
    # When cPlayer2 = 10 is chosen, formatting needs to be corrected accordingly
    elif playerCard2 == 10:
        print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   " + str(playerCard1) + "    |      |   10   |\n|        |      |        |\n|________|      |________|")
    
    # Any other card chosen will format accordingly
    else:
        print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   " + str(playerCard1) + "    |      |    " + str(playerCard2) + "   |\n|        |      |        |\n|________|      |________|")

    # Calculations

    # Dealer
    
    #If first dealer card is A
    if (dealerCard1 == "A") and (dealerCard== "A"):
        
        dealerSum = 12

    elif (dealerCard1 == "A") and (int(dealerCard) < 10):

        numDealer1 = 11

        dealerSum = numDealer1 + dealerCard

    elif (dealerCard1 == "A") and (int(dealerCard) == 10):
        
        dealerSum = 21
    
    elif (dealerCard1 == "A") and (int(dealerCard) > 10):

        numDealer1 = 1

        dealerSum = numDealer1 + dealerCard

    #If second dealer card is A
    elif (dealerCard == "A") and (int(dealerCard1) < 10):

        numDealer = 11

        dealerSum = numDealer + dealerCard1

    elif (dealerCard == "A") and (int(dealerCard1) == 10):
        
        dealerSum = 21
    
    elif (dealerCard == "A") and (int(dealerCard1) > 10):

        numDealer = 1

        dealerSum = numDealer1 + dealerCard1
    
    else:

        dealerSum = dealerCard1 + dealerCard

    # Player
    #If both aces are in players hand
    if (playerCard1 == "A") and (playerCard2 == "A"):

        #First ace
        while (numPlayer1 != 1) or (numPlayer1 != 11):

            numPlayer1 = int(input("Enter First Ace Value (1 or 11): "))

            #Once player has selected, break from loop
            if numPlayer1 == 1 or numPlayer1 == 11:

                break
        
        #If player chooses 11, 2nd ace must be 1 because 11 + 11 = 22
        if numPlayer1 == 11:
            
            numPlayer2 = 1

        #Second ace
        elif numPlayer1 == 1:

            while (numPlayer2 != 1) or (numPlayer2 != 11):

                numPlayer2 = int(input("Enter Second Ace Value (1 or 11): "))

                #Once player has selected, break from loop
                if numPlayer2 == 1 or numPlayer2 == 11:

                    break
        
        playerSum = numPlayer1 + numPlayer2

    #If first card is A and second card is less than 10
    elif (playerCard1 == "A") and (playerCard2 <= 9):
        
        numPlayer1 = int(11)

        playerSum = numPlayer1 + playerCard2

    #If second card is A and first card is less than 10
    elif (playerCard2 == "A") and (playerCard1 <= 9):
        
        numPlayer2 = int(11)

        playerSum = int(numPlayer2) + int(playerCard1)

    elif (playerCard1 == "A") and (playerCard2 == 10):

        playerSum = int(21)

    elif (playerCard2 == "A") and (playerCard1 == 10):

        playerSum = int(21)

    else:
        playerSum = int(playerCard1) + int(playerCard2)

    #Loop for user input
    while (playerSum < 22):

        playerInput = input("\nHIT | STAND (Q to Quit) [Player Sum: " + str(playerSum) + "] ")

        if playerInput == "Q":
            break

        if playerInput == "HIT":
            
            time.sleep(0.3)
            print("\n---PLAYER DRAWS CARD---\n")

            numPlayer = (random.choice(cards))

            if numPlayer == "A":
                numPlayer = 1

            playerSum = playerSum + int(numPlayer)

            if numPlayer == 10:
                print("__________\n|        |\n|        |\n|   10   |\n|        |\n|________|")
            
            else:
                print("__________\n|        |\n|        |\n|   " + str(numPlayer) + "    |\n|        |\n|________|")

            if playerSum > 21:
                
                input("\nYou lost, final score: " + str(playerSum))

                os.system('cls')
                
                break
            
        if playerInput == "STAND":

            print("\n--------------------------\n")

            if (dealerSum == playerSum):

                print("     ---DEALER CARDS---\n")

                # When dealerCard1 = 10 and dealerCard = 10 is chosen, formatting needs to be corrected accordingly
                if (dealerCard1 == 10 and dealerCard == 10):
                    print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   10   |      |   10   |\n|        |      |        |\n|________|      |________|")
                
                # When dealerCard1 = 10 is chosen, formatting needs to be corrected accordingly
                elif dealerCard1 == 10:
                    print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   10   |      |   " + str(dealerCard) + "    |\n|        |      |        |\n|________|      |________|")
                
                # When dealerCard = 10 is chosen, formatting needs to be corrected accordingly
                elif dealerCard == 10:
                    print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   " + str(dealerCard1) + "    |      |   10   |\n|        |      |        |\n|________|      |________|")
                
                # Any other card chosen will format accordingly
                else:
                    print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   " + str(dealerCard1) + "    |      |    " + str(dealerCard) + "   |\n|        |      |        |\n|________|      |________|")

                input("\nDraw, total score: " + str(playerSum) + " (Press Enter to Play Again) ")

                break

            print("     ---DEALER CARDS---\n")

            # When dealerCard1 = 10 and dealerCard = 10 is chosen, formatting needs to be corrected accordingly
            if (dealerCard1 == 10 and dealerCard == 10):
                print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   10   |      |   10   |\n|        |      |        |\n|________|      |________|")
            
            # When dealerCard1 = 10 is chosen, formatting needs to be corrected accordingly
            elif dealerCard1 == 10:
                print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   10   |      |   " + str(dealerCard) + "    |\n|        |      |        |\n|________|      |________|")
            
            # When dealerCard = 10 is chosen, formatting needs to be corrected accordingly
            elif dealerCard == 10:
                print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   " + str(dealerCard1) + "    |      |   10   |\n|        |      |        |\n|________|      |________|")
            
            # Any other card chosen will format accordingly
            else:
                print("__________      __________  \n|        |      |        |\n|        |      |        |\n|   " + str(dealerCard1) + "    |      |    " + str(dealerCard) + "   |\n|        |      |        |\n|________|      |________|")
            
            time.sleep(1)

            print("\n")

            if (dealerSum > playerSum) and (dealerSum < 22):

                input("\nYou lost, final score: " + str(playerSum) + " (Press Enter to Play Again) ")

                os.system('cls')

                break

            if dealerSum < 16:

                # Draw more cards for dealer
                while (dealerSum < 16):

                    dealerCard = (random.choice(cards))

                    if dealerCard == "A" and dealerSum < 11:
                        numDealer = 11

                        dealerSum = dealerSum + numDealer

                    elif dealerCard == "A" and dealerSum > 10:
                        numDealer = 1

                        dealerSum = dealerSum + numDealer

                    else:

                        dealerSum = dealerSum + dealerCard

                    if dealerCard == 10:
                        print("__________\n|        |\n|        |\n|   10   |\n|        |\n|________|")
            
                    else:
                        print("__________\n|        |\n|        |\n|   " + str(dealerCard) + "    |\n|        |\n|________|")

                    time.sleep(1)

            if (dealerSum == playerSum):

                input("\nDraw, total score: " + str(playerSum) + " (Press Enter to Play Again) ")

                os.system('cls')

                break

            elif playerSum == 21:

                input("\nYou won, final score: " + str(playerSum) + " (Press Enter to Play Again) ")

                os.system('cls')

                break

            elif dealerSum == 21:
                input("\nYou lost, final score: " + str(playerSum) + " (Press Enter to Play Again) ")

                os.system('cls')

                break
                    
            elif (dealerSum > playerSum) and (dealerSum < 22):
                input("\nYou lost, final score: " + str(playerSum) + " (Press Enter to Play Again) ")

                os.system('cls')

                break
            
        
            elif (playerSum > dealerSum) and (playerSum < 22):

                input("\nYou won, final score: " + str(playerSum) + " (Press Enter to Play Again) ")

                os.system('cls')

                break

            elif (dealerSum > playerSum) and (dealerSum > 21):

                input("\nYou won, final score: " + str(playerSum) + " (Press Enter to Play Again) ")

                os.system('cls')

                break

    print("\n--------------------------\n")

    if playerInput == "Q":
            os.system('cls')
            break

    #Resetting all variables
    playerSum = 0
    dealerSum = 0

    playerInput = ""

    numPlayer1 = 0
    numPlayer2 = 0
    numPlayer = 0

    numDealer = 0
    numDealer1 = 0
    dealerCard = 0

    playAgain = ""