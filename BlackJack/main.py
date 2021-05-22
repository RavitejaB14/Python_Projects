############### Blackjack Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo
def deal_card() :
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2 :
     return 0
  
  if 11 in cards and sum(cards) > 21:
     cards.remove(11)
     cards.append(1)

  return sum(cards)


def compare(user_score,computer_score) :
  if user_score == computer_score :
    return "Draw"
  elif computer_score == 0 :
    return "you Lose, Opponent has BlackJack"
  elif user_score == 0 :
    return "You Win, You got a Black Jack"
  elif user_score > 21 :
    return "You Lose"
  elif computer_score > 21 :
    return "You Win, Opponent has greater than 21"
  else :
    if user_score > computer_score :
       return "You Win"
    else: 
      return "Opponent Wins"
    
def playGame():
  print(logo)
  user_cards = []
  computer_cards = []
  Game=False
  for _ in range(2) : 
      user_cards.append(deal_card())
      computer_cards.append(deal_card())


  while not Game:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards} , current Score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21 :
      Game=True

    else:
       user_should_deal = input("Type 'y' to get another card, type 'n' to pass\n")
       if(user_should_deal == 'y'):
          user_cards.append(deal_card())
       else:
         Game = True

  while computer_score !=0 and computer_score < 17 :
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f" Your final hand : {user_cards}, final score : {user_score}")
  print(f" Computer final hand : {computer_cards}, final score : {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ")== "y":
  clear()
  playGame()
