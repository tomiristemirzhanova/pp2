import psycopg2
from config import load_config


def get_connection():
    config = load_config()
    return psycopg2.connect(**config)


def search_by_pattern():
    pattern = input("Enter search pattern: ")
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", (pattern,))
                rows = cur.fetchall()

                if rows:
                    print("\nMatched contacts:")
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found.")
    except Exception as error:
        print("Search function error:", error)


def upsert_one_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
        print("Upsert completed successfully.")
    except Exception as error:
        print("Upsert procedure error:", error)


def insert_many_contacts():
    try:
        count = int(input("How many contacts do you want to insert? "))
        names = []
        phones = []

        for _ in range(count):
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            names.append(name)
            phones.append(phone)

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))
        print("Bulk insert procedure completed.")
    except Exception as error:
        print("Bulk insert error:", error)


def show_paginated_contacts():
    try:
        limit = int(input("Enter LIMIT: "))
        offset = int(input("Enter OFFSET: "))

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
                rows = cur.fetchall()

                if rows:
                    print("\nPaginated contacts:")
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found.")
    except Exception as error:
        print("Pagination function error:", error)


def delete_by_name_or_phone():
    value = input("Enter username or phone to delete: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact(%s);", (value,))
        print("Delete procedure completed.")
    except Exception as error:
        print("Delete procedure error:", error)


def menu():
    while True:
        print("\n--- PHONEBOOK MENU (FUNCTIONS & PROCEDURES) ---")
        print("1. Search contacts by pattern")
        print("2. Upsert one contact")
        print("3. Insert many contacts")
        print("4. Show contacts with pagination")
        print("5. Delete by username or phone")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_by_pattern()
        elif choice == "2":
            upsert_one_contact()
        elif choice == "3":
            insert_many_contacts()
        elif choice == "4":
            show_paginated_contacts()
        elif choice == "5":
            delete_by_name_or_phone()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()