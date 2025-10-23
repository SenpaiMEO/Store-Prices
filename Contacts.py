# Define a dictionary with contact names and phone numbers
Contacts = {"Mahmoud": "01157482085","Saif": "01157482087","Ahmed": "01157482088"}
print(Contacts.items())

# Allow user to search by name
Search_Name = input("\nEnter a name to search: ")
Phone = Contacts.get(Search_Name, "Contact not found.")
print(f"{Search_Name}'s phone: {Phone}")