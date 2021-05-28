import base64  
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import  bytes_to_long,long_to_bytes



# todo This must be redacted !!!
SECRET_PADDING = bytes_to_long(os.urandom(4))
print(SECRET_PADDING)
iv = os.urandom(16)
key = os.urandom(32)



def make_token(username,type,padding):
    data = {
        "type":type,
        "username":username,
        "padding":str(padding)
    }   
    data_json ="{"+ ";".join([ key+':'+val  for key,val in data.items()])+ "}"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(data_json.encode(), 16))
    token= base64.b64encode(ct)
    return token
    


def menu():
    print("Select one of the following: ")
    print("1) Register a new account ")
    print("2) Login with your token")

def register():
    print("Please Submit your Username")
    username = input()
    token = make_token(username,"user", SECRET_PADDING).decode("utf-8")
    return token



def login():
    print("Hello There, welcome back !")
    print("To get your secret you need to log in using your token")
    token_enc  = base64.b64decode(input())
    cipher = AES.new(key, AES.MODE_CBC, iv)
    token_padded  = cipher.decrypt(token_enc)
    try:
        token_unpadded = unpad(token_padded)
    except ValueError:
        print("Incorrect Padding :- _ - ")
    token = token_unpadded.replace("{","").replace("}","")
    padding = 0
    type ="user"
    for block in token.split(";"):
        key,value= block.split(":")
        if key=="padding":
            padding = int(value)
        elif key=="type":
            type = value
    if type=="root" and padding==SECRET_PADDING:
        flag = open("flag.txt").read()
        print("Here is your secret keep it warm : ) ")
        # a security concern : ) 
        print(bytes_to_long(flag.encode("utf-8"))*13337 % SECRET_PADDING)
    else:
        print("Here is your secret keep it warm : ) ")
        print("I love IngeHack :!")


def main():
    print("Welcome To Our Secret Keeper")
    print("Our special secret keeper use padding as a source of security. we do believe padding solves a lot of security issues. And we are planning to pad more : ) ")
    print("Please You need to authenticate yourself in order to access secrets")
    while True:
        menu()
        choice = int(input(""))
        assert choice in [1,2]
        if choice == 1:
            token = register()
            print(f"Welcome to the club here is your token {token}")
        elif choice == 2:
            login()




if __name__ == "__main__":
    main()