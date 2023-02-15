import pickle

class Car:
    def __init__(self, vehicle_ID="", registration="", date_of_registration=None, engine_size=0, purchase_price=0.00):
        self.vehicle_ID = vehicle_ID
        self.registration = registration
        self.date_of_registration = date_of_registration
        self.engine_size = engine_size
        self.purchase_price = purchase_price

FILENAME = "carfile.DAT"

def is_address_available(address):
    with open(FILENAME, "rb+") as file:
        try:
            file.seek(address)
            record = pickle.load(file)
        except pickle.UnpicklingError:
            return False
        address_available = True if record else False
    return address_available

def write_record():
    car_record = input_record_data()
    try:   
        with open(FILENAME, "rb+") as file:
            record_address = generate_hash(int(car_record.vehicle_ID))
            while is_address_available(record_address):
                record_address += 1
            file.seek(record_address)
            pickle.dump(car_record, file)
    except IOError:
        print(f"{FILENAME} can't be opened")

def input_record_data():
    vehicle_ID = input("Please enter the vehicle ID: ")
    registration = input("Please enter the registration: ")
    date_of_registration = input("Please enter the enter the date of registration: ")
    engine_size = int(input("Please enter the engine size: "))
    purchase_price = float(input("Please enter the purchase price: "))
    new_car = Car(vehicle_ID, registration, date_of_registration, engine_size, purchase_price)
    return new_car

def initialise_file():
    with open(FILENAME, "w") as file:
        for i in range(1000):
            file.write("\n")

def read_record():
    record_key = input("Please enter the vehicle ID you want search for: ")
    address = generate_hash(int(record_key))
    with open(FILENAME, "rb+") as file:
        while is_address_available(address):
            address += 1
        file.seek(address)
        record = pickle.load(file)
    print(record.vehicle_ID)
    print(record.registration)

def generate_hash(value):
    return (int(value) % 1000)

def main():
    initialise_file()
    for i in range(10):
        write_record()
    read_record()
main()