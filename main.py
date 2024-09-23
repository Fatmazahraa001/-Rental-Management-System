from lib.landlord import Landlord
from lib.tenant import Tenant
from lib.apartment import Apartment


def main_menu():
    while True:
        print("===============MAIN MENU==============")
        print("1. Manage Tenant")
        print("2. Manage Landlord")
        print("3. Manage Apartment")
        print("4. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            return tenant_operations()
        elif choice == "2":
            return landlord_operations()
        elif choice == "3":
            return apartment_operations()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice")


def tenant_operations():
    while True:
        print("\n***Tenant Menu***")
        print("1. Create Tenant")
        print("2. Fetch tenant by id")
        print("3. Delete tenant")
        print("4. Get total rent")
        print("5. Fetch tenants by landlord id")
        print("6. Get average rent for a specific landlord")
        print("7. Get total tenants")
        print("8. Update tenant details")
        print("9. Fetch all tenants")
        print("7. Return to main menu")

        choice = input("\nEnter your choice: ")
        tenant = Tenant()

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = input("Enter age: ")
            phone_number = input("Enter phone number: ")
            rent = input("Enter rent: ")
            landlord_id = input("Enter landlord id: ")
            apartment_id = input("Enter apartment id: ")

            create_tenant_id = tenant.create_tenant(name, email, age, phone_number, rent, landlord_id, apartment_id)
            print(f"Tenant {create_tenant_id} created successfully")
        elif choice == "2":
            tenant_id = input("Enter tenant id: ")
            tenant_details = tenant.get_tenants_by_id(tenant_id)
            print(tenant_details)
        elif choice == "3":
            tenant_id = input("Enter tenant id: ")
            tenant.delete_tenant(tenant_id)
            print(f"Tenant {tenant_id} deleted successfully")
        elif choice == "4":
            landlord_id = input("Enter landlord id: ")
            total = tenant.get_total_rents(landlord_id)
            print(f"Total rent collected: {total[0]}")
        elif choice == "5":
            landlord_id = input("Enter landlord id: ")
            landlord_tenants = tenant.get_tenants_by_landlord_id(landlord_id)
            print(landlord_tenants)
        elif choice == "6":
            landlord_id = input("Enter landlord id: ")
            average = tenant.get_average_rent(landlord_id)
            print(f"Average rent of landlord {landlord_id} is : {average[0]}")
        elif choice == "7":
            total_tenant = tenant.count_all_tenants()
            print(f"Total tenants: {total_tenant[0]}")
        elif choice == "8":
            tenant_id = input("Enter tenant id: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = input("Enter age: ")
            phone_number = input("Enter phone number: ")
            rent = input("Enter rent: ")
            landlord_id = input("Enter landlord id: ")
            apartment_id = input("Enter apartment id: ")

            tenant.update_tenant(tenant_id, name, email, age, phone_number, rent, landlord_id, apartment_id)
            print(f"Tenant {tenant_id} updated successfully")
        elif choice == "9":
            all_tenants = tenant.fetch_all_tenants()
            print(all_tenants)
        elif choice == "7":
            return main_menu()

def landlord_operations():
    while True:
        
        print("\n***Landlord Menu***")
        print("1. Create Landlord")
        print("2. Get landlord by id")
        print("3. Update landlord by id")
        print("4. Delete landlord")
        print("5. Count all landlords")
        print("6. Fetch all landlords")
        print("7. Return to main menu")

        choice = input("\n Enter your choice: ")

        landlord = Landlord()
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")           

            create_tenant_id = landlord.create_landlord(name, email)
            print(f"Landlord {create_tenant_id} created successfully")
        elif choice == "2":
            landlord_id = input("Enter landlord id: ")
            landlord_details = landlord.get_landlord_by_id(landlord_id)
            print(landlord_details)
        elif choice == "3":
            landlord_id = input("Enter landlord id: ")
            name = input("Enter name: ")
            email = input("Enter email: ")

            landlord.update_landlord_by_id(landlord_id, name, email)
            print(f"Landlord {landlord_id} updated successfully")
        elif choice == "4":
            landlord_id = input("Enter landlord id: ")
            landlord.delete_landlord_by_id(landlord_id)
            print(f"Landlord {landlord_id} deleted successfully")
        elif choice == "5":
            total = landlord.count_all_landlords()
            print(f"Total number of landlords: {total[0]}")
        elif choice == "6":
            all_landlords = landlord.fetch_all_landlords()
            print(all_landlords)
        elif choice == "7":
            return main_menu()
    
def apartment_operations():
    while True:
        print("\n***Apartment Menu***")
        print("1. Create Apartment")
        print("2. Get Apartment by Id")
        print("3. Update apartment by id")
        print("4. Fetch all apartments")
        print("5. Delete apartment by Id")
        print("6. Fetch apartment by landlord id")
        print("7. Get total number of all apartments") 
        print("8. Get all apartments in certain location")       
        print("9. Return to main menu")

        choice = input("\n Enter your choice: ")
        apartment = Apartment()

        if choice == "1":
            apartment_name = input("Enter apartment name: ")  
            location = input("Enter location: ")          
            landlord_id = input("Enter landlord id: ")
            create_apartment_id = apartment.create_apartment(apartment_name, location, landlord_id)
            print(f"Apartment {create_apartment_id} created successfully")
        elif choice == "2":
            apartment_id = input("Enter apartment id: ")
            apartment_details = apartment.get_apartments_by_id(apartment_id)
            print(apartment_details)
        elif choice == "3":
            apartment_id = input("Enter apartment id: ")
            apartment_name = input("Enter apartment name: ")  
            location = input("Enter location: ")          
            landlord_id = input("Enter landlord id: ")
            apartment.update_apartment_by_id(apartment_id, apartment_name, location, landlord_id)
            print(f"Apartment {apartment_id} updated successfully")
        elif choice == "4":
            all_apartments = apartment.fetch_all_apartments()
            print(all_apartments)
        elif choice == "5":
            apartment_id = input("Enter apartment id: ")
            apartment.delete_apartment_by_id(apartment_id)
            print(f"Apartment {apartment_id} deleted successfully")
        elif choice == "6":
            apartment_id = input("Enter landlord id: ")
            apartment_details = apartment.get_apartment_by_landlord_id(apartment_id)
            print(apartment_details)
        elif choice == "7":
            total = apartment.count_all_apartments()
            print(f"Total number of apartments: {total[0]}")
        elif choice == "8":
            location = input("Enter location: ")
            apartment_details = apartment.get_apartments_by_location(location)
            print(apartment_details)
        elif choice == "9":
            return main_menu()

main_menu()