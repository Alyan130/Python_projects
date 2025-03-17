
def display_stats(books:list[dict]):
    read_percentage:list[dict]=[]
    print("Library Details:")

    if len(books) > 0:
      print(f"Total no of books : {len(books)} ")
     
      for book in books:
        if book["read"].lower()=="yes".lower():
          read_percentage.append(book)
    
      print(f"Book read percentage : {(len(read_percentage)*100)/len(books):.1f}%")
     
    else:
       print("No books available!")


