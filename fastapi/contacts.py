import uuid

# Initial list of contacts
contacts = [
    {"id": "562915f6-e46c-455b-a18c-fe982f709f7e", "name": "Anicka", "discord": "anka.01"},
    {"id": "38ab581d-c729-423c-bbce-1157196d3f3d", "name": "Štefan", "discord": "stef.07"},
]

def add_contact(name: str, discord: str):
    """Adds a new contact with a unique UUID."""
    new_contact = {
        "id": str(uuid.uuid4()),  # Generate a new unique ID
        "name": name,
        "discord": discord
    }
    contacts.append(new_contact)
    return new_contact  # Return the newly created contact

def find_contact(contact_id: str):
    """Finds a contact by its ID."""
    for contact in contacts:
        if contact["id"] == contact_id:
            return contact
    raise ValueError("No contact with given id.")

def all_contacts():
    """Returns a list of all contacts."""
    return contacts

def update_contact(contact_id, name=None, discord=None):
    """Updates a contact's name and/or discord username."""
    for contact in contacts:
        if contact["id"] == contact_id:
            if name:
                contact["name"] = name
            if discord:
                contact["discord"] = discord
            return contact  # Return updated contact
    raise ValueError("No contact with given id.")

def delete_contact(contact_id):
    """Deletes a contact by its ID."""
    for index,contact in enumerate(contacts):
        if contact["id"] == contact_id:
            contacts.pop(index)
            return
    raise ValueError("No contact with given id.")
