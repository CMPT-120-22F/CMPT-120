#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''
import random
#I don't know if you want us to import stuff or not, but you said to google things and this is what google said to do

def bust():
    listCards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
                 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
    card1 = random.choice(listCards)
    card2 = random.choice(listCards)
    card3 = random.choice(listCards)
    
    cardTotal = card1 + card2 + card3

    if cardTotal <= 21:
        return cardTotal
    elif cardTotal > 21 and (card1 == 11 or card2 == 11 or card3 == 11):
        cardTotal = cardTotal - 10
        return cardTotal
    elif cardTotal > 21:
        print(cardTotal)
        return "Bust!"

def main():
    score = bust()
    print(score)
    if score == 21:
        print("not blackjack but good job!")
main()
