import random

def main_game():
    print("歡迎來玩十點半！")

    while True:
        print("\n發牌中...")
        dealer_cards, player_cards = [deal_card()], [deal_card()]

        while True:
            display_cards(dealer_cards, player_cards)
            continue_playing = ask_for_another_card()

            if continue_playing:
                drawn_card = deal_card()
                print(f"你抽到了: {drawn_card}")
                player_cards.append(drawn_card)
                if (len(player_cards) == 5 and calculate_points(player_cards) <= 10.5) or calculate_points(player_cards) == 10.5:
                    print("過五關，你贏了！")
                    break
                elif calculate_points(player_cards) > 10.5:
                    print("爆了！你輸了。")
                    break
            else:
                break

        if calculate_points(player_cards) <= 10.5:
            while calculate_points(dealer_cards) < 8.5 and len(dealer_cards) < 5:
                drawn_card = deal_card()
                print(f"莊家抽到了: {drawn_card}")
                dealer_cards.append(drawn_card)

        display_cards(dealer_cards, player_cards)

        dealer_points = calculate_points(dealer_cards)
        player_points = calculate_points(player_cards)

        determine_winner(dealer_points, player_points)
        play_again = input("要再玩一次嗎？ (是/否): ").lower()
        if play_again != '是':
            break
def ask_for_another_card():
    while True:
        continue_playing = input("是否要繼續拿牌? (是/否): ").lower()
        if continue_playing in ['是', '否']:
            return continue_playing == '是'
        else:
            print("請輸入是或否。")
def deal_card():
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0.5, 0.5, 0.5])
def display_cards(dealer_cards, player_cards):
    print(f"\n莊家的牌: {', '.join(map(str, dealer_cards))}")
    print(f"你的牌:  {', '.join(map(str, player_cards))}")
def calculate_points(cards):
    points = sum(cards)
    return points
def determine_winner(dealer_points, player_points):
    print(f"\n莊家點數: {dealer_points}")
    print(f"你的點數: {player_points}")
    if player_points > 10.5:
        print("爆了！你輸了。")
    elif dealer_points > 10.5:
        print("莊家爆了！你贏了。")
    elif player_points > dealer_points:
        print("你贏了！")
    elif player_points < dealer_points:
        print("你輸了。")
    else:
        print("和局.")
if __name__ == "__main__":
    main_game()
