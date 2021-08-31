import pickle


class contacts():

    contact_ID = 0

    def __init__(self, contact_ID, first_name, last_name, email):
        contacts.contact_ID += 1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_contact(self):
        return (self.first_name, self.last_name, self.email)



def print_list(something):
    if len(something) > 0:
        fs = "%-15s %-15s %-15s"        
        print(fs % ('First name', 'Last name', 'Email'))

        for i in something:
            print (fs % i.get_contact())

    else:
        print("No contacts added yet.")


def add_contact():
    self = "self"
    first_name = input("Enter contact's first name: ")
    last_name = input("Enter contact's last name: ")
    email = input("Enter contact's email: ")
    contact_instance = contacts(self, first_name, last_name, email)
    return contact_instance





def main():

    mycontacts = []

    try:
        f = open("contacts.txt", "rb")     # open binary read mode
        mycontacts = pickle.load(f)
        f.close()
    except EOFError:
        pass
    

    while True:
        
        print("""
        SUPER FUN CONTACTS PROGRAM - OPTIONS MENU
        1.) Display all contacts
        2.) Create new contact
        3.) Clear all contacts
        4.) Save and exit
        """)

        option = input("Enter 1, 2, 3 or 4: ")

        if option == "1":
            print_list(mycontacts);

        elif option == "2":
            contact = add_contact()
            mycontacts.append(contact)

        elif option == "3":
            mycontacts = []

        elif option == "4":
            f = open("contacts.txt", "wb")    
            pickle.dump(mycontacts, f)              
            f.close()
            print("Have a nice day. Good bye =)")
            break

        else:
            print("Invalid entry.")


if __name__ == '__main__':
    main()



