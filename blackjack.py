from bjart import logo
import random
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]


#function to draw random cards
def draw_card(numberOfCardsToPick,who):
  count = 0
  while count < numberOfCardsToPick:
    who.append(random.choice(deck))
    count+=1
  
def checkScore(who):
    if sum(who) == 21 and len(who) == 2:
        return 0
    else:
        return sum(who)
  
def blackjack():
#setup the game
    notbust = True
    print(logo)
    player_hand = []
    dealer_hand = []
    player_hand.clear()
    dealer_hand.clear()
    draw_card(2,player_hand)
    draw_card(2,dealer_hand)
    print(f"Your hand is: {player_hand}\n")
    print(f"The Dealer\'s hand is: [{dealer_hand[0]}, ?] ")

#check for player blackjack
    if checkScore(player_hand) == 0:
        notbust = False
        print("Blackjack! You Win!")

#player's turn
    while notbust:
        handtotal = checkScore(player_hand)
        playersAnswer = input("Do you want to Hit or Stand? ").lower()
        while not playersAnswer in ("hit","stand"):
            playersAnswer = input("Please change your answer.  Do you want to Hit or Stand? ").lower()
        if playersAnswer == "hit":
            draw_card(1,player_hand)
            print(f"You got a {player_hand[-1]}")
            print(player_hand)
            handtotal += player_hand[-1]
            if handtotal > 21:
                notbust = False
                print(f"oh no, you busted. You have {handtotal}")
            else:
                print(f"You've got {handtotal} now what?\n")
        else:
            #notbust = False
            break
#dealer's turn
    if notbust:
        print("Dealer's turn.\n")
        dealertotal = checkScore(dealer_hand)
        dealerbust = False
        while not dealerbust:
            print(dealer_hand)
            if dealertotal == 0:
                dealerbust = True
                print("Ouch, dealer has Blackjack, you lose")
            elif dealertotal > 21:
                dealerbust = True
                print("Dealer busted, you win!")
            elif dealertotal > 16:
                print(f"Dealer has {dealertotal}, dealer stands.")
                if dealertotal > handtotal:
                    print("Sorry, you lose.")
                    dealerbust = True
                elif dealertotal < handtotal:
                    print("Congratulations!  You beat the dealer!")
                    dealerbust = True
                else:
                    print("You tied, it's a push.")
                    dealerbust = True

            else:
                print(f"Dealer has {dealertotal}, dealer hits.\n")
                draw_card(1,dealer_hand)
                dealertotal += dealer_hand[-1]

    while input("Want to play again? (y/n)").lower() == 'y':
        blackjack()



blackjack()


