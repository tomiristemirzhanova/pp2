import csv
from pathlib import Path

from connect import get_connection
from db_init import initialize_database


def import_from_csv(file_path: str):
    """Import contacts from CSV into the phonebook table."""
    query = """
    INSERT INTO phonebook (first_name, phone_number)
    VALUES (%s, %s)
    ON CONFLICT (phone_number)
    DO UPDATE SET first_name = EXCLUDED.first_name;
    """

    try:
        file = Path(file_path)
        if not file.exists():
            print(f"File not found: {file_path}")
            return

        imported_count = 0

        with get_connection() as conn:
            with conn.cursor() as cur:
                with open(file_path, mode="r", encoding="utf-8", newline="") as f:
                    reader = csv.DictReader(f)

                    required_columns = {"first_name", "phone_number"}
                    if not reader.fieldnames or not required_columns.issubset(set(reader.fieldnames)):
                        print("CSV must contain these headers: first_name, phone_number")
                        return

                    for row in reader:
                        name = (row.get("first_name") or "").strip()
                        phone = (row.get("phone_number") or "").strip()

                        if not name or not phone:
                            continue

                        cur.execute(query, (name, phone))
                        imported_count += 1

            conn.commit()
            print(f"Contacts imported successfully from CSV. Rows processed: {imported_count}")
    except Exception as e:
        print(f"Error importing from CSV: {e}")



def add_contact(name: str, phone: str):
    """Add a new contact manually."""
    query = """
    INSERT INTO phonebook (first_name, phone_number)
    VALUES (%s, %s)
    ON CONFLICT (phone_number)
    DO UPDATE SET first_name = EXCLUDED.first_name;
    """

    try:
        name = name.strip()
        phone = phone.strip()

        if not name or not phone:
            print("Name and phone number cannot be empty.")
            return

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (name, phone))
            conn.commit()

        print(f"Contact '{name}' added/updated successfully.")
    except Exception as e:
        print(f"Error adding contact: {e}")



def update_contact(name: str, new_phone: str):
    """Update a contact's phone number by name."""
    query = """
    UPDATE phonebook
    SET phone_number = %s
    WHERE first_name ILIKE %s;
    """

    try:
        name = name.strip()
        new_phone = new_phone.strip()

        if not name or not new_phone:
            print("Name and new phone number cannot be empty.")
            return

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (new_phone, name))

                if cur.rowcount == 0:
                    print(f"No contact found with the name '{name}'.")
                else:
                    print(f"Contact '{name}' updated successfully.")

            conn.commit()
    except Exception as e:
        print(f"Error updating contact: {e}")



def query_contacts(search_term: str):
    """Search contacts by name or phone prefix."""
    query = """
    SELECT id, first_name, phone_number
    FROM phonebook
    WHERE first_name ILIKE %s OR phone_number LIKE %s
    ORDER BY id;
    """

    try:
        search_term = search_term.strip()

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (f"%{search_term}%", f"{search_term}%"))
                results = cur.fetchall()

                if not results:
                    print("No contacts found matching the criteria.")
                else:
                    print("\n--- Search Results ---")
                    for contact in results:
                        print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]}")
    except Exception as e:
        print(f"Error querying contacts: {e}")



def delete_contact(identifier: str):
    """Delete a contact by name or phone number."""
    query = """
    DELETE FROM phonebook
    WHERE first_name ILIKE %s OR phone_number = %s;
    """

    try:
        identifier = identifier.strip()

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (identifier, identifier))

                if cur.rowcount == 0:
                    print(f"No contact found for '{identifier}'.")
                else:
                    print(f"Deleted {cur.rowcount} contact(s) successfully.")

            conn.commit()
    except Exception as e:
        print(f"Error deleting contact: {e}")



def show_all_contacts():
    """Display all contacts."""
    query = """
    SELECT id, first_name, phone_number
    FROM phonebook
    ORDER BY id;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()

                if not results:
                    print("Phonebook is empty.")
                else:
                    print("\n--- All Contacts ---")
                    for contact in results:
                        print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]}")
    except Exception as e:
        print(f"Error showing contacts: {e}")



def main_menu():
    """Main terminal interface."""
    initialize_database()

    while True:
        print("\n===== PhoneBook Application =====")
        print("1. Import contacts from CSV")
        print("2. Add new contact (Manual)")
        print("3. Update contact phone")
        print("4. Search contacts (Filter)")
        print("5. Delete contact")
        print("6. Show all contacts")
        print("7. Exit")

        choice = input("\nSelect an option (1-7): ").strip()

        if choice == "1":
            path = input("Enter CSV file path (e.g., contacts.csv): ").strip()
            import_from_csv(path)

        elif choice == "2":
            name = input("Enter first name: ").strip()
            phone = input("Enter phone number: ").strip()
            add_contact(name, phone)

        elif choice == "3":
            name = input("Enter the name of the contact to update: ").strip()
            new_phone = input("Enter the new phone number: ").strip()
            update_contact(name, new_phone)

        elif choice == "4":
            term = input("Enter search term (Name or Phone prefix): ").strip()
            query_contacts(term)

        elif choice == "5":
            target = input("Enter name or phone to delete: ").strip()
            delete_contact(target)

        elif choice == "6":
            show_all_contacts()

        elif choice == "7":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main_menu()