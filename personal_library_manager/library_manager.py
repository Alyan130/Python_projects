import json
from add_book import add_book
from remove_book import remove_book
from search_book import search
from display_books import display_books
from display_statistics import display_stats

books:list[dict]=[]

def read_data():
  try:
   with open("library.json","r") as file:
     return json.load(file)
  except:
    return []

def write_data():
  try:
   with open("library.json","w") as file:
      json.dump(books,file,indent=5)     
  except:
     print("Error saving data")

books=read_data()

while True:
 print(f'''
 Welcome to our personal library manager:
 1. Add a book  
 2. Remove a book  
 3. Search for a book  
 4. Display all books  
 5. Display statistics  
 6. Exit       
 ''')

 user_input:int=int(input("Enter your choice (1/6) : "))

 match user_input:
   case 1:
     book =  add_book()
     books.append(book)
     write_data()
     print("Book added to library successfully!")
   case 2:
     remove_book(books)
     write_data()
   case 3:
     search(books)
   case 4:
     display_books(books)
   case 5:
     display_stats(books)
   case 6:
     break 
   case _:
      print("Invalid choice please select from available books!")   
