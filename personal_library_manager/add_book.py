
def add_book():
  book_title:str = input("Enter the book title : ")
  author_name:str = input("Enter the author : ")
  publication_year:int = int(input("Enter the publication year : "))
  genre:str = input("Enter the genre : ")
  read_book:str = input("Have you read this book? (yes/no) : ")

  return {
     "title" : book_title,
     "author" : author_name,
     "publication" : publication_year,
     "genre" : genre,
     "read" : read_book,
  }