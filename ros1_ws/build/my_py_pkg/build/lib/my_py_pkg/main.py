from game import *
import time
cont = '1'

while(cont == '1'):
    P1 = player("Player 1")
    P2 = player("Player 2")
    print("\nGame started\n")
    for i in range(4):
        P1.RPS_num = RPS.random_num()
        P2.RPS_num = RPS.random_num()
        print(f"Round {i}\n")
        str = "Player 1 is " + game_system.get_name(P1.RPS_num)
        print(str)
        str = "Player 2 is " + game_system.get_name(P2.RPS_num)
        print(str + "\n")
        check = RPS.win(P1.RPS_num, P2.RPS_num)
        game_system.add_score(check, P1, P2)
        if check == 1:
            print("Player 1 won the round!\n")
        if check == -1:
            print("Player 2 won the round!\n")
        if check == 0:
            print("Draw!\n")
        print(f"Player 1 score: {P1.score}")
        print(f"Player 2 score: {P2.score}\n")
        time.sleep(1)
    if P1.score >  P2.score:
        print("Player 1 won the game!\n")
    elif P1.score <  P2.score:
        print("Player 2 won the game!\n")
    else:
        print("Draw!\n")
    print("Game ended!\n")
    print("Do you wish to play another game\n")
    print("1) Yes")
    print("2) No\n")
    cont = input("Enter: ")