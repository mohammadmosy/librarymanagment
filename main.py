import management
import objects

def main():
    menu=input("1.member\n,2.management\nchoice>:")
    match menu:
        case"1":
            management.main()
        case "2":
            object.main()


if __name__ == "__main__":
    main()


# TODO Registration
# TODO when the user signs up, their username and password should be added to members.json
# TODO when the user wants to sign in, their username and password must be checked


