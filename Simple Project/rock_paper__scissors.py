import random

def play():
    user = input ("'b' untuk batu, 'g' untuk gunting, 'k' untuk kertas: ")
    computer = random.choice(['b','g','k'])

    if user == computer:
        return 'Draw'
    
    if is_win(user, computer):
        return 'Kamu Kenang'

    return 'Kamu Kalah'

def is_win(pemain, lawan):
    #fungsi ini mengembalikan nilai jika user menang
    # b > g, g > k, k > b
    if(pemain == 'b' and lawan == 'g') or (pemain == 'g' and lawan == 'k') or (pemain == 'k' and lawan == 'b'):
        return True

print (play())