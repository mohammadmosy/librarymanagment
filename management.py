import objects



def AddBook():
    new_book = objects.Book()
    BookName=input("enter Book name")
    if BookName=="":
        print("Book name is required")
        return False
    NumberOfBooks = input("enter Number of books: ")
    if NumberOfBooks=="":

        print("Number of books is required")

        return False

    IsAvailable = input("enter IsAvailable: ")

    if IsAvailable=="":

        print("IsAvailable is required")

        return False
    objects.books.Name=BookName
    objects.Books.Number=NumberOfBooks
    objects.Books.IsAvailable.IsAvailable


import json

import objects


def sign_up():
    name=input("enter your name:")
    password = input('enter Password: ')
    user_data = {"name": name, "password":password}
    
    json_object = json.dumps(user_data, indent=4)
    
    with open("sample.json", "a") as outfile:
        outfile.write(json_object+",\n")
    outfile.close()

import json

res = []
seen = set()

def add_entry(res, name, element, type):

    # check if in seen set
    if (name, element, type) in seen:
        return res

    # add to seen set
    seen.add(tuple([name, element, type]))

    # append to results list
    res.append({'name': name, 'element': element, 'type': type})

    return res

args = ['xyz', '4444', 'test2']

res = add_entry(res, *args)  # add entry - SUCCESS
res = add_entry(res, *args)  # try to add again - FAIL

args2 = ['wxy', '3241', 'test3']

res = add_entry(res, *args2)  # add another - SUCCESS






def sign_in():

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


 




