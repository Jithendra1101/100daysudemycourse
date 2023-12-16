import random

class BlackjackGame:
    def __init__(self):
        self.deck = self.initialize_deck()
        self.player_hand = []
        self.dealer_hand = []

    def initialize_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop()

    def calculate_score(self, hand):
        score = sum(self.card_value(card) for card in hand)
        if score > 21 and 'A' in hand:
            # Adjust for the presence of Ace(s)
            while score > 21 and 'A' in hand:
                score -= 10
                hand.remove('A')
        return score

    def card_value(self, card):
        if card['rank'] in ['K', 'Q', 'J']:
            return 10
        elif card['rank'] == 'A':
            return 11  # Ace can be 1 or 11; default to 11 and adjust later if needed
        else:
            return int(card['rank'])

    def display_hand(self, hand):
        return ', '.join([f"{card['rank']} of {card['suit']}" for card in hand])

    def start_game(self):
        for _ in range(2):
            self.player_hand.append(self.deal_card())
            self.dealer_hand.append(self.deal_card())

        self.play_round()

    def play_round(self):
        while True:
            print(f"\nYour cards: {self.display_hand(self.player_hand)}")
            print(f"Your current score: {self.calculate_score(self.player_hand)}")
            print(f"Dealer's first card: {self.dealer_hand[0]['rank']} of {self.dealer_hand[0]['suit']}")

            if self.calculate_score(self.player_hand) == 21:
                print("Blackjack! You win!")
                break
            elif self.calculate_score(self.player_hand) > 21:
                print("Busted! You went over 21. You lose.")
                break

            action = input("Type 'hit' to get another card, or 'stand' to pass: ").lower()

            if action == 'hit':
                self.player_hand.append(self.deal_card())
            elif action == 'stand':
                self.play_dealer_turn()
                break

    def play_dealer_turn(self):
        while self.calculate_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())

        print(f"\nYour final hand: {self.display_hand(self.player_hand)}")
        print(f"Your final score: {self.calculate_score(self.player_hand)}")
        print(f"\nDealer's final hand: {self.display_hand(self.dealer_hand)}")
        print(f"Dealer's final score: {self.calculate_score(self.dealer_hand)}")

        self.determine_winner()

    def determine_winner(self):
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)

        if player_score > 21:
            print("Busted! You went over 21. You lose.")
        elif dealer_score > 21:
            print("Dealer busted! You win!")
        elif player_score == dealer_score:
            print("It's a draw!")
        elif player_score == 21:
            print("Blackjack! You win!")
        elif dealer_score == 21:
            print("Dealer got a Blackjack. You lose.")
        elif player_score > dealer_score:
            print("You win!")
        else:
            print("You lose.")

if __name__ == "__main__":
    game = BlackjackGame()
    game.start_game()
