'''Brainstorming
    T -> number of testcases, range(1,10)
        integer G -> at first line of each T, range(1, 2000)
            I N Q -> at the first line of each G
    integer I(initial state of coins, 1(guess number of heads at the end) or 2(guess number of tails at the end)) 
    integer N(number of coins and rounds), range(1, 109)
    integer Q(1(guess number of heads at the end) or 2(guess number of tails at the end))
'''
def q_is(Q):
    ''' number of head or tail, arg head or tail'''
    if (int(Q) == 1):
        print(1)
    elif (int(Q) == 2):
        print(2)
    else:
        exit()

def flip_coin():
    ''' flip the coin for each rounds'''
    print('WIP')

T = int(input())
if T>=1 and T<=10:
    for test in range(T):
        G = int(input())
        if G>=1 and G<=2000:
            for game in range(G):
                I, N, Q = input().strip().split()
                if (int(I) == 1):
                    pass
                elif (int(I) == 2):
                    pass
                else:
                    exit()
                if int(N)>=1 and int(N)<=109:
                    for rounds in range(int(N)):
                        flip_coin()
                else:
                    break
                if (int(Q) == 1):
                    print(q_is(Q))
                elif (int(Q) == 2):
                    print(q_is(Q))
                else:
                    exit()
        else:
            exit()
else:
    exit()