
#Project 08 — Vehicle Rental Management System

vehicles = []

def add_vehicle():
    print("\nAdd Vehicle")

    vehicle_id = input("Enter vehicle ID: ")

    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            print("Vehicle ID already exists")
            return

    name = input("Enter vehicle name: ")
    vehicle_type = input("Enter vehicle type: ")
    price = input("Enter rental price per day: ")

    vehicle = {
        "id": vehicle_id,
        "name": name,
        "type": vehicle_type,
        "price": price,
        "status": "Available"
    }

    vehicles.append(vehicle)
    print("Vehicle added successfully")


def rent_vehicle():
    print("\nRent Vehicle")

    vehicle_id = input("Enter vehicle ID: ")

    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            if vehicle["status"] == "Rented":
                print("Vehicle is already rented")
                return

            vehicle["status"] = "Rented"
            print("Vehicle rented successfully")
            return

    print("Vehicle not found")


def return_vehicle():
    print("\nReturn Vehicle")

    vehicle_id = input("Enter vehicle ID: ")

    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            if vehicle["status"] == "Available":
                print("Vehicle is already available")
                return

            vehicle["status"] = "Available"
            print("Vehicle returned successfully")
            return

    print("Vehicle not found")


def calculate_rent():
    print("\nCalculate Rental Charges")

    vehicle_id = input("Enter vehicle ID: ")

    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            days = int(input("Enter number of days: "))

            price = float(vehicle["price"])
            total = price * days

            print("Vehicle:", vehicle["name"])
            print("Days:", days)
            print("Total rental charge:", total)
            return

    print("Vehicle not found")


def show_vehicles():
    print("\nAll Vehicles")

    if len(vehicles) == 0:
        print("No vehicles found")
        return

    for vehicle in vehicles:
        print("ID:", vehicle["id"])
        print("Name:", vehicle["name"])
        print("Type:", vehicle["type"])
        print("Price per day:", vehicle["price"])
        print("Status:", vehicle["status"])
        print()


while True:
    print("\nVehicle Rental Management System")
    print("1. Add Vehicle")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. Calculate Rental Charges")
    print("5. Show All Vehicles")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_vehicle()

    elif choice == "2":
        rent_vehicle()

    elif choice == "3":
        return_vehicle()

    elif choice == "4":
        calculate_rent()

    elif choice == "5":
        show_vehicles()

    elif choice == "6":
        print("Program closed")
        break

    else:
        print("Invalid choice")