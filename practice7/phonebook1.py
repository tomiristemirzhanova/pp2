import csv
import psycopg2
from config1 import load_config


def get_connection():
    config = load_config()
    conn = psycopg2.connect(**config)
    conn.set_client_encoding('UTF8')
    return conn


def create_table():
    """Create the phonebook table if it does not exist."""
    query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    );
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
        print("Table created successfully.")
    except Exception as error:
        print("Create table error:", error)


def insert_from_csv(filename):
    """Insert contacts from a CSV file."""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                with open(filename, "r", encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        cur.execute(
                            """
                            INSERT INTO phonebook (name, phone)
                            VALUES (%s, %s)
                            ON CONFLICT (phone) DO NOTHING;
                            """,
                            (row["name"], row["phone"])
                        )
        print("CSV data inserted successfully.")
    except Exception as error:
        print("CSV insert error:", error)


def insert_from_console():
    """Insert one contact from user input."""
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s);",
                    (name, phone)
                )
        print("Contact inserted successfully.")
    except Exception as error:
        print("Console insert error:", error)


def show_all_contacts():
    """Display all contacts."""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, phone FROM phonebook ORDER BY id;")
                for row in cur:
                    print(row)
                rows = cur.fetchall()

                if rows:
                    print("\nContacts:")
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found.")
    except Exception as error:
        print("Show contacts error:", error)


def search_by_name():
    """Search contacts by name."""
    name = input("Enter name to search: ")
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, name, phone FROM phonebook WHERE name ILIKE %s;",
                    (f"%{name}%",)
                )
                rows = cur.fetchall()

                if rows:
                    print("\nSearch results:")
                    for row in rows:
                        print(row)
                else:
                    print("No matching contacts found.")
    except Exception as error:
        print("Search by name error:", error)


def search_by_phone_prefix():
    """Search contacts by phone prefix."""
    prefix = input("Enter phone prefix: ")
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, name, phone FROM phonebook WHERE phone LIKE %s;",
                    (f"{prefix}%",)
                )
                rows = cur.fetchall()

                if rows:
                    print("\nSearch results:")
                    
                else:
                    print("No matching contacts found.")
    except Exception as error:
        print("Search by phone prefix error:", error)


def update_contact():
    """Update a contact's name or phone number."""
    old_phone = input("Enter the phone number of the contact to update: ")
    print("1. Update name")
    print("2. Update phone")
    choice = input("Choose option: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if choice == "1":
                    new_name = input("Enter new name: ")
                    cur.execute(
                        "UPDATE phonebook SET name = %s WHERE phone = %s;",
                        (new_name, old_phone)
                    )
                elif choice == "2":
                    new_phone = input("Enter new phone: ")
                    cur.execute(
                        "UPDATE phonebook SET phone = %s WHERE phone = %s;",
                        (new_phone, old_phone)
                    )
                else:
                    print("Invalid choice.")
                    return

                if cur.rowcount > 0:
                    print("Contact updated successfully.")
                else:
                    print("No contact found with that phone.")
    except Exception as error:
        print("Update error:", error)


def delete_contact():
    """Delete a contact by name or phone."""
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose option: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if choice == "1":
                    name = input("Enter name to delete: ")
                    cur.execute("DELETE FROM phonebook WHERE name = %s;", (name,))
                elif choice == "2":
                    phone = input("Enter phone to delete: ")
                    cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
                else:
                    print("Invalid choice.")
                    return

                if cur.rowcount > 0:
                    print("Contact deleted successfully.")
                else:
                    print("No matching contact found.")
    except Exception as error:
        print("Delete error:", error)


def menu():
    """Console menu for the phonebook application."""
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Insert contacts from CSV")
        print("3. Insert contact from console")
        print("4. Show all contacts")
        print("5. Search by name")
        print("6. Search by phone prefix")
        print("7. Update contact")
        print("8. Delete contact")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv("contacts1.csv")
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            show_all_contacts()
        elif choice == "5":
            search_by_name()
        elif choice == "6":
            search_by_phone_prefix()
        elif choice == "7":
            update_contact()
        elif choice == "8":
            delete_contact()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()