
def search(books):
    print("Search by:\n1.Title\n2.Author")
    search_by:int = int(input("Enter your choice : "))
    found:bool=False

    if search_by == 1:
        book_title=input("Enter book title : ")
        for book in books:
            if book["title"].lower() == book_title.lower():
                print(f"{book["title"]} by {book["author"]}  ({book["publication"]}) - {book["genre"]} - {book["read"]} ")
                found=True
                break
        if found == False:
              print("Book not find!")

    elif search_by == 2:
        book_title=input("Enter book author : ")
        for book in books:
            if book["author"].lower() == book_title.lower():
                print(f"{book["title"]} by {book["author"]}  ({book["publication"]}) - {book["genre"]} - {book["read"]} ")
                found=True
                break
        if found == False:
              print("Book not find!")

     
    else:
        print("Invalid choice please select valid options!")