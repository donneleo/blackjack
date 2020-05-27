print("Let's play Blackjack. This game pays 2/1.")

print("How much is in your wallet tonight?")
wallet = int(input())

finished = bool(False)

print("How much would you like to bet?")
bet = int(input())
wallet = wallet - bet

print("OK, you've bet ", bet,". Let's deal.")

total = 0
import random
card1 = random.randint(1, 14)
if card1 == 1:
    cardname = "Ace"
    cardValue = 11
elif card1 == 11:
    cardname = "Jack"
    cardValue = 10
elif card1 == 12:
    cardname = "Queen"
    cardValue = 10
elif card1 == 13:
    cardname = "King"
    cardValue = 10
else:
    cardname = card1
    cardValue = card1

total += cardValue
print("You drew a ", cardname, ". Your total is now ", total)

dealerTotal = 0
dealerCard1 = random.randint(1, 14)
if dealerCard1 == 1:
    cardname = "Ace"
    cardValue = 11
elif dealerCard1 == 11:
    cardname = "Jack"
    cardValue = 10
elif dealerCard1 == 12:
    cardname = "Queen"
    cardValue = 10
elif dealerCard1 == 13:
    cardname = "King"
    cardValue = 10
else:
    cardname = card1
    cardValue = card1

total += cardValue
print("You drew a ", cardname, ". Your total is now ", total)

card2 = random.randint(1, 14)
if card2 == 1:
    cardname = "Ace"
    cardValue = 11
elif card2 == 11:
    cardname = "Jack"
    cardValue = 10
elif card2 == 12:
    cardname = "Queen"
    cardValue = 10
elif card2 == 13:
    cardname = "King"
    cardValue = 10
else:
    cardname = card1
    cardValue = card1
total += cardValue
print("You drew a ", cardname, ". Your total is now ", total)

if total == 21:
 bet *= 2
 wallet += bet
 print("Congrats. That's a winner. You've won ", bet, " and your wallet now has ", wallet)
elif total > 21:
    print("Sorry. Your bust!")

