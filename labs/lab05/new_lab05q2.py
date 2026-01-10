def add_car(cars, plate, record):
      if plate not in cars:
            cars[plate] = [record]
            print("Car Added")
      else:
            print("Car already exists.")

def add_rental(cars, plate, record):
    if plate in cars:
        cars[plate].append(record)
    else:
        print("Car not found.")

def find_car(cars, plate):
    if plate in cars:
        print("Rental records:", cars[plate])
    else:
        print("Car not found.")

def show_all(cars):
    print("All cars:", cars)


# ---- Ana program ----
cars = {}

while True:
    print("\n1)Add Car")
    print("2)Search Car")
    print("3)Add Rental Record")
    print("4)Show All Cars")
    print("5)Quit")

    choice = input("Enter Choice: ")

    if choice == "1":
        plate = input("Enter car plate: ")
        name = input("Enter customer name: ")
        days = int(input("Enter number of days rented: "))
        add_car(cars, plate, (name, days))

    elif choice == "2":
        plate = input("Enter car plate: ")
        find_car(cars, plate)

    elif choice == "3":
        plate = input("Enter car plate: ")
        name = input("Enter customer name: ")
        days = int(input("Enter number of days rented: "))
        add_rental(cars, plate, (name, days))

    elif choice == "4":
        show_all(cars)

    elif choice == "5":
        print("Program Ended....")
        break

    else:
        print("Invalid choice.")