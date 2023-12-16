import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0    
    score = sum(cards)
    if score > 21 and 11 in cards:
        score -= 10
    return score

def determine_winner(player_score, computer_score):
    if player_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif player_score == 0:
        return "Win with a Blackjack"
    elif player_score > computer_score:
        return "You win"
    else:
        return "You lose"

def print_status(usercards, user_score, computercards, computer_score):
    print(f"\nYour cards: {usercards}, current score: {user_score}")
    print(f"Computer's first card: {computercards[0]}")
    print(f"Computer's cards: {computercards}, current score: {computer_score}")

def play_blackjack():
    usercards = [deal_cards() for _ in range(2)]
    computercards = [deal_cards() for _ in range(2)]

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(usercards)
        computer_score = calculate_score(computercards)

        print_status(usercards, user_score, computercards, computer_score)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_input = input("Do you want to draw another card or hold? ").lower()
            if user_input == "draw":
                usercards.append(deal_cards())
            elif user_input == "hold":
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computercards.append(deal_cards())
        computer_score = calculate_score(computercards)

    print_status(usercards, user_score, computercards, computer_score)
    print(determine_winner(user_score, computer_score))

play_blackjack()
