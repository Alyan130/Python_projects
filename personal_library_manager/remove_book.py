
def remove_book(books:list[dict]):
    book_removed = False
    remove = input("Enter the title of the book to remove : ") 
    for book in books:
      if (book["title"].lower()==remove.lower()):
         books.remove(book)
         print("Book removed from library successfully!")
         found=True
         break
    if found == False:
         print("Book not found!")
