import main
import book
usere_pass={}

def register():
    Name=input("enter your name:")
    if Name=="":
        print("Name is required")
        return
    phone=input("enter your phone number")
    if phone=="":
        print("phone number is required")
        return
    if Name in usere_pass:
        print("username has already been registered")

    else:
        password = input('enter Password: ')
        if  password=="":
            print("password is required")
            return
    usere_pass[Name] = password,phone



def login():
    username = input("enter your username: ")
    if username=="":
        print("username is required")
        return False
    password = input("enter your password: ")
    if password=="":
        print("password is required")
        return False

    if usere_pass.get(username) == password:
        print(f"hello {username} ,you loged in successfully!")
        buyer_seller()
    else:
        print("wrong username or password!!")
    


def logout(username):
    if username in usere_pass:
        print(f"{username} loged out successfully")


 
def main_menu():
    while True:
        action = input("\n1. register\n2. log in\n3. log out\n4.  end\nchoose: ")
        match action:
            case'1':
                register()
                
            case'2':
                login()
                
            case'3':
                username = input("enter username: ")
                logout(username)
            case'4':
                print("end of program")
                break
