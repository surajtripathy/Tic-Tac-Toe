#Works for n size board
import itertools
import sys
def blank_board(n):
    a = "  --"
    b = " |  "
    for i in range(n):
        print(a*n)
        print(b*(n+1))
        print(a*n)

#Taking input the size of the baord
size = 0
while True:
    try:
        size = int(input("Please enter the size of the tic tac toe (Expected greater than two) "))
        if size > 2:
            break
        else:
            print("Please enter a value more than two")
    except ValueError:
        print("Please enter a valid size")
    except KeyboardInterrupt:
        print("\nGame Terminated")
        sys.exit()
print("Creating tic tac toe for "+ str(size) + "x" + str(size))
blank_board(size)
one_pos = []
zero_pos = []
count_pos = 0

list_row = []
list_col =[]
d1 = []
d2 = []

#Storing all the win conditions in lists
#IF WIN CONDITION IN ROWS
for i in range(size):
    list_temp = list(range(i*size,(i+1)*size))
    list_row.append(list_temp)

#IF WIN CONDITION IN COLS
list_temp = list(range(size))
for x in range(size):
    list_temp_2 = []
    for i in range(size):
        var = list_temp[x] + i*size
        list_temp_2.append(var)
    list_col.append(list_temp_2)

#IF WIN CONDITION IS DIAGONALS
list_temp = list(range(size))
for x in range(size):
    var1 = list_temp[x] + x*size
    var2 = list_temp[size-x-1] + x*size
    d1.append(var1)
    d2.append(var2)

#Take single input from player and find all the possible combinations
#Check if combination is matched with win_conditions, if yes break, if no continue taking input
#If input more than size*size then the game gets tied
def who_wins():
    #ALL COMBINATIONS OF X_POS
    x_pos_list = [[0]]
    for i in range(len(one_pos) - size + 1):
        temp_list = []
        for l in itertools.combinations(one_pos, size):
            x_pos_list.append(list(l))
    #print(x_pos_list)
    #ALL COMBINATIONS OF ZERO_POS
    zero_pos_list = [[0]]
    for i in range(len(zero_pos) - size + 1):
        temp_list = []
        for l in itertools.combinations(zero_pos, size):
            zero_pos_list.append(list(l))
    #print(zero_pos_list)
    set_x_win = False
    set_0_win = False
    #CHECK WHO WINS
    i = 0
    while True:
        try:
            if x_pos_list[i] == d1 or x_pos_list[i] == d2:
                set_x_win = True
                break
            if zero_pos_list[i] == d1 or zero_pos_list[i] == d2:
                set_0_win = True
                break
        except IndexError:
            print("",end="")
        i = i + 1
        if(i == max(len(x_pos_list),len(zero_pos_list))):
            break


    if set_x_win == False and set_0_win == False:
        for i in x_pos_list:
            for j in list_row:
                if i == j:
                    set_x_win = True
                    break
            if set_x_win == True:
                break
            for j in list_col:
                if i == j:
                    set_x_win = True
                    break
            if set_x_win == True:
                break

        for i in zero_pos_list:
            for j in list_row:
                if i == j:
                    set_0_win = True
                    break
            if set_0_win == True:
                break
            for j in list_col:
                if i == j:
                    set_0_win = True
                    break
            if set_0_win == True:
                break

    if set_x_win == True and set_0_win == False:
        print("Winner winner chicken dinner, player 'X' wins")
        return True
    if set_0_win == True and set_x_win == False:
        print("Winner winner chicken dinner, player '0' wins")
        return True


#TAKING INPUT FROM X_USER AND 0_USER
check_tie = True
x_repeated = False
o_repeated = False
while True:
    while True:
        if o_repeated == True:
            break
        try:
            one = int(input("Please enter the position of X from 1-" + str(size*size)+ " ")) - 1
            if (one+1) > (size*size) :
                print("Please enter valid input")
            else:
                break
        except ValueError:
            print("Please enter valid input")
        except KeyboardInterrupt:                     #To terminate when Ctrl+C
            print("\nGame Terminated")
            sys.exit()
    dup = 0
    try:
        zero_pos.index(one)
        check_tie = False
    except ValueError:
        dup += 1
    try:
        one_pos.index(one)
        check_tie = False
    except ValueError:
        dup +=1
        if dup !=2:
            print("Please enter a valid position")
            x_repeated = True
        if dup == 2:
            x_repeated = False
            one_pos.append(one)
            one_pos.sort()
            count_pos +=1
            check_win = who_wins()
        if check_win == True:
            check_tie = False
            break
        if count_pos == (size*size):
            check_tie = True
            break

    while True:
        if x_repeated == True:
            break
        try:
            zero = int(input("Please enter the position of 0 from 1-" + str(size*size)+ " ")) - 1
            if (zero+1) > (size*size)  :
                print("Please enter valid input")
            else:
                break
        except ValueError:
            print("Please enter valid input")
        except KeyboardInterrupt:                     #To terminate when Ctrl+C
            print("\nGame Terminated")
            sys.exit()
    dup = 0
    try:
        one_pos.index(zero)
        check_tie = False
    except ValueError:
        dup += 1
    try:
        zero_pos.index(zero)
        check_tie = False
    except ValueError:
        dup += 1
        if dup !=2:
            print("Please enter a valid position")
            o_repeated = True
        if dup == 2:
            o_repeated = False
            zero_pos.append(zero)
            zero_pos.sort()
            count_pos +=1
            check_win = who_wins()
        if check_win == True:
            check_tie = False
            break
        if count_pos == (size*size):
            check_tie = True
            break
if check_tie == True:
    print("Game tied!!! Nobody gets chicken dinner!!! Please play again!!!")
