import main


def AddBook():
    new_book = main.Book()
    
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
    main.books.Name=BookName
    main.Books.Number=NumberOfBooks
    main.Books.IsAvailable.IsAvailable




