import random
player_card1 = random.randint(1, 11)
dealer_card1 = random.randint(1, 11)

player_card2 = random.randint(1, 11)
dealer_card2 = random.randint(1, 11)

player = player_card1 + player_card2
dealer = dealer_card1 + dealer_card2

def display(player, dealer):
    print(f"Player's cards: {player_card1}")
    print(f"Dealer's cards: {dealer_card1}")

    print(f"Player's cards: {player_card2}")
    print(f"Dealer's cards: {dealer_card2}")

    print(f"\nPlayer's total: {player}")
    print(f"Dealer's total: {dealer}")

display(player, dealer)

if player > 21 and dealer > 21:
    print("Both players bust! Dealer wins.")

elif player > 21:
    print("Player busts! Dealer wins.")

elif dealer > 21:
    print("Dealer busts! Player wins.")

elif player == 21 and dealer != 21:
    print("Player has blackjack! Player wins.")

elif dealer == 21 and player != 21:
    print("Dealer has blackjack! Dealer wins.")

elif player > dealer:
    print("Player wins!")

elif dealer > player:
    print("Dealer wins!")

else:
    print("It's a tie! Dealer wins.")
