class User():
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.book={}
        
    def get_email(self):
        return self.email
    
    def change_email(self,new_email):
        self.email=new_email
        print("The user's email has been updated.")
        
    def __repr__(self):
        return("User "+self.name+", email "+self.email+", books read : "+str(len(self.book)))
    
    def __eq__(self,user):
        return self.email==user.email and self.name==user.name
    
    def read_book(self, book, rating=None):
        self.book[book]=rating
        
    def get_average_rating(self):
        values=[value for value in self.book.values() if value != None]
        return sum(values)/len(values)
    
        
class Book():
    def __init__(self,title,isbn):
        self.title=title
        self.isbn=isbn
        self.ratings=[]
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self,new_isbn):
        self.isbn=new_isbn
        print("The book's ISBN has been updated")
        
    def add_rating(self,rating):
        if rating==None:
            self.ratings.append(None)
        elif 0<=rating<=4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
            
    def __eq__(self,book):
        return self.title==book.title and self.isbn==book.isbn 
    
    def get_average_rating(self):
        ratings=[rating for rating in self.ratings if rating != None]
        return sum(ratings)/len(ratings)        
    
    def __hash__(self):
        return hash((self.title, self.isbn)) 
    
    
class Fiction(Book):
    def __init__(self, author, title, isbn):
        super(Fiction, self).__init__(title, isbn)
        self.author=author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return self.title+" by "+self.author
    
    
class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        super(Non_Fiction, self).__init__(title, isbn)
        self.subject=subject
        self.level=level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return self.title+", a "+self.level+" manual on "+self.subject
    
    
class TomeRater():
    def __init__(self):
        self.users={}
        self.books={}
        
    def create_book(self, title, isbn):
        return Book(title, isbn)
    
    def create_novel(self, title, author, isbn):
        return Fiction(author, title, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, isbn, subject, level)
    
    def add_book_to_user(self, book, email, rating=None):
        try:
            user=self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in list(self.books.keys()):
                self.books[book]+=1
            else:
                self.books[book]=1
        except KeyError:
            print("No user with email "+email+"!")
            
    def add_user(self, name, email, user_books=None):
        user=User(name, email)
        self.users[email]=user
        if user_books!=None:
            for book in user_books:
                self.add_book_to_user(book, email)
                
    def print_catalog(self):
        for book in list(self.books.keys()):
            print(book.title)
            
    def print_users(self):
        for user in list(self.users.keys()):
            print(user)
            
    def most_read_book(self):
        return list(self.books.keys())[list(self.books.values()).index(max(self.books.values()))]
    
    def highest_rated_book(self):
        first_book=list(self.books.keys())[0] if len(self.books)>=1 else "No books"
        max_rating=first_book.get_average_rating() if len(self.books)>=1 else "No books"
        for book in list(self.books.keys()):
            avg_rating=book.get_average_rating()
            if avg_rating >= max_rating:
                first_book=book
                max_rating=avg_rating
        return first_book
    
    def most_positive_user(self):
        first_user=list(self.users.values())[0] if len(self.users)>=1 else "No users"
        max_rating=first_user.get_average_rating() if len(self.users)>=1 else "No users"
        for user in list(self.users.values()):
            avg_rating=user.get_average_rating()
            if avg_rating >= max_rating:
                first_book=user
                max_rating=avg_rating
        return first_user
    
    def get_n_most_read_books(self, n):
        temp_books=self.books
        final_books=[]
        for ind in range(n):
            try:
                final_books.append(list(temp_books.keys())[list(temp_books.values()).index(max(temp_books.values()))])
                del temp_books[final_books[-1:][0]]
            except KeyError:
                print("Not enough books for this request, but here's all of the most read books:")
        if len(self.books)==0:
            print("No books for this request")
        else:
            for i in final_books:
                print(i.title)            
    
    def get_n_most_prolific_users(self, n):
        users=list(self.users.values())
        number_books=[len(i.book) for i in users]
        final_users=[]
        for i in range(n):
            try:
                max_book=max(number_books)
                final_users.append(users[number_books.index(max_book)])
                del users[users.index(final_users[-1:][0])]
                del number_books[number_books.index(max_book)]
            except ValueError:
                print("Not enough users for this request, but here's all of the most prolific users:")
        if len(self.users.values())==0:
            print("No users for this request")
        else:
            for i in final_users:
                print(i.name)            
        
        
            
            
        