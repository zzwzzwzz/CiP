def main():
    print("The Ancient Game of Nimm")
    print("There are 20 stones left")
    stone_number = 20
    player = 1
    remove_amount = 0
    while stone_number > 0:
        while True:
            try:
                remove_amount = int(input("Player " + str(player) + " Would you like to remove 1 or 2 stones? "))
                if remove_amount <= 2 and remove_amount >= 1:
                    break
                else:
                    print("Please enter 1 or 2.")
            except ValueError:
                print("Please enter 1 or 2.")
        
        stone_number = stone_number - remove_amount
        if stone_number > 0:
            print("There are " + str(stone_number) + " stones left")
        if player == 1:
            player = 2
        else:
            player = 1
    print("Player " + str(player) + " wins!")
    print("Game over")

if __name__ == '__main__':
    main()