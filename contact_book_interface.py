class ContactBookInterface:
  
  def __init__(self, contact_book):
    self.contact_book = contact_book
    
  def display_menu(self):
    print("\nContact Book Menu:\n")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact By Name")
    print("5. Exit")
    
  def add_contact(self):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    self.contact_book.add_contact(name, phone, email, address)
    print("Contact added successfully")
    
  def update_contact(self):
    name = input("Enter name of contact to update: ")
    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")
    address = input("Enter new address: ")
    self.contact_book.update_contact(name, phone, email, address)
    print("Contact updated successfully")
    
  def delete_contact(self):
    name = input("Enter name of contact to delete: ")
    self.contact_book.delete_contact(name)
    print("Contact deleted")
  
  def search_contac_by_name(self):
    name = input("Enter name to search: ")
    contacts = self.contact_book.search_contact_by_name(name)
    if contacts:
      print("Search Results:")
      for contact in contacts:
        print(contact)
    else:
      print("No contacts found with that name")
  
  def run(self):
    while True:
      self.display_menu()
      choice = input("Enter your choice: ")
      if choice == '1':
        self.add_contact()
      elif choice == '2':
        self.update_contact()
      elif choice == '3':
        self.delete_contact()
      elif choice == '4':
        self.search_contac_by_name()
      elif choice == '5':
        print("Exiting...")
        break
      else:
        print("Invalid choice, please try again.")
  


    
