import json

# File to store data
FILE_NAME = "health_data.json"

# Load existing data
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add new patient
def add_patient(data):
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    data[patient_id] = {
        "name": name,
        "age": age,
        "records": []
    }

    print("Patient added successfully!")

# Add health record
def add_record(data):
    patient_id = input("Enter Patient ID: ")

    if patient_id not in data:
        print("Patient not found!")
        return

    bp = input("Enter Blood Pressure: ")
    sugar = input("Enter Sugar Level: ")
    weight = input("Enter Weight: ")

    record = {
        "bp": bp,
        "sugar": sugar,
        "weight": weight
    }

    data[patient_id]["records"].append(record)
    print("Record added successfully!")

# View patient data
def view_patient(data):
    patient_id = input("Enter Patient ID: ")

    if patient_id not in data:
        print("Patient not found!")
        return

    print("\n--- Patient Details ---")
    print("Name:", data[patient_id]["name"])
    print("Age:", data[patient_id]["age"])

    print("\n--- Health Records ---")
    for record in data[patient_id]["records"]:
        print(record)

# Simple analytics
def analytics(data):
    patient_id = input("Enter Patient ID: ")

    if patient_id not in data:
        print("Patient not found!")
        return

    records = data[patient_id]["records"]

    if not records:
        print("No records available.")
        return

    total_bp = 0
    total_sugar = 0
    count = len(records)

    for r in records:
        total_bp += int(r["bp"])
        total_sugar += int(r["sugar"])

    print("\n--- Analytics ---")
    print("Average BP:", total_bp // count)
    print("Average Sugar:", total_sugar // count)

# Main menu
def main():
    data = load_data()

    while True:
        print("\n==== SHM-WAS MENU ====")
        print("1. Add Patient")
        print("2. Add Health Record")
        print("3. View Patient Data")
        print("4. Analytics")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient(data)
        elif choice == "2":
            add_record(data)
        elif choice == "3":
            view_patient(data)
        elif choice == "4":
            analytics(data)
        elif choice == "5":
            save_data(data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice!")

# Run program
main()