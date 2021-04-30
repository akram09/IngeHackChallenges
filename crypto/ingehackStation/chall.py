import random 
import ecdsa
import hashlib
from Crypto.Util.number import inverse
BITS_LENGTH = 16
MOD = 2**9
# make it a dict a key and description 
games = ["batman", "gtaiv", "uncharted", "flag"]
def generate_random():
    r = random.randint(2**BITS_LENGTH,2**(BITS_LENGTH+1))
    return r+2**BITS_LENGTH  % MOD 
def print_intro():
    print("==================   IngeHack Station  ===================")
    print("Welcome to our Ingehack Station where you can play different games ")
    # TODO to be redacted 
def print_menu():
    print("You can choose one of the games to play with ")
    for i, game in enumerate(games):
        print(" {} - {}".format(i,game))

def play_game(game_number, G,priv,n):
    # flag game 
    if game_number == 3:
        print("To play this game you need to give us the private key ")
        m1 = input("Enter your password: ").encode()
        h1 = int(hashlib.sha256(m1).hexdigest(),16)
        done = False
        while not done:
            k = generate_random()
            P = k1*G
            r = P.x()%n
            if r == 0:
                continue
            s = inverse(k1,n)*(h1+r*priv)%n
            if s == 0:
                continue
            done = True
        print("Here is the signature of your password r = {} , s =  {}".format(r,s))
        print("Please input the private key: ")
        priv_inp = int(input())
        if priv_inp == inp:
            # print flag 
            print(open("games/flag.txt",'r').read().decode())
    # TODO here add other games to be read 


def main():
    print_intro()
    curve = ecdsa.NIST256p
    G = curve.generator
    n = curve.order
    # private key 
    session_key = random.randint(1,n-1)
    Q = G*session_key
    print((Q.x, Q.y))
    while True:
        print_menu()
        game_number = int(input())
        if game_number>0 and game_number<len(games):
            play_game(game_number,G,session_key,n)
        else:
            exit(1)





if __name__ == '__main__':
    
    main()