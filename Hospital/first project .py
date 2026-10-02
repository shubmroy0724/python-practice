patients = []

def register_patient():
    print("\nRegister Patient")

    patient_id = input("Enter patient ID: ")

    for patient in patients:
        if patient["id"] == patient_id:
            print("Patient ID already exists")
            return

    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter gender: ")
    disease = input("Enter disease: ")
    phone = input("Enter phone number: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "phone": phone
    }

    patients.append(patient)
    print("Patient registered successfully")


def search_patient():
    print("\nSearch Patient")

    patient_id = input("Enter patient ID: ")

    for patient in patients:
        if patient["id"] == patient_id:
            print("ID:", patient["id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Disease:", patient["disease"])
            print("Phone:", patient["phone"])
            return

    print("Patient not found")


def update_patient():
    print("\nUpdate Patient")

    patient_id = input("Enter patient ID: ")

    for patient in patients:
        if patient["id"] == patient_id:
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            gender = input("Enter new gender: ")
            disease = input("Enter new disease: ")
            phone = input("Enter new phone number: ")

            if name != "":
                patient["name"] = name

            if age != "":
                patient["age"] = age

            if gender != "":
                patient["gender"] = gender

            if disease != "":
                patient["disease"] = disease

            if phone != "":
                patient["phone"] = phone

            print("Patient updated successfully")
            return

    print("Patient not found")


def delete_patient():
    print("\nDelete Patient")

    patient_id = input("Enter patient ID: ")

    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            print("Patient deleted successfully")
            return

    print("Patient not found")


def show_patients():
    print("\nAll Patients")

    if len(patients) == 0:
        print("No patients found")
        return

    for patient in patients:
        print("ID:", patient["id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Disease:", patient["disease"])
        print("Phone:", patient["phone"])
        print()


while True:
    print("\nHospital Patient Record System")
    print("1. Register Patient")
    print("2. Search Patient")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Show All Patients")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_patient()

    elif choice == "2":
        search_patient()

    elif choice == "3":
        update_patient()

    elif choice == "4":
        delete_patient()

    elif choice == "5":
        show_patients()

    elif choice == "6":
        print("Program closed")
        break

    else:
        print("Invalid choice")