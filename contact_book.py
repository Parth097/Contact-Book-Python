import sqlite3

class ContactBook:

  def __init__(self):
    self.conn = sqlite3.connect('contacts.db')
    self.c = self.conn.cursor()
    self.create_table()

  def create_table(self):
    self.c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        phone TEXT,
                        email TEXT,
                        address TEXT
                   )''')
    self.conn.commit()

  def add_contact(self, name, phone, email, address):
    self.c.execute('''INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)''', (name, phone, email, address))
    self.conn.commit()
    
  def update_contact(self, name, phone, email, address):
    self.c.execute('''UPDATE contacts SET phone=?, email=?, address=? WHERE name =? ''', (name, phone, email, address))
    self.conn.commit()
    
  def delete_contact(self, name):
    self.c.execute('''DELETE FROM contacts WHERE name=?''',(name,))
    self.conn.commit()
    
  def search_contact_by_name(self, name):
    self.c.execute('''SELECT * FROM contacts WHERE name LIKE ?''', ('%'+name+'%',))
    contacts = self.c.fetchall()
    return contacts
  
  def __del__(self):
    self.conn.close()