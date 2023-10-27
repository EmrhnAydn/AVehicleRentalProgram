# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 03:30:36 2023

@author: emirh
"""
from aracKiralama import CarRent, BikeRent, Customer
bike = BikeRent(100)
car = CarRent(100)
customer = Customer()

main_menu = True
while True:
    if main_menu:
        print("""
              ***** VEHICLE RENTAL SHOP *****
              A. BIKE MENU
              B. CAR MENU
              Q. EXIT
              """)
        main_menu = False
        
        choice = input("Enter Choice:")
    if choice == "A" or choice == "a":
        print("""
              ****BIKE MENU****
              1. Display Available bikes
              2. Request a bike on hourly basis $ 5 
              3. Request a bike on daily basis $ 84
              4. Return Bike
              5. Main Menu 
              6. Exit""")
        choice = input("Enter Choice:")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue
        if(choice == 1):
            bike.displayStock()
            choice = "A"
        elif choice == 2:
            customer.rentalTime_b =  bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("---------")
        elif choice == 3:
            customer.rentalTime_b =  bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("---------")
        elif choice == 4 :
            customer.bill = bike.returnVechile(customer.returnVechile("bike"),"bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu= True
        elif choice == 5:
            main_menu = True
        elif choice == 6 :
            break
        else:
            print("Invalid input.Please Enter between 1-6")
            main_menu = True

    elif choice == "B" or choice == "b":
        print("""
              ****CAR MENU****
              1. Display Available cars
              2. Request a car on hourly basis $ 10 
              3. Request a car on daily basis $ 192
              4. Return car
              5. Main Menu 
              6. Exit""")
        choice = input("Enter Choice:")
        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue
        if(choice == 1):
            car.displayStock()
            choice = "B"
        elif choice == 2:
            customer.rentalTime_c =  car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("---------")
        elif choice == 3:
            customer.rentalTime_c =  car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("---------")
        elif choice == 4 :
            customer.bill = car.returnVechile(customer.returnVechile("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu= True
        elif choice == 5:
            main_menu = True     
        elif choice == 6 :
            break
        else:
            print("Invalid input.Please Enter between 1-6")
            main_menu = True
    elif choice == "Q" or choice == "q":
        break
    else:
        print("Invalid Input. Please Enter A-B-Q")
        main_menu = True
    print("Thank You For Using  ")
