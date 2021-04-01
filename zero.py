import random

player_score = 0
computer_score = 0
turn = 0

while player_score < 5 and computer_score < 5:
    player_bet = 0
    player_target = 0
    computer_bet = 0
    computer_target = 0

    computer_bet = random.randint(0,2)
    computer_target = random.randint(0,4)


    if turn == 0:
        player_target = int(input("목표 숫자(0~4)를 입력하세요:"))
        player_bet = int(input("배팅 값(0~2)을 입력하세요:"))
        temp = player_bet + computer_bet
        if temp == player_target:
            player_score = player_score + 1
            print("점수를 획득하셨습니다. 당신의 점수는", player_score, "점, 컴퓨터의 점수는", computer_score, "점입니다.")
            print("컴퓨터는", computer_bet, "을(를) 배팅했습니다.")
        else:
            print("점수를 획득하지 못하셨습니다. 당신의 점수는", player_score, "점, 컴퓨터의 점수는", computer_score, "점입니다.")
            print("컴퓨터는", computer_bet, "을(를) 입력했습니다.")
        turn = turn + 1

    else:
        player_bet = int(input("배팅 값(0~2)을 입력하세요:"))
        temp = player_bet + computer_bet
        if temp == computer_target:
            computer_score = computer_score + 1
            print("컴퓨터가 점수를 획득했습니다. 당신의 점수는", player_score, "점, 컴퓨터의 점수는", computer_score, "점입니다.")
            print("컴퓨터는", computer_bet, "을(를) 배팅했으며", computer_target, "을(를) 목표로 설정했습니다.")
        else:
            print("컴퓨터가 점수를 획득하지 못했습니다. 당신의 점수는", player_score, "점, 컴퓨터의 점수는", computer_score, "점입니다.")
            print("컴퓨터는", computer_bet, "을(를) 배팅했으며", computer_target, "을(를) 목표로 설정했습니다.")
        turn = turn - 1


if player_score == 5:
    print("승리하셨습니다! 당신의 점수는", player_score, "점, 컴퓨터의 점수는", computer_score, "점입니다.")
else:
    print("패배하셨습니다. 당신의 점수는", player_score, "점, 컴퓨터의 점수는", computer_score, "점입니다.")