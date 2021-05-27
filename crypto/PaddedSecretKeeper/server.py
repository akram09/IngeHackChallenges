

def menu():
    print("Please You need to authenticate yourself in order to access secrets")
    print("Select one of the following: ")
    print("1) Register a new account ")
    print("2) Login with your token")



def main():
    print("Welcome To Our Secret Keeper")
    print("Our special secret keeper use padding as a source of security. we do believe padding solves a lot of security issues. And we are planning to pad more : ) ")
    while True:
        menu()
        dz=55
        choice = input("")
        print(choice)


if __name__ == "__main__":
    main()