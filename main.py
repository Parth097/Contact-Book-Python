from contact_book import ContactBook
from contact_book_interface import ContactBookInterface

def main():
  contact_book = ContactBook()
  contact_book_interface = ContactBookInterface(contact_book)
  contact_book_interface.run()
  
if __name__ == "__main__":
  main()