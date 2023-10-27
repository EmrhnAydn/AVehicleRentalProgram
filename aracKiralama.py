# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 02:08:27 2023

@author: emirh
"""
import datetime

#parent class
class VehicleRent:
    def __init__(self,stock):
        self.stock = stock
        self.now = 0
        
    def displayStock(self):
        print("{} Vechile available to rent".format(self.stock))
        return self.stock
     
    def rentHourly(self,n):
        if n <=0:
            print("Number Should  Be Positive")
            return None
        elif n > self.stock:
            print("Sorry, {} Vehciles available to rent".format(self.stock))
        else :
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for hourly at {} hours".format(n,self.now.hour))
            
            self.stock -=n
            return self.now
        
    def rentDaily(self,n):
        if n <=0:
            print("Number Should  Be Positive")
            return None
        elif n > self.stock:
            print("Sorry, {} Vehciles available to rent".format(self.stock))
        else :
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for daily at {} hours".format(n,self.now.hour))
            
            self.stock -=n
            return self.now
    def returnVechile(self,request,brand):
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24
        
        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        if brand == "car":
           if rentalTime and rentalBasis and numOfVehicle:
               self.stock += numOfVehicle
               now = datetime.datetime.now()
               rentalPeriod =  now - rentalTime  
               if rentalBasis == 1: #hourly
                   bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle
               elif rentalBasis ==2: #daily
                   bill = rentalPeriod.seconds/(3600*24)*car_h_price*numOfVehicle
               if (2<= numOfVehicle):
                   print("You have extra %20 discount")
                   
               print("Thank you for returning car")   
               print("Price: {}".format(bill))
        if brand == "bike":
           if rentalTime and rentalBasis and numOfVehicle:
               self.stock += numOfVehicle
               now = datetime.datetime.now()
               rentalPeriod =  now - rentalTime  
               if rentalBasis == 1: #hourly
                   bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle
               elif rentalBasis ==2: #daily
                   bill = rentalPeriod.seconds/(3600*24)*bike_h_price*numOfVehicle
               if (4 <= numOfVehicle):
                   print("You have extra %20 discount")
                   
               print("Thank you for returning bike")   
               print("Price: {}".format(bill))
        else:
            print("You don't rent a vehicle")
            return None
#child class1
class CarRent(VehicleRent):
    global discount_rate
    discount_rate =15
    def __init__(self,stock):
        super().__init__(stock)
    def discount(self,b):
        bill = b - (b*discount_rate)/100
        return bill
#child class2
class BikeRent(VehicleRent):
    def __init__(self,stock):
        super().__init__(stock)
        
    
#customer
class Customer:
    def __init__(self):
        self.bikes= 0
        self.rentalBasis_b=0
        self.rentalTime_b=0
        
        self.cars=0
        self.rentalBasis_c=0
        self.rentalTime_c=0
    def requestVehicle(self,brand):
        if brand == "bike":
            bikes = input("How Many Bikes Would You Like to Rent?")
            try:
                bikes = int(bikes)
            except ValueError:
                print("Enter Number!")
                return -1
            if bikes < 1:
                print("Number of Bikes must be greater than zero!")
                return -1
            else:
                self.bikes = bikes
                return self.bikes
            
        elif brand == "car":
            cars = input("How Many Cars Would You Like to Rent?")
            try:
                cars = int(cars)
            except ValueError:
                print("Enter Number!")
                return -1
            if cars < 1:
                print("Number of Bikes must be greater than zero!")
                return -1
            else:
                self.cars = cars
                return self.cars
            
        else:
            print("Request Vehicle Error")
    def returnVechile(self,brand):
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0        
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0
            
        else:
            print("return Vehicle erorr")
    