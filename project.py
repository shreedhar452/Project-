import uuid
import time

def generate_unique_id():
    return str(uuid.uuid4())

def current_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def save_to_database(change_request):
    # Placeholder for saving to a database
    print("Change request saved:", change_request)

def create_change_request(description):
    request_id = generate_unique_id()

    change_request = {
        "request_id": request_id,
        "description": description,
        "status": "pending",
        "created_at": current_timestamp(),
        "updated_at": current_timestamp()
    }

    save_to_database(change_request)
    
    return change_request

def display_menu():
    print("\nChange Request Menu:")
    print("1. Create Change Request")
    print("2. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter the change request description: ")
            request = create_change_request(description)
            print("Change Request Created:", request)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if _name_ == "_main_":
    main()
