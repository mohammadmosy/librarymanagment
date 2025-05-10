import json
books={}

listMember= ["mohammad",'hadi','arman']

class Book:
    """
     
    """
    def __init__(self,name , numbers,IsAvailable):
        self.name=name
        self.numbers=numbers
        self.IsAvailable=IsAvailable
        books[name]=numbers,IsAvailable


class Members:
    def __init__(self,Name,PhonNumber):
        self.Name=Name 
        self.PhonNumber=PhonNumber
        """self.LoanedBooks=LoanedBooks"""
        listMember.append(Name)
        listMember.append(PhonNumber)
        """listMember.append(LoanedBooks)"""
        print(listMember)

class ManagementSystem:
    pass

"""res=Members("mohammad","123456789","book")"""


with open('memmbers.json','w') as f:
    json.dump(listMember,f)