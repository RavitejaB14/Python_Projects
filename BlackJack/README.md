# BlackJack Rules

1. The deck is unlimited in size. 
2. There are no jokers. 
3. The Jack/Queen/King all count as 10.
4. The the Ace can count as 11 or 1.
5. Use the following list as the deck of cards:
6. cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
7. The cards in the list have equal probability of being drawn.
8. Cards are not removed from the deck as they are drawn.
9. The computer is the dealer.


#Code Hints:

Hint 1: Create a deal_card() function that uses the List below to *return* a random card.11 is the Ace.
Hint 2: Deal the user and computer 2 cards each using deal_card() and append().
Hint 3: Create a function called calculate_score() that takes a List of cards as input and returns the score.
Hint 4: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.Look up the sum() function to help you do this.
Hint 5: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
Hint 6: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
Hint 7: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
Hint 8: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
Hint 9: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
Hint 10: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
Hint 11: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.