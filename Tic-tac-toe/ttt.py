from tabulate import tabulate
import sys

table = [[None,None,None],
         [None,None,None],
         [None,None,None]]

def print_board():
    print(tabulate(table, tablefmt = "rounded_grid"))


def get_input(turn):
    while True:
        try:
            n = int(input(f"Enter the square number (1-9) for Player {turn}: "))
            if n not in range(1, 10):
                raise ValueError("Number out of range!")
            return n
        except ValueError as e:
            print(f"Invalid Input: {e}")


def update_table(turn):
    print_board()
    while True:
        n = get_input(turn)
        i, j = (n - 1) // 3, (n - 1) % 3
        if table[i][j] is None:
            table[i][j] = turn
            return
        else:
            print("The square is already used!")
        
    
def win_check():
    if table[0][0] == table[0][1] == table[0][2] != None:
        return True
    if table[1][0] == table[1][1] == table[1][2] != None:
        return True
    if table[2][0] == table[2][1] == table[2][2] != None:
        return True
    if table[0][0] == table[1][0] == table[2][0] != None:
        return True
    if table[0][1] == table[1][1] == table[2][1] != None:
        return True
    if table[0][2] == table[1][2] == table[2][2] != None:
        return True
    if table[0][0] == table[1][1] == table[2][2] != None:
        return True
    if table[0][2] == table[1][1] == table[2][0] != None:
        return True
    if is_board_full():
        print_board()
        sys.exit("No any winner!")
    return False

def is_board_full():
    for i in range(0,3):
        for j in range(0,3):
            if table[i][j] == None:
                return False
    return True

def main():
    i = 0
    while not win_check():
        i += 1
        if i % 2 == 1:
            turn = "O"
        else:
            turn = "X"
        update_table(turn)
    print_board()
    print(f"Player {turn} won!")


if __name__ == "__main__":
    main()