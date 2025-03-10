class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in self._contracts if contract.author == self]
    
    def books(self):
        return[contract.book for contract in Contract.all if contract.author ==self]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)

        return contract
    
    def total_royalties(self):
        total = 0
        for contract in self._contracts:
            total += contract.royalties
        return total



class Book:
    all = []

    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
          self.author = author
        else:
            raise Exception("Author must be an instance of Author")
        
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("Book must be an instance of Book")
        
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception("Date must be a string")
        
        if isinstance(royalties, int) or royalties < 0:
            self.royalties = royalties
        else:
            raise Exception("Royalties must be an integer")
        
        Contract.all.append(self)
        author._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    

