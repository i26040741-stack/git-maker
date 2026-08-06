import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    total = sum(hand)
    ace_count = hand.count(11)
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total

player_hand = []
dealer_hand = []

for _ in range(2):
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())


while True:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print(f"""Your hand: {player_hand}, 
          current score: {player_score}""")
    print(f"Dealer's first card: {dealer_hand[0]}") 
    if player_score == 21 and len(player_hand) == 2:
        print("Blackjack! You win!")
        break
    if player_score > 21:
        print("You went over 21. Dealer wins.")
        break
    answer = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if answer == 'y':
        player_hand.append(deal_card())
    elif answer == 'n':
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card())
        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
        if dealer_score > 21 or player_score > dealer_score:
            print("You win!")
        else:
            print("You lose!")
        break