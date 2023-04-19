import random

# Define a function to deal a card
def deal_card():
    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    return random.choice(cards)

# Define a function to calculate the value of a hand
def calculate_hand(hand):
    value = 0
    for card in hand:
        if card == "Ace":
            value += 11
        elif card in ["King", "Queen", "Jack"]:
            value += 10
        else:
            value += int(card)
    # Check if the hand contains an Ace and the value is over 21
    if "Ace" in hand and value > 21:
        value -= 10
    return value

# Define the main function
def play_game():
    print("Welcome to Blackjack!")
    # Initialize the deck
    deck = []
    for i in range(4):
        deck.extend(["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"])
    # Shuffle the deck
    random.shuffle(deck)
    # Deal the first two cards to the player
    player_hand = [deal_card(), deal_card()]
    # Deal the first two cards to the dealer
    dealer_hand = [deal_card(), deal_card()]
    # Print the initial hands
    print("Player's Hand:", player_hand)
    print("Dealer's Hand:", [dealer_hand[0], "X"])
    # Player's turn
    while True:
        player_value = calculate_hand(player_hand)
        if player_value == 21:
            print("Blackjack! You win!")
            return
        elif player_value > 21:
            print("Bust! You lose.")
            return
        else:
            action = input("Do you want to hit or stand? ").lower()
            if action == "hit":
                player_hand.append(deal_card())
                print("Player's Hand:", player_hand)
            elif action == "stand":
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")
    # Dealer's turn
    while True:
        dealer_value = calculate_hand(dealer_hand)
        if dealer_value >= 17:
            break
        else:
            dealer_hand.append(deal_card())
            print("Dealer's Hand:", [dealer_hand[0], "X"])
    # Determine the winner
    if dealer_value > 21:
        print("Dealer bust! You win!")
    elif dealer_value > player_value:
        print("Dealer's hand is higher. You lose.")
    elif dealer_value < player_value:
        print("Your hand is higher. You win!")
    else:
        print("It's a tie!")

# Call the main function to start the game
play_game()
