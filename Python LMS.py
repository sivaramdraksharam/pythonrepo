import datetime
import os
os.getcwd()

class LMS:
    '''This class is used to keep record of books
    It has four modules: "Display books","Issue books","Return books","Add books"'''

    #constructor
    def __init__(self, list_of_books, library_name) :
        self.list_of_books = "C:\\Users\\Shivaram Prrasad\\Desktop\\pyproject\\List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101

        with open(self.list_of_books) as bk:
            content = bk.readlines()

        for line in content:
            #print(line)
            self.books_dict.update({str(Id): {"books_title":line.replace("\n",""),"lender_name":"","Issue_date":"","Status":"Available"}})

            Id = Id + 1

    def display_books(self):
        print("------------------List of Books-----------------")
        print("Books_ID","\t","Title")
        print("------------------------------------------------")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("Status"),"]")

    def issue_books(self):
        books_id = input("Enter books id:")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys:
            if not self.books_dict[books_id]["Status"] == "Available" :
                print( f"This books is already issued to {self.books_dict[books_id]['lender_name']}  on {self.books_dict[books_id]["Issue_date"]}")
                return self.issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                your_name=input("Enter your name:")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date']=current_date
                self.books_dict[books_id]['Status']="Already issued"
                print("Books issued successfully!!!\n")
            
        else:
            print("Book ID not found")
            return self.issue_books()
    def add_books(self):
        new_books = input("Enter books title:")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Books title length is too long!! Title length should be 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update(str(int(max(self.books_dict))+1) : {"books_title":new_books, "lender_name" : "","Issue_date":"","Status":"Available"})
                print(f"This books '{new_books}' has been added successfully!")
               # self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
               #                                  "lender_name":"","Issue_date":"","Status":"Available"}})
                

    def return_books(self):
        book_id = input("Enter book id:")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["Status"] == "Available":
                print("This book is already available in library. Please check your book ID")
                return return_books()
            elif not self.books_dict[book_id]["Status"] == "Available":
                self.books_dict[book_id]["lender_name"]=""
                self.books_dict[book_id]["Issue_date"]=""
                self.books_dict[book_id]["Status"]="Available"
                print("Successfully returned!")
        else:
            print("Book ID not found")

l = LMS("List_of_books.txt","Python's library")

print(l.display_books())
