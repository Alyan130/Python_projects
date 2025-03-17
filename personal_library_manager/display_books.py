
def display_books(books:list[dict]):
     print("Your library:")
     increament:int=0
     
     if len(books) > 0:
       for book in books:
             increament+=1
             print(f"{increament}. {book["title"]} by {book["author"]}  ({book["publication"]}) - {book["genre"]} - {book["read"]} ")
     
     else:
        print("No books available!")